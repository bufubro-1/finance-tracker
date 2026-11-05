# TASK-025A — Development authentication review

Status: **Implemented for human review; uncommitted and not accepted or integrated.**
No backlog task, broad requirement, test case or milestone is marked complete.

## Authorization, baseline and scope

- Task: TASK-025A — Prototype standard Django authentication; Must; WBS 1.7.1;
  M-009 second leaf; approved budget 4 h including tests/notes, not an actual-time claim.
- Owner approved the preparation report and explicitly authorized TASK-025A implementation,
  isolated branch/worktree creation, focused tests and setup/review documentation.
- Baseline: `18c1066f3fbb7546bdc448a43a54125a5a937db3`, verified local main.
- Branch: `feat/TASK-025A-development-auth`.
- Worktree: `/tmp/finance-tracker-task-025a`; review its current uncommitted diff,
  including new files. Nothing is staged.
- TASK-022A is accepted/integrated: `18c1066` records owner acceptance of `b6393f4`;
  ancestry and exact tree equality were verified during preparation. TASK-001 remains
  accepted at `5052b5b`. Earlier review-pending document wording is historical.
- Local main is unchanged. Recorded `origin/main` matches that baseline, but remote
  freshness is unverified; no fetch, push, commit, PR or merge was performed.
- Other branches/worktrees and stale worktree registrations were left untouched.

The change uses the existing custom email user model and Django password/session/CSRF
foundations. Dashboard and Accounts retain their synthetic cards/navigation behind
login. There is no account creation or financial persistence. Public signup,
invitations, recovery, Admin MFA, PostgreSQL, infrastructure and integrations are excluded.

## Implementation and changed files

- Identity: new `identity/forms.py` normalizes the login email through the existing
  manager; new `identity/management/commands/provision_prototype_user.py` and package
  initializers add explicit interactive provisioning. The model and migrations are unchanged.
- Routing/settings/views: standard `LoginView`/`LogoutView`, named login/dashboard
  destinations, auth template context, `login_required` and private-page cache prevention.
- UI: new login template; base template includes authenticated navigation and POST
  sign-out; Accounts/footer guidance reflects this task; CSS adds form/error/focus styles.
- Tests: new authentication/provisioning modules; isolated migration fixture; updated
  shell/startup checks distinguish anonymous login redirects from authenticated cards.
- Documentation: root README, setup instructions and this report. Protected requirements,
  Charter, decisions, architecture, backlog, RTM and historical review reports are unchanged.

Provisioning is restricted to the exact prototype settings module and SQLite, even
though prototype `DEBUG` is false. It creates only `sample@example.invalid`, active
with staff/superuser flags false. Password entry is hidden and confirmed; blank,
mismatched, canceled or insecure-terminal input fails without creating a user.
There is no password CLI argument or default password. Existing identities are
never changed. The command requires explicit migrations and does not create a
missing database or run migrations itself.

Login uses Django's normal password verification, session rotation and CSRF rotation.
Wrong password, unknown email and inactive identity use the same generic credential
failure. The email remains visible after an error; the password is never redisplayed.
Login accepts Django-validated same-host destinations and otherwise returns to Dashboard.
Logout accepts POST with CSRF, invalidates the server session and always returns to
login, ignoring destination overrides. Protected pages use no-store cache headers.

## Acceptance coverage

| Requirement / acceptance | Evidence and limits |
|---|---|
| Backlog acceptance; FR-034, P1-02; US-023/UC-020; CMP-011 | Synthetic provisioning, password hash, actual form login/logout, protected-page redirects and CSRF scenarios pass. |
| NFR-013 prototype foundations; TC-055 subset | Generic credential failures, inactive-user rejection, session-key rotation, cross-process persistence, logout cookie replay rejection, cookie attributes and CSRF/origin checks pass. No release-security acceptance. |
| Safe redirects; TC-053/055 subsets | Requested local path/query and same-host URL work; external, deceptive-host, scheme-relative, backslash and unsafe-scheme inputs fall back safely; logout destination is fixed. |
| NFR-001/002; BR-024 scoped boundary | Loopback listener, restrictive hosts, synthetic-only banner, private SQLite, nonprivileged identity and no exposed admin/registration/reset routes verified. No full financial-ownership claim. |
| P1-01/03/06 subsets; NFR-004; TC-039/053 subsets | Authenticated navigation, active indication, sample card/empty state/escaping and login labels/errors tested; desktop/narrow browser checks below. |
| TASK-001 regression | Original runtime/configuration/tests unchanged; all 58 original scenarios pass in the new combined run. Historical acceptance results remain separate evidence. |

TC-053 and M-009 remain incomplete until TASK-004A1 adds and verifies owned account
creation, validation, saved balances and the full owner demonstration. TC-055 and
NFR-013 still require release membership/recovery/revocation/throttling/MFA work.

