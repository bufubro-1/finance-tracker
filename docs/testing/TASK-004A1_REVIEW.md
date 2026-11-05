# TASK-004A1 — Account creation and balances review

Status: **Implemented for human review; uncommitted, not accepted or integrated.**
No backlog task, broad requirement, test case or milestone is marked complete.
The owner accepted the original prototype review, then requested Turkish UI,
dark mode and a persistent Turkish-interface rule. The current revised diff
awaits renewed human review; that acceptance did not authorize committing or merging.

## Authorization and baseline

- TASK-004A1 — Prototype account creation and balances; Must; WBS 2.1.1.1;
  M-009 final implementation leaf; planned budget 4 h including tests/notes.
  This is the approved estimate, not an actual-effort claim.
- Owner approved preparation and explicitly authorized this implementation,
  feature branch/worktree, focused/full tests, documentation and this report.
- Baseline: `d27f06b8988d7dda7ab35f5d45366b6ffc2e56e6`, accepted local main.
  Its merge record confirms owner acceptance and integration of TASK-025A
  source `86cf366`; ancestry and relevant source-tree equality were verified.
  TASK-022A and TASK-001 remain accepted at `18c1066` and `5052b5b`.
- Branch: `feat/TASK-004A1-account-balances`.
- Worktree: `/tmp/finance-tracker-task-004a1`.
- Main remains unchanged and clean at the baseline. Recorded `origin/main`
  is two commits behind; remote freshness is unverified. No fetch or push.
- All changes are unstaged. Other worktrees and stale registrations are untouched.

The owner explicitly approved synthetic USD/scale 2, integer minor units,
signed-64-bit per-record limits, exact parsing without rounding, synthetic UTC
with an injectable clock, session-derived ownership, atomic creation and minimal
idempotency. These conventions do not resolve OQ-002/OQ-007 for release.
The subsequent Turkish UI/theme request authorizes the interface revision, and
the explicit request to record the language in the rules authorizes the narrow
AGENTS.md edit. No new backlog ID applies to that owner-requested UI/governance
revision; no task or planning budget was invented or changed.

## Implementation and file scope

New files:

- `src/finance_tracker/django_app/account_rules.py`: framework-independent exact
  parsing/formatting, USD validation and account-name normalization.
- `src/finance_tracker/django_app/models.py`: UserSettings, Account and
  BalanceObservation prototype subset.
- `src/finance_tracker/django_app/migrations/__init__.py` and `0001_initial.py`:
  additive schema depending on the established custom user model.
- `src/finance_tracker/django_app/services.py`: authenticated ordinary-owner
  guard, atomic creation/replay and owner-scoped cards/subtotal query.
- `src/finance_tracker/django_app/forms.py` and
  `templates/prototype/account_form.html`: explicit currency selection, labels,
  help/errors, preserved input and hidden submission identity.
- `tests/django/test_accounts.py`: 58 focused scenarios including parameterized
  exactness/input checks, isolation, HTTP protections, rollback and restart.
- This review report.

Modified files:

- `views.py`, `urls.py`: protected creation and saved-record presentation.
- Prototype `base.html`, `accounts.html`, `account_card.html`, `dashboard.html`
  and `static/prototype/style.css`: create action, saved cards, exact totals,
  success/empty states and separated illustrative preview.
- `tests/django/conftest.py`: force child imports to this checkout and assert
  source identity, including when reusing dependencies from another environment.
- `test_shell.py`, `test_authentication.py`: update obsolete assertions that
  account creation is unavailable; preserve other accepted scenarios.
- Root README and setup instructions: actual task state and synthetic workflow.

The interface revision additionally changes `identity/forms.py`, `settings.py`,
the login template and `test_prototype_startup.py`; adds `static/prototype/theme.js`,
the shared error template, CSRF error template and 400/403/404/500 templates; and
extends `pyproject.toml` package data to include JavaScript. AGENTS.md records the
owner-approved Turkish interface rule. There are **34 intended changed/new files**.
Existing identity model/migrations, provisioning, loopback launcher, dependency
versions/lock, TASK-001 application/tests and protected product/planning documents
are unchanged. Language/form/settings changes preserve authentication behavior.

## Behavior and integrity

Account creation accepts name, explicitly selected USD and exact opening text.
Names are NFKC-normalized, trimmed and casefolded for owner-local uniqueness;
the visible name is limited to 100 characters. Controls/invisible characters fail;
template escaping protects display. Two owners may use the same name.

