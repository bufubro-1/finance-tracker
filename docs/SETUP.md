# Finance Tracker — Local Runtime Setup

**Accepted implementation:** TASK-001 Streamlit runtime shell at `5052b5b`. Its existing commands remain below. Keep it on loopback with synthetic configuration. Historical trusted-LAN instructions describe the old accepted interface, not authorization to expose it or use sensitive data under the revised release policy.

**Accepted Django foundation:** TASK-022A is integrated at `18c1066`. It supplies Dashboard/Accounts navigation, synthetic sample cards, a development banner and the custom email user model.

**Accepted authentication:** TASK-025A's dedicated synthetic provisioning and standard Django login/logout are integrated at `d27f06b`.

**TASK-004A1, prepared for human review:** the isolated task worktree adds owned savings accounts, exact synthetic USD openings, cards and Dashboard totals. Its implementation and complete M-009 owner demonstration await human acceptance; this is not a production application.

**Intended later release environment:** Raspberry Pi 5 (8 GB), CasaOS, Docker Compose, PostgreSQL and Cloudflare Tunnel with HTTPS. TASK-024 verifies ARM64/runtime/OS/image/Compose compatibility; TASK-020 separately implements/rehearses authorized deployment and recovery. No Dockerfile, Compose configuration, release PostgreSQL database, CI workflow, tunnel or CasaOS setup is created by this task. Existing x86_64/Python 3.14.8 evidence does not establish that environment's compatibility.

All intermediate work uses synthetic data. Full authentication, ownership authorization, Admin MFA, privacy, recovery and release verification precede real users or sensitive data. See [approved schedule](planning/PROJECT_SCHEDULE.md) and [Decision Log](DECISION_LOG.md). Python 3.14.x development selection remains approved; version/image choices for the intended host remain a recorded gate.

## TASK-004A1 local Django prototype (Bash)

