# M-009 — Early Working Prototype closure

Status: **Completed — Owner Accepted**, limited to the local synthetic prototype.

## Authority and accepted revision

This proposal records the owner's current "M-009 — Formal Milestone Closure" request, following prior prototype manual acceptance and the earlier approved closure proposal. No backlog task ID applies to this documentation maintenance. Proposed documentation changes await human review; no commit or integration is authorized. Accepted prototype revision: `6c937a6ff71ab5285c32ee6281b5e9d8014c9313`, integrating TASK-004A1 source `31acf5194e4ce76c2dbc986daa1017efcd8908e3`. Predecessors TASK-022A and TASK-025A were accepted/integrated at `18c1066` and `d27f06b`; TASK-001 remains accepted at `5052b5b`.

Current comparison baseline: `a338168910c35c385aabcd24f98092a06e087171` (local main), integrating separately accepted TASK-022B commit `32b58c665f0d5f42e226b534428bd4f2ff8d02c4`. The pending-worktree HEAD `32b58c6` has the same committed file tree as current main. TASK-022B is baseline context, not a prototype leaf newly completed by this closure.

## Scoped acceptance evidence

| Criterion | Accepted evidence |
|---|---|
| P1-01 | Guarded Django launcher, loopback listener and visible synthetic-data banner; accepted TASK-022A and integration regression evidence. |
| P1-02 | Explicit synthetic provisioning, standard password/session/CSRF login/logout and protected-page rejection; accepted TASK-025A and integration regression evidence. |
| P1-03 | Turkish Dashboard/Accounts navigation, active indication, readable saved cards, currency/balance, empty state and create action. |
| P1-04 | Labeled exact nonnegative synthetic USD opening form, useful errors, retained input and clear saved outcome. |
| P1-05 | Saved exact openings survive refresh/server restart; openings create no savings movement; no external integration or public listener. |
| P1-06 | Recorded focused/regression checks, desktop/narrow browser verification and the owner's successful manual sign-in/navigation/create/cards/logout demonstration. |

TC-053 is passed and owner-accepted for the complete P1-01–P1-06 prototype. TC-039 has accepted prototype usability coverage; broader release scenarios and FR/NFR obligations remain partial/planned.

## Recorded verification, not rerun for closure

The `6c937a6` integration record reports 161 pytest tests passed in 43.30 s against merged-main source on Linux x86_64/Python 3.14.8. It also records clean Django system checks, fresh isolated SQLite migrations, no migration drift, foreign-key/private-mode checks, successful pip check, lock-pin and packaged-asset checks, and TASK-001 preservation. The owner confirms automated verification and manual acceptance.

The later `a338168` TASK-022B integration record reports 60 focused tests passed in 3.26 s and 221 regression tests passed in 45.45 s against integrated main, plus development system/migration/dependency checks. It preserves earlier prototype behaviour and excludes closure planning edits. Release Django startup remains unavailable without the deferred PostgreSQL driver. These are recorded integration results, not test execution for this closure review.

Detailed developer/browser evidence is retained in [TASK-004A1 review](TASK-004A1_REVIEW.md), [TASK-025A review](TASK-025A_REVIEW.md) and [TASK-022A review](TASK-022A_REVIEW.md). Their pending-review wording describes their original snapshots; subsequent integration records and this owner acceptance supersede that status without rewriting history. No tests are claimed rerun by this documentation update. Historical TASK-001's original 58-pass record remains separate.

## Budget and release boundary

The accepted leaves consume 8+4+4=16 hours of planned allocation within the approved 264-hour baseline; 248 hours were originally allocated after M-009, including the subsequently accepted TASK-022B 8-hour allocation. This does not claim 248 hours of work remain now. These are estimates, not measured effort. Milestone positions and estimates are unchanged. This closure does not change parent-rollup statuses. TASK-025B and TASK-004A2 remain open. Both TASK-022 children now have separate accepted evidence; any parent bookkeeping is outside this M-009-only change.

Only synthetic USD openings and disposable private SQLite on loopback are accepted. Full identity lifecycle, authorization, Admin MFA, privacy, PostgreSQL integrity/concurrency, backup/recovery, Pi/CasaOS/Compose/Tunnel compatibility and deployment/system acceptance remain mandatory later gates before real users or sensitive data. M-001 and M-007 are not completed. TASK-022B is already separately accepted/integrated. No other task or milestone is newly completed; no real-user/sensitive-data admission, subsequent task or restricted Git/deployment operation is authorized.

## Documentation review boundary

Only TASK-022A, TASK-025A and TASK-004A1 gain leaf completion status; TASK-001's historical status is unchanged. P1-01–P1-06 and the complete prototype TC-053 are recorded as accepted; TC-039 remains prototype-subset coverage. Full FR/NFR obligations and all production acceptance gates stay partial/planned. No requirements, numerical policy, estimates, architecture, application, migration, test code or dependency changes are proposed. Historical task review files, including TASK-022B's current main acceptance note, are preserved byte-for-byte in the candidate tree. See [closure validation](M-009_CLOSURE_REVIEW.md) for actual document checks and omissions.
