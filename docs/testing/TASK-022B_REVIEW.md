# TASK-022B — Django configuration and boundaries review

Current integration scope: the owner accepted TASK-022B and explicitly authorized
one implementation commit and local merge in "TASK-022B — Acceptance, Commit
and Merge". M-009 closure documentation is excluded from this task commit and
preserved separately in the task worktree. The original review-time snapshot
below records the earlier combined review and its actual results; its references
to closure files and pending acceptance are historical. The implementation and
integration commit records supply subsequent acceptance and verification.

Status: **Implemented for human review; uncommitted, not accepted or integrated.**
M-009 closure documentation was explicitly reviewed/approved separately during
this task; its uncommitted changes are included here. No later task, broad
requirement or production release gate is marked complete.

## Authorization and baseline

- Task: TASK-022B — Complete Django configuration and boundaries; executable
  Must leaf; WBS 1.4.2; M-001 foundation; approved 8 h including tests/notes,
  not measured actual effort.
- Owner approved the preparation report and explicitly authorized implementation,
  a dedicated branch/worktree, focused/full synthetic verification and setup
  documentation in "M-009 Closure and TASK-022B Implementation Authorization".
- Owner then approved the exact proposed M-009 closure patch, prepared outside the
  repository, before any protected planning edits: "Approve closure patch and
  proceed". Closure maintenance has no new backlog task ID.
- Baseline: accepted local main
  `6c937a6ff71ab5285c32ee6281b5e9d8014c9313`.
- Branch: `feat/TASK-022B-django-configuration`.
- Worktree: `/tmp/finance-tracker-task-022b`.
- Main remains at the accepted baseline. Recorded `origin/main` matches it;
  live remote freshness is unverified. No fetch, push or merge occurred.
- Existing worktrees, stale registrations and unrelated branches were preserved.
  No changes are staged or committed.

TASK-004A1 and its TASK-022A/025A predecessors have owner acceptance and local
integration evidence. TASK-022B has no blocking recorded decision gate.
DEC-017/020–025 remain controlling. OQ-002/007 financial policies, OQ-010 release
identity/MFA, OQ-004/008 intended-host compatibility and all later gates remain
unresolved at their assigned tasks.

## Implementation and scope

- `settings.py` retains the existing prototype settings entrypoint and private
  synthetic SQLite. Its accepted SQLite validator moves verbatim into
  `configuration.py`; the launcher and provisioning command are unchanged.
- `settings_common.py` extracts existing framework/authentication/template/
  Turkish-language defaults and defines private console logging.
- `settings_release.py` selects explicit release configuration, secure cookies
  and HTTPS redirection. Forwarded HTTPS trust is opt-in; forwarded-host trust
  stays disabled. HSTS/subdomain/preload policy awaits deployment review.
- `configuration.py` validates required release inputs and private environment/
  secret-file inputs with value-free errors. Secret files require current-user
  ownership, private readable regular files, no final symlink and bounded UTF-8
  content. Conflicting value/file inputs fail. No secret/key fallback is used.
- Release hosts are exact, and trusted origins are matching exact HTTPS origins.
  A dedicated absolute static-assets output directory is configured without
  creating/serving it. PostgreSQL name/user/password/host/port form an explicit
  backend dictionary; importing it loads no driver and opens no connection.
- Django/application logs contain only fixed level/status metadata: no request
  path/body, message interpolation, environment, SQL or exception traceback.
  This deliberately reduces diagnostic detail. Future server/proxy/host logs
  remain separately governed deployment work.
- `test_release_configuration.py` adds 60 focused scenarios for settings
  separation, failure redaction, secret-file controls, HTTPS/CSRF/cookies,
  explicit proxy trust, actual Django logging initialization and independent
  exact-input functions.
- Setup documents the inputs, private-file rules and future release limitations.
  Approved closure changes update README/index, Backlog, WBS, Schedule, RTM and
  Test Plan and add separate `docs/testing/M-009_CLOSURE.md` evidence.

No accepted UI/template/static asset, financial model, migration, calculation,
service, account ownership path, identity model, provisioning command or launcher
was changed. No dependency pins, TASK-001 code/configuration/tests or TASK-001
database was changed. All validation storage was isolated and synthetic.

TASK-002 remains responsible for full wealth/date/attribution rules; TASK-026 for
release roles/authorization/private health; TASK-003 for PostgreSQL schema,
ownership constraints, replay/version/concurrency integrity. TASK-023/024/020
retain CI, intended-host compatibility and deployment. This task implements none
of those later deliverables.

## Acceptance and traceability