Amounts accept ASCII decimal digits with up to two fractional places. Zero is
valid; negatives, NaN/infinity, exponent/comma notation, excess precision,
non-text financial inputs and values above `92233720368547758.07` USD fail.
Parsing uses Decimal in an explicit local context; storage is integer minor
units. Display uses integer division/remainder and totals use Python integers,
including totals larger than a single record's signed-64-bit limit. No float
enters financial parsing, aggregation or display.

UserSettings stores the explicitly selected USD/scale 2 metadata. Database checks
restrict this prototype to that convention. Account has an authenticated owner,
savings kind, owner-local name constraint and owner/creation-key uniqueness.
BalanceObservation inherits ownership through its mandatory Account; its cash
amount is bounded and the opening-only slice permits one observation per account.
Later dated-update work can extend this subset with a reviewed migration.

The minimal creation guard is stored on Account as a UUID and canonical-request
SHA-256 fingerprint, rather than adding the full future UPDATE_BATCH subsystem.
Account, observation and first-use currency metadata commit together. Identical
owner/key/payload retries return the original account; changed-payload reuse
fails. Equivalent decimal spelling has the same intent. A new key/name can create
a legitimate equal-valued account. Failure rolls back records and key consumption;
SQLite busy errors preserve the form for retry. This is not release concurrency
or revision acceptance.

Owner context comes only from the authenticated session. User-supplied owner or
account identifiers cannot redirect ownership or reads. All financial pages and
services reject privileged staff/superuser identities; no financial models are
registered with Django admin and no admin route is exposed. Full Admin/User role
policy remains later work. Existing CSRF/session/no-store protections are retained.

The opening clock must return an aware datetime; the service converts it to UTC
and records the UTC date and timestamp. Openings are starting positions, never
contributions. There is no movement/transaction model or write. Saved records are
clearly labeled synthetic. The illustrative card remains collapsed, explicitly
unsaved and excluded from totals. Missing opening data yields an incomplete
subtotal instead of an assumed zero. Unsupported currency metadata is not summed.

## Owner-requested Turkish interface and theme revision

User-facing pages, navigation, labels, help, empty/success/error states and login
messages are Turkish. Django uses `LANGUAGE_CODE="tr"` for framework validation;
HTML declares `lang="tr"`. Generic login failures remain non-disclosing and
passwords are never redisplayed. Turkish 400/403/404/500 and CSRF error templates
retain status codes and do not reflect exception reasons or submitted values.
The project name remains Finance Tracker. Numeric input/storage/display rules
are unchanged; Turkish form guidance explicitly explains the decimal point.

The accessible `Koyu tema` button is available before and after sign-in. First
load follows `prefers-color-scheme`; a valid explicit light/dark choice overrides
the system and is stored in localStorage under `finance-tracker-theme`. It holds
only a display preference, never identity, session or financial data. The external
script applies the theme before the stylesheet paints, supports keyboard
activation and follows later system changes until a manual preference exists.
Storage errors are caught; current-page switching still works. CSS provides the
system-theme fallback without JavaScript, with the manual button hidden.

No dependency version, database schema, financial convention or record changed
for this revision. The owner explicitly requested the AGENTS.md rule covering
Turkish user-facing pages/navigation/forms/help/errors/notifications/states,
Django messages and HTML language while preserving the Finance Tracker name.
Source identifiers and project documentation do not require translation under
that rule.

## Acceptance coverage

| Scope | Evidence and limits |
|---|---|
| FR-003/037; US-002/026; UC-002/023; P1-03/04 | Authenticated form creation, owner-local name uniqueness, saved cards, exact initial observations and totals verified. Rename/archive/holdings remain later scope. |
| NFR-012 subset; BR-011/016; TC-047/059 subsets | Zero, cents, nonfinite/precision/overflow boundaries, integer SQLite storage, exact display and no contributions/double-counting verified. Full numeric/revision policy remains later. |
| FR-036 and NFR-008 subsets; BR-024; TC-058 subset | Two owners, forged identifiers, same names/keys across owners, anonymous and privileged denial verified for current pages/service. No full release-privacy claim. |
| FR-032; NFR-005 subset; P1-05; TC-040 subset | Atomic failure rollback, durable replay, fresh-process reads and two real server starts preserve saved values/session. No backup/recovery or PostgreSQL acceptance. |
| BR-023 outcome; minimal prototype guard | Identical replay, conflicting payload, distinct equal-valued accounts and retry after rollback/busy error verified. No general update/concurrency subsystem. |
| NFR-004; P1-03/04/06; TC-039/053 subsets | Empty/error/success states, explicit currency, retained input, accessible markup, desktop/narrow browser flow verified. Owner demonstration/acceptance remains pending. |
| Accepted-task preservation | Existing 103 scenarios pass within the final combined suite; TASK-001 source/tests and identity foundations remain byte-identical. Historical test evidence is separate. |