From the task worktree, create and install the Python 3.14 environment with the
same venv/pip setup commands in the existing instructions below. The updated
lock retains all TASK-001 pins and adds Django 5.2.19, asgiref 3.13.0 and
sqlparse 0.6.1. Django 5.2 supports Python 3.14 from 5.2.8 onward; see the
[official compatibility notes](https://docs.djangoproject.com/en/5.2/releases/5.2/).
Pi/ARM64 and release compatibility remain unverified.

Configure the separate prototype database and a private development signing key:

```bash
umask 077
install -d -m 700 data
export FINANCE_TRACKER_PROTOTYPE_DATABASE_PATH="$PWD/data/prototype.sqlite3"
export FINANCE_TRACKER_DJANGO_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(64))')"
export DJANGO_SETTINGS_MODULE=finance_tracker.django_app.settings
python -m django check
python -m django migrate --noinput
python -m django provision_prototype_user
python -m finance_tracker.django_app
```

Run these commands from the TASK-004A1 worktree, not the TASK-001 checkout.
The database is `data/prototype.sqlite3` relative to that worktree; it is
gitignored, disposable and strictly synthetic. Never use the TASK-001 database.

Provisioning creates only `sample@example.invalid`, an ordinary active synthetic
user. Enter a new development-only password twice at the hidden terminal prompts.
No password is supplied in commands, printed or stored in plaintext. The command
requires the exact prototype settings module and SQLite; it does not depend on
`DEBUG=True`. It requires explicit migrations first and never changes an existing
identity or password. A repeated invocation reports that the identity exists;
skip provisioning on later starts. There is no default password or recovery flow.
If secure hidden input is unavailable, provisioning stops without creating a user.

Open `http://127.0.0.1:8000`; sign in with that synthetic email and the password
you chose. Anonymous Dashboard/Accounts visits lead to login. The sign-in form
retains the email after an error, uses a generic authentication failure and never
redisplays the password. Use **Sign out** to submit the CSRF-protected logout form;
visiting `/logout/` with GET does not log you out. Stop the server with Ctrl+C.
Optional `--port 8001`
changes only the port. The launcher fixes the address to `127.0.0.1`, selects
prototype settings even if `DJANGO_SETTINGS_MODULE` was inherited, disables
autoreload and serves packaged CSS using Django's development static handler.
`--insecure` is supplied internally solely to serve static files with `DEBUG=False`.
Use this guarded launcher; do not bind a development server to a LAN/public address.
No deployment, proxy, cloud credentials or external calls are involved.

The database path defaults to `data/prototype.sqlite3` relative to the launch
directory. It must be a local file in an existing owner-owned private directory
(0700); an existing file must be owner-owned and private (0600). The configured
legacy database path is rejected if it resolves to the same file path. No legacy
configuration is changed. Path validation creates nothing; explicit `migrate`
creates the synthetic identity/session and account/opening schema. Startup does
not run migrations or provision identities. Keep the signing key local and out of Git; regenerating
it invalidates existing authentication sessions. Keep the same key when checking
session persistence across server restarts. Do not enter real identities or records.

Login returns to the requested safe same-host destination, or Dashboard by
default. Logout always returns to login. Sessions use Django's database backend
and default expiry; logout invalidates the current session on the server. Cookies
are HttpOnly for sessions and SameSite=Lax for sessions/CSRF. Secure-only cookies
are not enabled for this loopback HTTP prototype; HTTPS/proxy/cookie policy,
throttling, membership, recovery, Admin MFA and full authorization/privacy remain
release work. The development login is not production security acceptance.

Open **Hesaplar → Birikim hesabı oluştur**, enter a unique synthetic name, explicitly
select **USD**, and enter an opening balance such as `1000.00`. Save to view the
owned account card and its exact balance; **Genel Bakış** shows the total of your saved
openings. Empty pages guide you to create the first account. Invalid fields explain
the problem and keep your entries. The collapsed illustrative card preview remains
**not saved** and never counts toward totals.

The application interface and validation/error messages are Turkish. The name
**Finance Tracker** and approved USD numeric convention remain unchanged: enter
`1000.00` using a decimal point, as explained in the Turkish form guidance.
The **Koyu tema** button is available on login and authenticated pages and supports
keyboard activation. First use follows the browser's system color preference;
an explicit choice is stored under `finance-tracker-theme` in browser localStorage
and survives navigation/reload. Only the display preference is stored there.
If storage is blocked, switching still works on the current page. Without JavaScript,
CSS follows the system preference and the manual switch stays hidden.

After updating to this interface revision, stop the running development server
with Ctrl+C and run `python -m finance_tracker.django_app` again in the same
configured terminal. Refresh the browser (Ctrl+F5 if needed). No new database
migration or user provisioning is needed for the language/theme changes.

USD with scale 2 is an approved synthetic prototype convention, not an inferred
owner preference. First creation saves that fixed currency metadata. Other
currencies are rejected; there is no FX or multi-currency total. Names are trimmed,
Unicode NFKC-normalized, limited to 100 characters and unique per owner ignoring
case; control/invisible characters are rejected. Different users may use the same
name. Balances use decimal digits with up to two fractional places, without commas
or exponent notation. Zero is valid; negatives, nonfinite values, excess precision
and values above `92233720368547758.07` USD are rejected without rounding.
Storage is integer minor units; calculations and display use no financial floats.

An opening establishes a starting position; it does not create a contribution or
any movement record. Opening dates use synthetic UTC; the service accepts an
injected aware clock for tests. There are no update, rename/archive, transaction,
transfer, valuation, goal, profile or reporting features in this slice.

Refreshing the saved page creates nothing. Repeating the same creation submission
returns the existing account; reusing its key with changed details fails. Account,
opening and guard commit together. A busy SQLite error keeps the form available
for retry. A new form uses a new key; a repeated account name still fails validation.
All reads and creates use the signed-in owner. Privileged staff/superuser identities
are denied the prototype financial pages; this is not the later release role policy.

To demonstrate persistence, stop the server and start the same command again from
the same worktree with the same database path. Keep the signing key to retain your
session. Do not rerun provisioning or replace/delete the database. Saved accounts
and exact totals remain. Migrations are explicit and additive; the existing custom
identity model/migration is unchanged.

The database is disposable prototype storage, never a production migration source.
The custom user model is established before the first migration so subsequent
tasks can extend it. Django admin is not exposed and superuser provisioning is
disabled; application Admin policy belongs to later identity tasks.

Verify the task with:

```bash
python -m pytest -q
python -m pip check
python -m django makemigrations --check --dry-run
```

For focused account coverage run `python -m pytest -q tests/django/test_accounts.py`.
For authentication and prototype regression coverage, run
`python -m pytest -q tests/django` before the complete suite.
The combined suite runs the unchanged TASK-001 tests and isolated Django tests.
The actual startup/restart checks require Linux local socket permission. Django tests
use private temporary databases and child interpreters so their settings cannot
leak into Streamlit tests. TASK-025A covers sign-in/logout and authenticated
navigation; TASK-004A1 adds creation, exactness, ownership, duplicate/rollback and
process/server-restart scenarios. The complete owner demonstration and acceptance
remain pending. See the [TASK-004A1 review report](testing/TASK-004A1_REVIEW.md),
the [TASK-025A review report](testing/TASK-025A_REVIEW.md)
and the historical [TASK-022A review report](testing/TASK-022A_REVIEW.md).

## Existing TASK-001 instructions


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

`requirements.lock` pins the Linux/Python 3.14 environment, including
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
