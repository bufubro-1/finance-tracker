# Finance Tracker local setup and development

TASK-001 provides a Python package, validated process configuration, and a minimal
Streamlit shell. Use the current Linux host and Python 3.14.x under DEC-017; the
initial tested interpreter is 3.14.8. The owner authorized TASK-001 execution after
DEC-018. See [the backlog](planning/BACKLOG.md) for its limited scope.

## Create the environment (Bash)

Run these Bash commands from the task worktree or your reviewed project checkout.
Fish users should use the complete Fish example below; Bash activation and
`set -a` are not Fish syntax.

```bash
python3.14 --version
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.lock
python -m pip install --no-build-isolation --no-deps -e '.[dev]'
python -m pip check
```

`requirements.lock` pins the full tested Linux/Python 3.14 environment, including
pip, the setuptools build backend, pytest, and Streamlit's transitive dependencies.
`pyproject.toml` declares the direct application and development requirements.
The editable installation uses the already installed, pinned build backend.
Internet access is required to download packages initially. Application startup
and tests need no external accounts. To update dependencies, resolve and validate
in a fresh venv, review metadata and startup tests, and regenerate the pins;
do not change the approved Python version to work around a dependency failure.

Python 3.14 is listed by [Streamlit's installation guide](https://docs.streamlit.io/get-started/installation/command-line).
The installed Streamlit 1.66.1 and pytest 9.2.0 metadata both list Python 3.14.
Both were installed and exercised on Linux x86_64 / Python 3.14.8; `pip check`
reported no broken requirements. Pandas 3.1.1, NumPy 2.5.4, and PyArrow 26.0.1
were installed as Streamlit dependencies with CPython 3.14 wheels. Plotly and
provider SDKs are unnecessary for this shell and are deferred until their tasks.
This compatibility evidence covers the current host and runtime shell.

## Configure and start locally (Bash)

Create a private data directory before validating the configured path:

```bash
umask 077
install -d -m 700 data
if [ ! -e .env ]; then
  cp --no-clobber .env.example .env
fi
chmod 600 .env
```

The template is copied only on first setup. Repeating these steps preserves the
contents of an existing `.env`; `--no-clobber` also prevents accidental replacement.

Edit `.env` locally. Set an explicit reporting currency and its matching scale
from the table below; the template deliberately has no currency default.
For example, `USD` / `2` is a possible selection, not an owner preference.
The app reads process environment variables; it does **not** read `.env`
automatically. Load only your own trusted shell-compatible file:

```bash
set -a
source .env
set +a
python -m finance_tracker
```

## First run with Fish

Open Fish in the project directory. This complete example creates/activates the
Python environment, installs dependencies, creates a private database directory,
and supplies every required configuration variable before starting Streamlit.
It uses TRY / scale 2 as an explicit example; choose another supported pair if
needed. Run installation steps once; for later sessions activate with
`source .venv/bin/activate.fish` and repeat the configuration/startup block.

```fish
python3.14 --version
python3.14 -m venv .venv
source .venv/bin/activate.fish
python -m pip install -r requirements.lock
python -m pip install --no-build-isolation --no-deps -e '.[dev]'
python -m pip check
```

```fish
umask 077
install -d -m 700 data
begin
    set -lx FINANCE_TRACKER_REPORTING_CURRENCY TRY
    set -lx FINANCE_TRACKER_MINOR_UNIT_SCALE 2
    set -lx FINANCE_TRACKER_DATABASE_PATH "$PWD/data/finance_tracker.sqlite3"
    set -lx FINANCE_TRACKER_GEMINI_ENABLED false
    set -lx FINANCE_TRACKER_TELEGRAM_ENABLED false
    python -m finance_tracker
end
```

The `set -lx` values are exported only inside the `begin`/`end` block. The data
directory must be owned by your user with mode 0700; an existing database file
must also be private (normally mode 0600). This shell only validates its path;
no database file or schema is created.

The Fish example does not create, read, or overwrite `.env`. The app reads the
exported process environment, and Bash-style `.env` assignments must not be
loaded with Fish's `source`. Keep any existing `.env` unchanged and enter your
chosen values in the Fish block instead. No additional dotenv parser, shell
plugin, Gemini credentials, or Telegram credentials are required.

## Inspect the local interface

Open `http://127.0.0.1:8501`. Stop with Ctrl+C. The launcher explicitly binds
`127.0.0.1`, keeps Streamlit's CORS/XSRF protection on, disables usage telemetry,
and runs headless, even when launched outside the checkout. The repository's
`.streamlit/config.toml` supplies the same defaults for direct Streamlit use:

```bash
python -m streamlit run src/finance_tracker/app.py --server.address=127.0.0.1 --browser.gatherUsageStats=false
```

Run the direct command from the checkout with the venv activated and package
installed. The packaged launcher is the preferred local command. Streamlit's
normal environment settings, such as `STREAMLIT_SERVER_PORT`, can select a port;
the launcher's explicit loopback and security flags take precedence.

A valid configuration shows the currency/scale and disabled integrations.
With the Fish example, expect `Local configuration is valid.`, TRY at scale 2,
`Gemini: disabled` and `Telegram: disabled`, and an explicit message that
financial tracking is not yet available.
Missing/invalid core configuration displays an actionable error in the page and
stops rendering the shell. It never prints the invalid value. Integration
configuration issues appear as warnings and leave the shell usable.

## Configuration variables

| Variable | Default | Validation and behavior |
|---|---|---|
| `FINANCE_TRACKER_REPORTING_CURRENCY` | Required | Explicit supported currency; whitespace trimmed and letters normalized to uppercase. |
| `FINANCE_TRACKER_MINOR_UNIT_SCALE` | Required | Must equal the selected currency's scale below; no silent inference or rounding. |
| `FINANCE_TRACKER_DATABASE_PATH` | `data/finance_tracker.sqlite3` | Local file path; relative to the launch directory, `~` allowed. Parent must exist, be owner-owned, mode 0700, and readable/writable/searchable. Existing target must be a regular owner-owned file, readable/writable with no group/other permission (normally 0600). Directories, missing parents, SQLite URIs, memory paths, and inaccessible paths are rejected. |
| `FINANCE_TRACKER_GEMINI_ENABLED` | `false` | `true`/`false`, case insensitive; malformed values warn and stay disabled. |
| `FINANCE_TRACKER_TELEGRAM_ENABLED` | `false` | Same validation; stays disabled in TASK-001. |
| `GEMINI_API_KEY` | Absent | Only presence checked if Gemini is requested; never stored in the configuration object or displayed. No key is needed now. |
| `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` | Absent | Only presence checked if Telegram is requested; values are never displayed or treated as validated destinations. No credentials are needed now. |

| Initially supported ISO 4217 currency | Minor-unit scale |
|---|---:|
| EUR | 2 |
| GBP | 2 |
| JPY | 0 |
| KWD | 3 |
| TRY | 2 |
| USD | 2 |

This explicit initial subset uses the code/scale pairs in
[SIX's ISO 4217 List One](https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/lists/list-one.xml).
Synthetic `TEST` and unknown codes are rejected for runtime configuration.
Currency/scale selection here is configuration only. Dataset initialization,
persisted currency locking, numeric policies, and SQLite schema are later work.
The shell does not create/open a database, verify an existing file's schema, or
change its contents or permissions. Use owner-controlled local disk, outside
network shares and synced folders; path validation cannot determine storage
hardware or remote mount safety.

Both adapters stay disabled even if flags and credentials are supplied. Missing
credentials produce redacted configuration warnings; supplied credentials produce
a scope warning. No clients, sends, schedules, inbound handlers, or provider calls
exist in TASK-001. Integration behavior and recipient validation belong to later
tasks with their existing decision gates.

## Local-network security

Loopback use needs no LAN admission. There is no application login: any admitted
device has full access to the eventual dataset. Do not expose Streamlit on the
public internet, port-forward it, or use a public tunnel.

Before any LAN use, choose a specific private interface address, configure the
host firewall to allow only explicitly trusted source devices to the selected
TCP port, and deny other sources. Keep router forwarding disabled. Apply and
check those rules **before** binding beyond loopback. Once the owner has made
those restrictions, use the direct Streamlit command above with
`--server.address=YOUR_PRIVATE_INTERFACE_IP`; do not use the local-only launcher
for LAN binding. Prefer a specific interface rather than `0.0.0.0`. Keep CORS
and XSRF protection enabled. Test from one allowed and one denied device before
using personal data; stop the server if the denied device can connect. Firewall
commands depend on the owner's host policy and are not applied by the app.

Keep `.env`, future records, journals, exports, backups and logs owner-only and
outside version control. Existing ignore rules cover those paths. Keep real
credentials out of command history, screenshots and review artifacts. The initial
template contains no secrets; core development uses synthetic data only.

## Development verification

```bash
python -m pytest -q
python -m pip check
```

Tests use temporary private paths, synthetic currency selections, no provider
credentials, Streamlit AppTest, and a short-lived loopback server on an unused
port. The startup test requires local socket permission and Linux `/proc/net/tcp`;
it asserts the actual loopback listener and health response, then stops the
process group. UI tests execute the script and verify valid configuration,
redacted errors, and continued availability after integration warnings. Unit
tests also import configuration without site packages to check UI independence.

These tests cover TASK-001's portions of TC-001/002/037/038/041/044. They do not
complete the broader persistence, currency immutability, financial workflow,
physical LAN-device, or milestone acceptance cases. A fresh-host installation,
allowed/denied LAN-device rehearsal, and human acceptance remain separate checks.