## Original prototype verification — 2026-11-05

Environment: Linux x86_64, Python 3.14.8, Django 5.2.19, pytest 9.2.0,
Streamlit 1.66.1. No packages were installed or changed. Checks reused the existing
`/tmp/finance-tracker-task-025a/.venv/bin/python` dependencies with
`PYTHONPATH=/tmp/finance-tracker-task-004a1/src`; actual task imports and every
installed lock pin were verified. No personal database or live destination was used.

In the table, `PY` means that interpreter with the explicit task PYTHONPATH.

| Command / check | Actual result |
|---|---|
| Authorized `git worktree add -b feat/TASK-004A1-account-balances /tmp/finance-tracker-task-004a1 d27f06b8988d7dda7ab35f5d45366b6ffc2e56e6` | Sandbox metadata write failed; approved rerun created exactly the authorized branch/worktree. |
| Isolated `makemigrations django_app` and `check` | Generated additive `0001_initial.py`; system check clean. No existing identity migration changed. |
| `PY -m pytest -q tests/django/test_accounts.py -k 'not application_restart'` | 56 passed, 1 deselected in 18.34 s, before the additional upgrade-preservation scenario. |
| Initial sandbox `PY -m pytest -q` | 157 passed; 3 loopback startup/restart checks blocked by socket permissions. |
| Permitted `PY -m pytest -q` | 160 passed in 40.22 s before the added upgrade-preservation scenario. |
| `PY -m pytest -q tests/django/test_accounts.py -k additive` | Added upgrade test passed: 1 passed, 57 deselected in 0.68 s; existing identity hash/session preserved through additive migration. |
| Original prototype final permitted `PY -m pytest -q` | **161 passed in 41.32 s:** 58 unchanged TASK-001 scenarios, 45 prior Django scenarios and 58 new account scenarios. Includes actual loopback startup and saved-data server restart checks. |
| `PY -m pip check` | No broken requirements. Pip emitted a non-fatal cache-permission warning; no installation occurred. |
| `PY -B /tmp/task004a1_validate.py` | Task import and all lock pins verified; Django check, fresh isolated migrations, `makemigrations --check --dry-run`, `migrate --check`, SQLite foreign keys, private modes and isolated legacy-sentinel preservation passed. |
| `/tmp/task004a1_browser_check.py` with permitted browser/socket access | Firefox exercised login, empty state, explicit USD, invalid/valid openings, input retention, saved cards, exact totals and logout. Nine screenshots; no horizontal overflow detected. |
| Browser-check attempts | Initial sandbox blocked local sockets. First permitted attempt exposed a checker wait bug: a login URL's `next=/accounts/` matched its suffix condition. Corrected the temporary checker to wait for the exact destination URL; rerun passed. No application change was needed. |
| `PY -B /tmp/task004a1_review_checks.py` | Complete intended-file manifest, unrelated-file preservation, local documentation links, whitespace, credential-signature/data exclusions, clean main and unstaged diff checked; complete review patch generated. |

Browser artifacts: `/tmp/task004a1-browser-pntwgkoc/`. Actual viewports were
1280x914 and 500x914 CSS pixels. All nine screenshots were visually inspected.
Form content uses normal vertical scrolling; no 390-pixel coverage or formal
accessibility audit is claimed. Temporary browser/app processes were stopped.
This is developer verification, not the owner's TC-039/053 acceptance.

The complete unstaged patch, including new files, is
`/tmp/task004a1-review.patch`. Protected requirements, architecture, decisions,
backlog, RTM, historical review reports and the TASK-001 setup section are unchanged.

## Current Turkish/theme revision verification — 2026-11-05

The same verified Python/dependency environment and explicit task source override
were used. Existing visible-text assertions were translated while financial,
ownership and authentication checks remain. Startup coverage now fetches the theme
JavaScript as well as CSS; navigation checks verify the Turkish HTML and theme control.

