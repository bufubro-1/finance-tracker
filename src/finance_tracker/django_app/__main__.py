"""Start only the loopback development server; never migrate or seed on startup."""

import argparse
import os
import sys


def main(argv=None):
    if sys.version_info[:2] != (3, 14):
        print("Finance Tracker requires Python 3.14.x.", file=sys.stderr)
        return 1
    parser = argparse.ArgumentParser(description="Local synthetic Django prototype")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args(argv)
    if not 1 <= args.port <= 65535:
        parser.error("--port must be between 1 and 65535")
    # Do not accept inherited release settings or a caller-supplied bind address.
    os.environ["DJANGO_SETTINGS_MODULE"] = "finance_tracker.django_app.settings"
    os.umask(0o077)
    from django.core.exceptions import ImproperlyConfigured
    from django.core.management import execute_from_command_line

    try:
        execute_from_command_line([
            "finance-tracker-prototype", "runserver", f"127.0.0.1:{args.port}",
            "--noreload", "--insecure",
        ])
    except ImproperlyConfigured as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