## Actual verification — 2026-11-05

Environment: Linux x86_64, Python 3.14.8, task-local venv, existing pinned Django
5.2.19/pytest 9.2.0/Streamlit 1.66.1. Test databases and identities are synthetic.
Child interpreters isolate Django settings from TASK-001 tests. External socket
connections are rejected in the authentication/presentation tests.

| Command / check | Actual result |
|---|---|
| Authorized worktree creation | Sandbox Git metadata was read-only; approved rerun created the task branch/worktree from the exact baseline. |
| `python3.14 -m venv .venv` | Created isolated environment. |
| `.venv/bin/python -m pip install -r requirements.lock` | Sandbox DNS failed; approved network-enabled rerun installed existing pins. No dependency files changed. |
| `.venv/bin/python -m pip install --no-build-isolation --no-deps -e '.[dev]'` | Installed editable task package successfully. |
| `.venv/bin/python -m pytest -q tests/django -k 'not actual_loopback'` | 44 passed, 1 deselected in 19.31 s. |
| Initial sandbox `.venv/bin/python -m pytest -q` | 101 passed; the two actual socket checks were blocked by sandbox permissions. |
| First permitted full run | 102 passed; a new startup assertion incorrectly assumed no SQLite file. Django's unchanged runserver migration probe opens an empty file. Corrected the assertion to require private permissions and no tables; no launcher change. |
| `.venv/bin/python -m pytest -q tests/django`, with approved socket access | **45 passed in 20.41 s.** |
| Final `.venv/bin/python -m pytest -q`, with approved socket access | **103 passed in 20.56 s:** 58 unchanged TASK-001 tests and 45 Django scenarios. |
| `.venv/bin/python -m pip check` | No broken requirements found. |
| `.venv/bin/python /tmp/task025a_validate.py` | Task-source import verified; `django check`, explicit `migrate --noinput --verbosity 0`, `makemigrations --check --dry-run` and `migrate --check` passed. Task data directory 0700/database 0600. |
| `.venv/bin/python /tmp/task025a_browser_check.py`, with approved browser/socket access | Firefox exercised anonymous redirect, invalid credentials, login, navigation, logout and rejection after logout. Seven screenshots captured; no horizontal overflow detected. Developer visually inspected all seven. |
| Additional `/tmp/task025a_narrow_check.py` attempt | Firefox BiDi viewport override returned unsupported operation. No application change resulted. Actual verified narrow viewport is 500 CSS pixels; 390-pixel coverage is not claimed. |
| `.venv/bin/python -B /tmp/task025a_review_checks.py` | Passed: exact 19-file scope, 46 other tracked files preserved, all installed dependency pins match, 12 local documentation links resolve, whitespace/credential-signature/data-exclusion checks pass, legacy setup preserved, nothing staged and main clean. |

Browser artifacts are disposable local files at `/tmp/task025a-browser-q5ph5d5d/`.
Captured viewports were 1280x814 and 500x914; the requested 390-pixel window was
clamped by Firefox. Login, errors, authenticated navigation, cards and sign-out
were readable. This is developer browser verification, not owner acceptance or
a formal accessibility audit. Temporary browser/app processes were stopped.

The complete review patch, including new files, is `/tmp/task025a-review.patch`.
The checker regenerated it after the final documentation update. Credential
signature checks supplement the manual complete-diff review; no secrets, generated
databases, virtual environments or unrelated changes are included.

## Launch and review

The worktree's `data/prototype.sqlite3` contains only the initial framework/custom
identity schema created by the explicit validation migrations. No user has been
provisioned in this database. It is private, disposable and gitignored. Automated
tests/browser checks used separate temporary databases; the TASK-001 database was
never accessed or modified.

From the task worktree, activate `.venv` and follow the [Django setup commands](../SETUP.md):
set the prototype database path and a private generated signing key, select prototype
settings, run the migrations, then run `python -m django provision_prototype_user`.
Choose your own synthetic development password at the hidden prompts. Start
`python -m finance_tracker.django_app` and open `http://127.0.0.1:8000`.
Keep the same signing key to demonstrate session persistence across restarts.

Owner review should verify sign-in with the provisioned identity, generic invalid
credentials, Dashboard/Accounts navigation, sample-card readability and sign-out.
The complete local diff and acceptance evidence require human review before any
commit or integration. No implementation blocker is known.

Remaining limits: all data must stay synthetic and loopback-only. Local HTTP does
not use Secure-only cookies; default Django session expiry remains unchanged.
Full release authentication, object authorization, Admin MFA, privacy, PostgreSQL
integrity/recovery, intended-host compatibility and deployment remain mandatory
later gates. No task status or release-suitability claim follows from these checks.

**Stopped at the Human Review Gate.** Commit, push, PR, merge, branch/worktree
deletion, deployment and any next task require separate owner authorization.
