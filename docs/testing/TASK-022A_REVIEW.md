# TASK-022A — Implementation review

Status: Implemented for human review; not accepted, committed or integrated.
No backlog task, requirement, test case or milestone is marked complete.

## Revision and scope

- Task: **TASK-022A — Prototype Django shell and dashboard**, Must, WBS 1.4.1,
  M-009 first leaf; approved estimate 8 h, not a measured actual-effort claim.
- Baseline: owner-approved `0fdf690be7e971ab3063147fbf6001adda6e6ce2`.
- Branch: `feat/TASK-022A-django-shell`.
- Worktree: `/tmp/finance-tracker-task-022a`; reviewed source is its uncommitted diff.
- Dependency: TASK-001 accepted/integrated at `5052b5b`; no task-local decision gate.
- Authorization: owner's instruction to implement the prepared TASK-022A plan.
  No commit, push, PR, merge, deployment or later task is authorized.
- Remote freshness remains unverified; no fetch. Main remains at the approved baseline.

The new Django package is separate from the existing Streamlit launcher. It
renders Dashboard/Accounts, active navigation, a synthetic banner, an empty
state and an explicitly unsaved example card. No ORM financial query, calculation,
form, account write or external client exists. Standard middleware and an initial
custom email-user migration prepare TASK-025A without implementing its workflows.
Email normalization and case-insensitive uniqueness are foundation behavior;
membership verification, lifecycle/recovery and authorization remain later gates.

The launcher uses Python 3.14.x, explicitly selects prototype settings and binds
127.0.0.1. Its only listener option is the port. DEBUG is false; development
static-file serving is explicitly enabled. A separate private SQLite path is
validated without changing its permissions or contents; migrations are explicit.
The legacy configured database path cannot be reused as the prototype path.
No Django admin route is exposed; the user manager rejects createsuperuser.
Application Admin is not a Django superuser. Full Admin policy remains TASK-026.

## Changed files

- `pyproject.toml`, `requirements.lock`: add Django 5.2.19, asgiref 3.13.0 and
  sqlparse 0.6.1; retain original pins and package HTML/CSS assets.
- `src/finance_tracker/django_app/`: isolated launcher/settings/routes/views,
  identity model and initial migration, four templates and one stylesheet.
- `tests/django/`: isolated child-interpreter fixtures and 16 focused scenarios.
- `README.md`, `docs/SETUP.md`, this report: current task status, separate startup
  instructions, boundaries and actual evidence. Requirements/design are unchanged.

## Acceptance coverage

| Acceptance / trace | Evidence and limit |
|---|---|
| Local Django package; FR-001, P1-01 | Actual server startup, HTTP response, listener verified in Linux socket table. |
| User-model foundation | Initial migration on temporary SQLite; custom identity, password hashing, case-insensitive uniqueness and subsequent-process read verified. No login UI or identity provisioning command. |
| Navigation/layout/cards; NFR-004, P1-03 subset | Dashboard/Accounts links, active indication, readable name/currency/value, empty state and escaping verified. Card is a fixed synthetic illustration, not an account. |
| Synthetic banner and loopback; NFR-001 | Banner on both routes, restrictive hosts, fixed listener and rejected bind arguments verified. |
| Integration independence; FR-032 shell subset | Pages render without a database or network; inherited integration flags do not initialize providers. No financial durability/atomicity claim. |
| Startup/navigation checks; P1-06 subset | Automated tests and developer screenshot inspection below. Owner acceptance remains pending. |

TC-001/038/039/053 have only their applicable shell scenarios exercised here.
TC-053 and M-009 remain incomplete until TASK-025A and TASK-004A1 provide and
verify sign-in, protected pages, create/form validation, actual saved balances,
restart and logout, followed by the full owner demonstration.

## Actual verification — 2026-11-05

Environment: Linux x86_64, Python 3.14.8, private task-local venv, synthetic data
and temporary SQLite only. No live integration, private destination or real identity.

| Command / check | Result |
|---|---|
| `python3.14 -m venv .venv` | Created isolated task environment. |
| `.venv/bin/python -m pip install -r requirements.lock 'Django==5.2.19'` | Sandbox DNS initially failed; approved network-enabled rerun installed successfully, preserving all existing pins. |
| `.venv/bin/python -m pip install --no-build-isolation --no-deps -e '.[dev]'` | Editable package installed successfully. |
| Initial pytest collection | New startup test filename collided with existing test module; renamed the new file without changing TASK-001 tests. |
| `.venv/bin/python -m pytest -q` in sandbox | 72 passed; two actual-listener checks blocked by sandbox socket permissions. |
| Same pytest command with approved local socket access | **74 passed in 2.27 s**: unchanged 58 TASK-001 tests plus 16 new Django scenarios. This is a new run, distinct from historical integration evidence. |
| `.venv/bin/python -m pip check` | No broken requirements found. |
| Django checks inside isolated migration test | System check clean; initial migrations apply; `makemigrations --check --dry-run` detects no changes; identity survives a child-process restart. |
| `.venv/bin/python -m pip wheel --no-build-isolation --no-deps --no-index --wheel-dir /tmp/finance-tracker-task-022a-wheel .` | Built wheel successfully. Installed-wheel content verification recorded below. |
| `python3.14 /tmp/task022a_browser_check.py` with approved browser/socket access | Headless Firefox captured Dashboard and Accounts at 1280×900, Accounts at 390×1000. Developer inspected all three images: readable cards/banner/navigation and no visible horizontal clipping. |

Screenshots and browser logs are disposable local artifacts under
`/tmp/task022a-browser-6higmzvy/`, outside the repository. This was a developer
visual inspection, not owner acceptance or an accessibility audit.

Final review command: `.venv/bin/python -I /tmp/task022a_review_checks.py` — passed.
It verified byte-for-byte preservation of the legacy runtime, tests, configuration
and protected documents; every original dependency pin; all installed lock versions;
local links in changed Markdown; whitespace; and an empty staging area. The wheel
was installed with `pip install --no-index --no-deps --target /tmp/task022a-installed-wheel`.
From that installed package, templates rendered, CSS was found, system checks
passed, initial migrations applied and no migration drift was detected.

All 22 changed/new text files passed trailing-whitespace, credential-signature
and database/secret-file exclusion checks. The complete tracked/new-file review
patch is `/tmp/task022a-review.patch`; it includes this report. No files are staged.

## Remaining limits and human gate

No current TASK-022A implementation blocker is known. All data must remain
synthetic and access loopback-only. There is no production deployment, PostgreSQL,
financial schema, account persistence or authenticated financial workspace.
Real users and sensitive data remain prohibited until the full M-007 gate.

OQ-002/007 financial policy/replay, OQ-010 identity/MFA lifecycle, Pi/ARM64 and
deployment compatibility, PostgreSQL integrity/concurrency, security, recovery
and release verification remain at their assigned later tasks. No threshold or
proposed policy is approved by this work.

Human review must assess the complete new-file and tracked-file diff, the scoped
acceptance evidence and these limitations. Protected requirements, Charter and
architecture decisions were not edited. The task remains uncommitted and awaits
owner review; do not advance automatically to TASK-025A.