| Scope | Evidence and limitation |
|---|---|
| Separate development/release settings; FR-001, US-001/UC-001, TC-001 subset | Required inputs, independence from prototype variables, PostgreSQL-only release dictionary and preserved development launcher/provisioning checked. Release operational startup is blocked by the absent driver. |
| Private secrets/redacted errors; NFR-002, TC-038 subset | Invalid/missing/conflicting inputs, bad private files, foreign ownership, output sentinels and actual Django log handlers tested. No mounted container/host or future server logging acceptance. |
| Service boundaries; NFR-006, TC-041 subset | Existing exact input functions run without framework/ORM/provider imports, credentials or network; service/models/calculations remain byte-identical. Full TASK-002 financial functions are not implemented. |
| Secure release configuration; scoped BR-024/NFR-001/013 safeguards | Exact hosts/HTTPS origins, redirect, secure cookies, rejected CSRF/hosts and explicit forwarded-header trust tested using isolated development SQLite. No release identity/MFA/topology/authorization acceptance. |
| Retained working prototype; TC-039/053 regression | Existing tests cover Turkish navigation/theme assets, synthetic provisioning/login/logout, exact openings/cards/totals, isolation, rollback/replay and real loopback startup/restart. M-009 owner's prior acceptance is retained; no new TASK-022B owner browser acceptance is claimed. |

## Actual verification

Environment: Linux x86_64 / Python 3.14.8; existing
`/tmp/finance-tracker-task-025a/.venv/bin/python` dependencies reused with
`PYTHONPATH=/tmp/finance-tracker-task-022b/src`. No dependency installation.
Actual imported source and every lock pin were asserted.

| Command / check | Actual result |
|---|---|
| Authorized `git worktree add -b feat/TASK-022B-django-configuration /tmp/finance-tracker-task-022b 6c937a6ff71ab5285c32ee6281b5e9d8014c9313` | Initial sandbox attempt blocked Git metadata writes; approved rerun created the exact authorized branch/worktree. |
| `git apply --check` then `git apply /tmp/finance-tracker-m009-closure-proposed.patch` | Approved closure patch applied only in task worktree. Reverse-apply check later verified all approved closure hunks remain present. |
| `PY -m pytest -q tests/django/test_release_configuration.py` | Initial 55 scenarios passed in 2.84 s; final expanded 60 scenarios passed in 3.11 s, including actual Django logging initialization. |
| Initial sandbox `PY -m pytest -q` | 218 passed; three loopback listener/restart tests blocked by socket permissions. |
| Permitted complete `PY -m pytest -q` | 221 passed in 43.49 s: 161 accepted regression scenarios plus 60 configuration/security scenarios. No application source changed after this run. |
| Final permitted complete `PY -m pytest -q` | **221 passed in 45.90 s** after the logging scenario was strengthened to exercise actual Django initialization. This is the final application/test revision. |
| `PY -B /tmp/task022b_validate.py` | Actual task source/Python/lock pins verified; development system check, fresh isolated `migrate --noinput`, `makemigrations --check --dry-run`, `migrate --check`, foreign keys/private file modes and isolated legacy sentinel preservation passed. |
| `PY -m pip check` within validator | No broken requirements found. |
| Release `PY -m django check` within validator | Attempted with synthetic release inputs: unavailable driver confirmed by `Error loading psycopg2 or psycopg module`. This is an expected prerequisite limitation, not a passed release system check. No database provisioned or connected. |
| `python3 -B /tmp/task022b_review_checks.py` | Passed: exact 15-file scope including new files, 72 unrelated tracked files byte-identical, verbatim SQLite validator, approved closure hunks, clean unchanged main, exact task branch/baseline, empty staging, whitespace/newline checks, 125 local Markdown links and six added-diff credential-signature scans. |

`PY` denotes the interpreter and explicit source override above. The historical
58-test TASK-001 integration record is preserved separately; the current full
regression run exercises the unchanged original tests anew.

The complete review diff, including new files, is
`/tmp/task022b-review.patch`; its file modes/SHA-256 manifest is
`/tmp/task022b-review-manifest.json`. Re-running the review checker refreshes
both artifacts after this report is finalized. No files are staged.

## Limitations and human gate

Release settings are a validated configuration contract, not an operational
release. PostgreSQL driver selection, actual constraints/concurrency, ARM64/Pi
compatibility, release server/static serving, trusted ingress, HSTS and operating
procedures remain later reviewed work. Secret-file owner/mode checks follow the
approved current Linux environment; no other OS/container-user mapping is claimed.
No production configuration/destination, credentials or real financial data was
used. No live SMTP/Gemini/Telegram, infrastructure, CI, deployment, recovery or
real-user admission was attempted.

No new manual browser acceptance, fresh-host installation or wheel build was
performed: UI/assets, dependency/packaging configuration and their accepted
behaviour are preserved, while actual loopback/static/restart regressions ran.
Broader acceptance cases remain partial/planned. The approved 8-hour estimate and
264-hour baseline are unchanged; passing checks do not close TASK-022B.

Review the complete tracked/new-file diff and acceptance evidence. **Stop at
Human Review Gate.** No commit, push, PR, merge, branch/worktree deletion,
deployment or subsequent task follows automatically.