| Command / check | Actual result |
|---|---|
| `PY -m pytest -q tests/django -k 'not actual_loopback and not application_restart'` | 101 passed, 2 deselected in 40.88 s during the interface revision. |
| Final permitted `PY -m pytest -q` | **161 passed in 41.23 s**, including all existing financial/ownership/authentication scenarios and actual loopback startup/restart. |
| `PY -B /tmp/task004a1_validate.py` | Exact source/pins, system check, fresh isolated migration, no model drift, applied migrations, foreign keys and private file modes passed. No new migration required for language/theme. |
| `PY -m pip check` | No broken requirements; non-fatal cache-permission warning. No packages installed or changed. |
| `PY -m pip wheel --no-deps --no-build-isolation --wheel-dir /tmp/task004a1-tr-wheel .` | Built local wheel successfully, without dependency installation. |
| `PY -B /tmp/task004a1_tr_validate.py` | Repeated isolated system/migration checks; Turkish framework validation and 400/403/404/500/CSRF responses passed without reflecting private reasons. Built wheel contains byte-identical theme JS/CSS and Turkish/error templates. |
| Permitted `/tmp/task004a1_tr_browser_check.py` | Firefox verified initial system preference, keyboard toggle, light/dark colors, stored choice across reload/navigation, restricted-storage switching, Turkish login/error/form flow, exact cards/totals, logout and missing-page response. 14 screenshots, no horizontal overflow. |
| `PY -B /tmp/task004a1_review_checks.py` | Current 34-file manifest, preservation, local links, whitespace, credential/data exclusions and clean main checked; complete patch/manifest refreshed. |

Current screenshots: `/tmp/task004a1-tr-browser-ir42xiae/`, at actual 1280x914
and 500x914 CSS pixels. Both themes and desktop/narrow screenshots were visually
inspected. No 390-pixel coverage or formal accessibility audit is claimed.
Browser/app checks used a new disposable synthetic database and stopped their
temporary processes. The owner's running prototype database was not accessed.

## Setup and owner review

Follow [Django setup](../SETUP.md) from this worktree. Create a task-local Python
3.14 environment and install the existing lock using the documented instructions,
or reuse the verified dependency environment with the source override below:

```bash
cd /tmp/finance-tracker-task-004a1
export PYTHONPATH="$PWD/src"
TASK_PYTHON=/tmp/finance-tracker-task-025a/.venv/bin/python
umask 077
install -d -m 700 data
export FINANCE_TRACKER_PROTOTYPE_DATABASE_PATH="$PWD/data/prototype.sqlite3"
export FINANCE_TRACKER_DJANGO_SECRET_KEY="$("$TASK_PYTHON" -c 'import secrets; print(secrets.token_urlsafe(64))')"
export DJANGO_SETTINGS_MODULE=finance_tracker.django_app.settings
"$TASK_PYTHON" -m django check
"$TASK_PYTHON" -m django migrate --noinput
"$TASK_PYTHON" -m django provision_prototype_user
"$TASK_PYTHON" -m finance_tracker.django_app
```

Choose a synthetic development password at the hidden prompts; there is no default.
This implementation run used only isolated validation/test/browser databases and
did not create a worktree `data/prototype.sqlite3`. The commands above explicitly
prepare it for review. Skip provisioning on subsequent starts. Keep the signing
key and database path unchanged for the restart demonstration; never point at
TASK-001's database. Fresh-host installation was not tested in this task.

Owner review should follow visible Turkish guidance: sign in, inspect empty pages, create
a synthetic USD savings account, try an invalid amount, find the saved card and
Dashboard total, refresh, stop/start the server and sign out. Repeat at a narrow
viewport. Review the complete diff and acceptance evidence. P1-06, TC-039/053 and
M-009 remain awaiting owner demonstration and acceptance; this report does not
mark them complete.
Also toggle **Koyu tema** on login and authenticated pages, refresh/navigate and
confirm the preference remains. Restart an already running development server
to load the language/settings revision, then refresh the browser. No migration or
re-provisioning is needed for these UI changes. The current revised diff requires
renewed owner review before any separately authorized Git operation.

Limits: local synthetic USD cash openings only; no edits/archive, transactions,
transfers, trading, investments, goals, profiles, reports or external integrations.
No PostgreSQL, full authentication/authorization/Admin MFA/privacy, recovery,
Pi/CasaOS/Compose/Tunnel, CI/deployment or production suitability is accepted here.
All release gates still precede real users/sensitive data. No implementation
blocker is known within this approved prototype slice.

**Stopped at the Human Review Gate.** No staging, commit, push, PR, merge,
branch/worktree deletion, deployment or next-task work was performed.
