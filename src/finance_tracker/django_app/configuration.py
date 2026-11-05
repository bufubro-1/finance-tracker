"""Validated Django configuration; never open a database or initialize providers."""

import ipaddress
import logging
import os
from pathlib import Path
import re
import stat
from urllib.parse import urlsplit

from django.core.exceptions import ImproperlyConfigured


def invalid(name, requirement):
    # Only caller-owned variable names and fixed guidance enter diagnostics.
    raise ImproperlyConfigured(f"{name} {requirement}. See docs/SETUP.md.") from None


def read_secret(env, name, *, minimum=1):
    """Read one explicit input; files must be owned, private, regular, not symlinks."""
    if name in env and name + "_FILE" in env:
        invalid(name, "requires exactly one of the value or its _FILE input")
    value = env.get(name, "")
    if name + "_FILE" in env:
        descriptor = None
        try:
            path = Path(env[name + "_FILE"]).expanduser()
            descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
            info = os.fstat(descriptor)
            if (not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid()
                    or stat.S_IMODE(info.st_mode) & 0o077 or not info.st_mode & stat.S_IRUSR):
                raise ValueError
            with os.fdopen(descriptor, "rb") as stream:
                descriptor = None
                raw = stream.read(4097)
            if len(raw) > 4096:
                raise ValueError
            value = raw.decode("utf-8").removesuffix("\n").removesuffix("\r")
        except (OSError, ValueError, RuntimeError):
            invalid(name, "requires a readable owner-only regular secret file of at most 4096 bytes")
        finally:
            if descriptor is not None:
                os.close(descriptor)
    if (not isinstance(value, str) or len(value.strip()) < minimum
            or "\x00" in value or "\n" in value or "\r" in value):
        invalid(name, f"requires at least {minimum} characters without line breaks")
    return value


def required(env, name):
    value = env.get(name, "")
    if not value or value != value.strip() or any(ord(c) < 32 for c in value):
        invalid(name, "requires an explicit valid value")
    return value


def host(value):
    """Exact DNS names or IP literals, never URL, port, wildcard or suffix rules."""
    candidate = value[1:-1] if value.startswith("[") and value.endswith("]") else value
    try:
        address = ipaddress.ip_address(candidate)
        return (str(address) == candidate and "%" not in candidate
                and (address.version == 4 or value.startswith("[")))
    except ValueError:
        return bool(len(value) <= 253 and re.fullmatch(
            r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?(?:\.[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)*",
            value,
        ))


def release_configuration(env):
    """Return a settings dictionary, without loading the PostgreSQL driver."""
    prefix = "FINANCE_TRACKER_RELEASE_"
    key = read_secret(env, prefix + "SECRET_KEY", minimum=50)
    if len(set(key)) < 5 or key.startswith("django-insecure-"):
        invalid(prefix + "SECRET_KEY", "requires a private independently generated signing key")
    hosts_name = prefix + "ALLOWED_HOSTS"
    hosts = [item.strip() for item in required(env, hosts_name).split(",")]
    if not all(host(item) for item in hosts):
        invalid(hosts_name, "requires comma-separated exact lowercase hosts without ports or wildcards")
    origins_name = prefix + "CSRF_TRUSTED_ORIGINS"
    origins = [item.strip() for item in required(env, origins_name).split(",")]
    try:
        for origin in origins:
            parts = urlsplit(origin)
            origin_host = f"[{parts.hostname}]" if parts.hostname and ":" in parts.hostname else parts.hostname
            canonical = f"https://{origin_host}" + (f":{parts.port}" if parts.port is not None else "")
            if (parts.scheme != "https" or origin_host not in hosts
                    or parts.username is not None or parts.password is not None
                    or parts.path or parts.query or parts.fragment
                    or (parts.port is not None and not 1 <= parts.port <= 65535)
                    or origin != canonical or "*" in origin):
                raise ValueError
    except ValueError:
        invalid(origins_name, "requires exact HTTPS origins matching allowed hosts, without paths or credentials")
    db = {}
    for option in ("NAME", "USER"):
        name = prefix + "DB_" + option
        value = required(env, name)
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]{0,62}", value):
            invalid(name, "requires an ASCII database identifier of at most 63 characters")
        db[option] = value
    db_host_name = prefix + "DB_HOST"
    db_host = required(env, db_host_name)
    if not host(db_host):
        invalid(db_host_name, "requires an exact database hostname or IP literal")
    db["HOST"] = db_host.strip("[]")
    port_name = prefix + "DB_PORT"
    port = env.get(port_name, "5432")
    if not re.fullmatch(r"[0-9]{1,5}", port) or not 1 <= int(port) <= 65535:
        invalid(port_name, "requires an integer port between 1 and 65535")
    db.update(
        ENGINE="django.db.backends.postgresql", PORT=port,
        PASSWORD=read_secret(env, prefix + "DB_PASSWORD"), CONN_MAX_AGE=0,
    )
    proxy_name = prefix + "TRUST_PROXY_HTTPS"
    proxy = env.get(proxy_name, "false")
    if proxy not in ("true", "false"):
        invalid(proxy_name, "must be exactly true or false")
    static_name = prefix + "STATIC_ROOT"
    static_root = Path(required(env, static_name))
    if not static_root.is_absolute() or ".." in static_root.parts or str(static_root) == "/":
        invalid(static_name, "requires a dedicated absolute static-assets directory")
    return {
        "SECRET_KEY": key, "ALLOWED_HOSTS": hosts, "CSRF_TRUSTED_ORIGINS": origins,
        "DATABASES": {"default": db}, "STATIC_ROOT": static_root,
        "SECURE_PROXY_SSL_HEADER": ("HTTP_X_FORWARDED_PROTO", "https") if proxy == "true" else None,
    }


class MetadataFormatter(logging.Formatter):
    """Do not interpolate messages, arguments, requests or exception tracebacks."""

    def format(self, record):
        level = logging.getLevelName(record.levelno) if record.levelno in (10, 20, 30, 40, 50) else "EVENT"
        status = getattr(record, "status_code", None)
        suffix = f" HTTP {status}" if type(status) is int and 100 <= status <= 599 else ""
        return f"Finance Tracker {level}{suffix}"


def prototype_database():
    """Validate without opening, creating or changing a database or directory."""
    message = (
        "FINANCE_TRACKER_PROTOTYPE_DATABASE_PATH must name a separate local SQLite "
        "file in an existing owner-only readable/writable directory. See docs/SETUP.md."
    )
    raw = os.environ.get("FINANCE_TRACKER_PROTOTYPE_DATABASE_PATH", "data/prototype.sqlite3")
    try:
        if not raw.strip() or raw == ":memory:" or "://" in raw or raw.startswith("file:"):
            raise ValueError
        path = Path(raw).expanduser().resolve()
        legacy = Path(os.environ.get(
            "FINANCE_TRACKER_DATABASE_PATH", "data/finance_tracker.sqlite3"
        )).expanduser().resolve()
        if path == legacy:
            raise ValueError
        for target in (path.parent, path) if path.exists() else (path.parent,):
            info = target.stat()
            mode = stat.S_IMODE(info.st_mode)
            required = 0o700 if target == path.parent else 0o600
            if (info.st_uid != os.getuid() or mode & 0o077
                    or mode & required != required
                    or not os.access(target, os.R_OK | os.W_OK)
                    or (target == path.parent and not target.is_dir())
                    or (target == path and not target.is_file())):
                raise ValueError
        return path
    except (OSError, ValueError, RuntimeError):
        raise ImproperlyConfigured(message) from None
