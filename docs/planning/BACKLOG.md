# Finance Tracker — Development Backlog

Status: Owner-approved DEC-025 planning baseline. TASK-001, TASK-022A, TASK-025A and TASK-004A1 are Completed — Accepted and Integrated within their recorded scopes. M-009 is Completed — Accepted; see the [M-009 closure record](../testing/M-009_CLOSURE.md). Only the three M-009 leaves gain completion status in this closure. Outside M-009, status/evidence fields below retain their historical baseline wording; they are not a current assertion that accepted TASK-022B is unimplemented. TASK-022B is already accepted/integrated in current main at `a338168`; its separate status reconciliation and parent-rollup bookkeeping are outside this milestone-only change. Deferred/superseded work is not completed.

## Baseline and prototype allocation

Count remaining executable MVP leaves only: **264 hours**, including **16 hours** for M-009. TASK-001's historical four-hour estimate is excluded from remaining effort and is not an actual-time claim. Later Gemini TASK-014/015 total 24 hours outside the MVP. Deferred tasks/future candidates and all rollups contribute zero additional hours.

| Package | Early prototype | Remaining portion | Total |
|---|---|---|---|
| Django foundation TASK-022 plus CI TASK-023 and compatibility TASK-024 | TASK-022A: 8 h | TASK-022B: 8 h; TASK-023: 6 h; TASK-024: 6 h | 28 h |
| Identity TASK-025 plus roles TASK-026 and MFA TASK-027 | TASK-025A: 4 h | TASK-025B: 16 h; TASK-026: 16 h; TASK-027: 12 h | 48 h |
| Rules, accounts, movements, valuation and history | TASK-004A1: 4 h | TASK-004A2: 2 h; TASK-004B: 4 h; TASK-002: 6 h; TASK-028: 6 h; TASK-008A/B: 6/2 h; TASK-010: 6 h | 36 h |

The first three executable leaves are TASK-022A -> TASK-025A -> TASK-004A1. Full infrastructure, PostgreSQL hardening, CI, invitations and Admin MFA are not prerequisites to that local synthetic demonstration. Initial exact cash parsing belongs to that form; complete monetary policy remains TASK-002. Full real-user/sensitive-data admission still waits for M-007.

## Completed historical task

### TASK-001 — Runtime skeleton and local configuration

- **Status:** Completed — Accepted and Integrated, limited historical scope.
- **Priority / historical estimate:** Must / 4 h, not an actual-effort claim; excluded from the 264 h remaining.
- **Dependencies:** None.
- **Requirements (historical wording):** FR-001, FR-002, FR-032; NFR-001, NFR-002, NFR-006, NFR-009, scoped setup portions only.
- **Acceptance/evidence:** Commit `5052b5b` integrates accepted source `475492a`; its record states 58 pytest passes and successful pip check on Linux x86_64/Python 3.14.8. Not rerun in this documentation change. Existing package/configuration/Streamlit shell remains unchanged; no Django/financial/Pi acceptance is inferred.
- **Validation limitations:** Fresh host, physical LAN checks and new browser acceptance were not run for that integration. Replacing the shell is separate authorized work; do not reopen TASK-001 or count it twice.

## MVP executable leaves

### TASK-022A — Prototype Django shell and dashboard

- **Type / priority / status:** Executable leaf / Must / Completed — Accepted and Integrated.
- **WBS / estimate:** 1.4.1 / 8 h, focused tests and notes included.
- **Dependencies:** TASK-001.
- **Related requirements:** FR-001, FR-032, NFR-001, NFR-004; applicable tests in RTM.
- **Acceptance criteria:** Local Django package, final user-model foundation, Dashboard/Accounts navigation, clean template layout, readable account cards and synthetic-data banner work on loopback. No SPA/frontend framework or deployment. Include startup and navigation checks.
- **Decision gates:** None.
- **Accepted evidence:** Local main integration `18c1066`; see the [M-009 closure record](../testing/M-009_CLOSURE.md) for scoped verification and owner acceptance.

### TASK-025A — Prototype standard Django authentication

- **Type / priority / status:** Executable leaf / Must / Completed — Accepted and Integrated.
- **WBS / estimate:** 1.7.1 / 4 h, focused tests and notes included.
- **Dependencies:** TASK-022A.
- **Related requirements:** FR-034; applicable tests in RTM.
- **Acceptance criteria:** Locally provisioned synthetic identity can log in/out using Django hashing, sessions and CSRF; protected pages reject anonymous access. No public signup, invitation emails or claim of production security.
- **Decision gates:** None.
- **Accepted evidence:** Local main integration `d27f06b`; see the [M-009 closure record](../testing/M-009_CLOSURE.md) for scoped verification and owner acceptance.

### TASK-004A1 — Prototype account creation and balances

- **Type / priority / status:** Executable leaf / Must / Completed — Accepted and Integrated.
- **WBS / estimate:** 2.1.1.1 / 4 h, focused tests and notes included.
- **Dependencies:** TASK-025A.
- **Related requirements:** FR-003, FR-037, NFR-004, NFR-012 (prototype input subset only), TC-039, TC-053; applicable tests in RTM.
- **Acceptance criteria:** An intuitive form creates an owned savings account with exact nonnegative synthetic opening balance and clear currency; cards show the saved balance and total. Valid input survives errors; empty state explains next action. Refresh/restart retains records; owner demonstrates the complete path.
- **Decision gates:** None.
- **Accepted evidence:** Local main integration `6c937a6`; see the [M-009 closure record](../testing/M-009_CLOSURE.md) for scoped verification and owner acceptance.

### TASK-022B — Complete Django configuration and boundaries

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 1.4.2 / 8 h, focused tests and notes included.
- **Dependencies:** TASK-004A1.
- **Related requirements:** FR-001, NFR-002, NFR-006; applicable tests in RTM.
- **Acceptance criteria:** Complete separate development/release settings, private secrets handling, redacted configuration errors and service boundaries; retain working prototype UI. No infrastructure deployment.
- **Decision gates:** None.

### TASK-023 — GitHub Actions CI

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 1.5 / 6 h, focused tests and notes included.
- **Dependencies:** TASK-022B.
- **Related requirements:** FR-046; applicable tests in RTM.
- **Acceptance criteria:** Reviewed CI runs applicable synthetic checks without production secrets; add PostgreSQL integration coverage as persistence is introduced. No automatic deployment.
- **Decision gates:** None.

### TASK-024 — Pi and deployment compatibility assessment

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 1.6 / 6 h, focused tests and notes included.
- **Dependencies:** TASK-022B.
- **Related requirements:** FR-047, NFR-007, NFR-009; applicable tests in RTM.
- **Acceptance criteria:** Check intended Pi 5 8 GB/CasaOS/Docker Compose/Cloudflare environment, ARM64 Python/dependency/image compatibility and storage assumptions using synthetic data. Record unsupported combinations; no silently selected OS/image versions or deployment.
- **Decision gates:** OQ-004, OQ-008.

### TASK-025B — Invite-only release authentication

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 1.7.2 / 16 h, focused tests and notes included.
- **Dependencies:** TASK-025A, TASK-022B.
- **Related requirements:** FR-033, FR-034, NFR-013; applicable tests in RTM.
- **Acceptance criteria:** Extend existing Django identity model to email/password membership, expiring hashed single-use invitations, verified-email reset, throttling, suspension/session revocation and secure-cookie/CSRF tests. Synthetic tests only.
- **Decision gates:** OQ-010.

### TASK-026 — Roles, ownership policy and private health

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 1.8 / 16 h, focused tests and notes included.
- **Dependencies:** TASK-025B.
- **Related requirements:** FR-035, FR-036, FR-045, NFR-001, NFR-013; applicable tests in RTM.
- **Acceptance criteria:** Admin/User access matrix, deny-by-default service guards and sanitized health views pass synthetic checks. No financial admin models, impersonation, arbitrary password changes or takeover through email/role edits. Financial-path isolation is completed by TASK-003 and verified by TASK-019.
- **Decision gates:** OQ-010.

### TASK-027 — Required Admin MFA

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 1.9 / 12 h, focused tests and notes included.
- **Dependencies:** TASK-026.
- **Related requirements:** FR-051, NFR-013; applicable tests in RTM.
- **Acceptance criteria:** Admin enrollment/challenge/recovery and session invalidation work; no Admin operations before MFA; lost-factor process does not grant financial access.
- **Decision gates:** OQ-010.

### TASK-002 — Exact wealth, savings and date rules

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 1.2 / 6 h, focused tests and notes included.
- **Dependencies:** TASK-001.
- **Related requirements:** FR-002, FR-012, FR-019, NFR-006, NFR-012; applicable tests in RTM.
- **Acceptance criteria:** Pure exact rules cover observation valuation, net contributions, unknown attribution, per-user dates and indicative goal contributions. Reject excess precision/nonfinite/overflow; no expense/trade/reservation engine.
- **Decision gates:** OQ-002.

### TASK-003 — PostgreSQL observations and ownership

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 1.3 / 20 h, focused tests and notes included.
- **Dependencies:** TASK-002, TASK-022B, TASK-026.
- **Related requirements:** FR-002, FR-032, FR-036, NFR-002, NFR-005, NFR-008, NFR-012; applicable tests in RTM.
- **Acceptance criteria:** Versioned PostgreSQL schema/repositories enforce owner relationships, atomic update batches, durable replay/version checks and exact persistence. Test actual PostgreSQL constraints/concurrency; disposable prototype data needs no migration.
- **Decision gates:** OQ-002, OQ-007.

### TASK-004A2 — Complete balance and holding observations

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 2.1.1.2 / 2 h, focused tests and notes included.
- **Dependencies:** TASK-004A1, TASK-003.
- **Related requirements:** FR-003, FR-004, FR-032, FR-037, FR-049, NFR-005; applicable tests in RTM.
- **Acceptance criteria:** Extend the existing form/model path to full account holdings and dated observations; exact validation, atomicity, conflict detection and replay service tests use the shared PostgreSQL foundation. Preserve the prototype workflow.
- **Decision gates:** OQ-002, OQ-007.

### TASK-004B — Account lifecycle and observation revision

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 2.1.2 / 4 h, focused tests and notes included.
- **Dependencies:** TASK-004A2.
- **Related requirements:** FR-003, FR-004, FR-049; applicable tests in RTM.
- **Acceptance criteria:** Rename/archive and owned asset definitions preserve history; revision reasons and superseded observations remain available; referenced unit changes cannot reinterpret history.
- **Decision gates:** OQ-002.

### TASK-008A — Manual prices and current wealth

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 3.1.1 / 6 h, focused tests and notes included.
- **Dependencies:** TASK-004B, TASK-002.
- **Related requirements:** FR-005, FR-011, FR-012, FR-050, NFR-012; applicable tests in RTM.
- **Acceptance criteria:** Dated prices, cash/holding totals and warnings work in the shared dashboard; missing values are incomplete, not zero; no independently added investment-account total.
- **Decision gates:** OQ-003.

### TASK-007A — Essential PostgreSQL backup and restore

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 2.4.1 / 10 h, focused tests and notes included.
- **Dependencies:** TASK-003, TASK-008A.
- **Related requirements:** FR-029, FR-030, NFR-011; applicable tests in RTM.
- **Acceptance criteria:** Synthetic round-trip preserves ownership, observations and exact figures; invalid candidate leaves live data intact; verify safety backup, stopped writers, rollback, session invalidation and paused jobs. No personal data admitted yet.
- **Decision gates:** OQ-006.

### TASK-028 — Classified savings updates

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 2.5 / 6 h, focused tests and notes included.
- **Dependencies:** TASK-004A2, TASK-002.
- **Related requirements:** FR-038, FR-039, NFR-005, NFR-008; applicable tests in RTM.
- **Acceptance criteria:** Optional dated contributions/withdrawals/internal movement annotations save with observations once. Starting wealth is excluded; no double addition. Incomplete intervals or changed coverage give unknown attribution; matching replay is idempotent and conflicting key reuse fails.
- **Decision gates:** OQ-007.

### TASK-008B — Valuation revisions and distribution

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 3.1.2 / 2 h, focused tests and notes included.
- **Dependencies:** TASK-008A, TASK-028.
- **Related requirements:** FR-005, FR-011, FR-012, FR-014, FR-049; applicable tests in RTM.
- **Acceptance criteria:** Complete owned price revisions and composition views; per-holding rounded values sum exactly and warnings persist; reuse shared revision/persistence behavior.
- **Decision gates:** None.

### TASK-010 — Historical wealth snapshots

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 3.3 / 6 h, focused tests and notes included.
- **Dependencies:** TASK-008B, TASK-028.
- **Related requirements:** FR-011, FR-015, FR-039, FR-044, FR-050; applicable tests in RTM.
- **Acceptance criteria:** Freeze coherent snapshot values and provenance, not a transaction-ledger reconstruction; missing past data stays missing; comparable interval residual only with valid completeness assertion and source revisions.
- **Decision gates:** None.

### TASK-011 — Goal lifecycle

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 4.1 / 4 h, focused tests and notes included.
- **Dependencies:** TASK-008A.
- **Related requirements:** FR-016; applicable tests in RTM.
- **Acceptance criteria:** Owned multiple goals with valid targets/deadlines and explicit closure; no cash reservation behavior.
- **Decision gates:** None.

### TASK-029 — Account-linked goal progress

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 4.4 / 4 h, focused tests and notes included.
- **Dependencies:** TASK-011, TASK-003.
- **Related requirements:** FR-018, FR-048, NFR-008; applicable tests in RTM.
- **Acceptance criteria:** Owned account links have one active goal per account; concurrent assignments cannot duplicate funding; value/withdrawal changes affect progress without locking money.
- **Decision gates:** None.

### TASK-013 — Indicative saving projections

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 4.3 / 4 h, focused tests and notes included.
- **Dependencies:** TASK-029, TASK-002.
- **Related requirements:** FR-019; applicable tests in RTM.
- **Acceptance criteria:** Use linked values, remaining target and local deadline; show funded/overdue/incomplete states and upward-rounded amount; do not infer actual income or investment returns.
- **Decision gates:** None.

### TASK-030 — Optional profile and review dates

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 4.5 / 8 h, focused tests and notes included.
- **Dependencies:** TASK-025B, TASK-003.
- **Related requirements:** FR-040, FR-050; applicable tests in RTM.
- **Acceptance criteria:** Users manually maintain optional income/expense estimates and explicitly confirm unchanged information; estimated surplus stays separate; no profile requirement for reports.
- **Decision gates:** None.

### TASK-007B — Owned export and expanded recovery

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 2.4.2 / 6 h, focused tests and notes included.
- **Dependencies:** TASK-007A, TASK-010, TASK-029, TASK-030.
- **Related requirements:** FR-029, FR-030, FR-031, NFR-011; applicable tests in RTM.
- **Acceptance criteria:** Export only own data with exact values and safe text; repeat recovery with goals, profile, snapshots, identity/session state and job-state safeguards; whole backup remains operator-only.
- **Decision gates:** None.

### TASK-031 — Saved private monthly reports

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 6.4 / 14 h, focused tests and notes included.
- **Dependencies:** TASK-010, TASK-013, TASK-030, TASK-007B.
- **Related requirements:** FR-043, FR-044, FR-050; applicable tests in RTM.
- **Acceptance criteria:** Previous local calendar-month report contains available month-end values, reported movements, goal state and dated profile estimates; preserve missing data and source versions. Atomic immutable revisions, owner-only viewing and no automatic AI.
- **Decision gates:** None.

### TASK-032 — Monthly reporting scheduler

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 6.5 / 12 h, focused tests and notes included.
- **Dependencies:** TASK-031.
- **Related requirements:** FR-041, FR-043; applicable tests in RTM.
- **Acceptance criteria:** Single scheduled management command claims unique occurrences, survives repeated/concurrent invocation and generates reports without fresh user input or SMTP success; test timezone/month/DST/downtime behavior.
- **Decision gates:** OQ-005.

### TASK-033 — Generic reminder email

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 6.6 / 10 h, focused tests and notes included.
- **Dependencies:** TASK-032, TASK-025B.
- **Related requirements:** FR-042, NFR-003, NFR-010; applicable tests in RTM.
- **Acceptance criteria:** Send approved generic reminders to verified email using fakes; inspect subjects/bodies/links/logs for financial details or bearer report access; failures do not block reports and ambiguity is visible.
- **Decision gates:** OQ-005, OQ-009.

### TASK-019 — System, privacy and owner verification

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 7.1 / 24 h, focused tests and notes included.
- **Dependencies:** TASK-007B, TASK-013, TASK-030, TASK-033, TASK-023, TASK-027.
- **Related requirements:** FR-036, NFR-004, NFR-007, NFR-013; applicable tests in RTM.
- **Acceptance criteria:** Run all MVP acceptance scenarios with synthetic multi-user fixtures, direct-ID/job/export/cache attacks, exact wealth/unknown attribution, usability and recovery. Record actual evidence and close mandatory defects.
- **Decision gates:** None.

### TASK-020 — Compose deployment and recovery rehearsal

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 7.2 / 24 h, focused tests and notes included.
- **Dependencies:** TASK-019, TASK-024.
- **Related requirements:** FR-001, FR-029, FR-030, FR-032, FR-045, FR-047, NFR-001, NFR-002, NFR-009, NFR-011; applicable tests in RTM.
- **Acceptance criteria:** After separate infrastructure/deployment authorization, validate ARM64 Compose app/database/runner/tunnel lifecycle on intended Pi/CasaOS host, private listeners/volumes, HTTPS/session settings, backup restoration, rollback and sanitized health. No sensitive data before the release gate.
- **Decision gates:** OQ-003, OQ-006, OQ-008, OQ-009, OQ-010.

### TASK-021 — Release documentation and acceptance

- **Type / priority / status:** Executable leaf / Must / Not Started.
- **WBS / estimate:** 7.3 / 12 h, focused tests and notes included.
- **Dependencies:** TASK-020.
- **Related requirements:** FR-047, NFR-009; applicable tests in RTM.
- **Acceptance criteria:** Observed setup, account/profile/report workflows, operations, recovery, limitations and owner acceptance are recorded; no automatic commit/push/merge/deploy. Real users/sensitive data require all release gates and separate authorization.
- **Decision gates:** None.

## Non-additive completion rollups

A rollup depends on completion of its named children. Its completion dependency is not inherited by an early child; only each leaf's explicit dependency list controls execution. All rollups remain Not Started. TASK-004A was formerly an executable leaf and is now a six-hour rollup; its original role is explicitly split, not counted again.

| ID | Title | Children | Rollup budget, not extra |
|---|---|---|---|
| TASK-004 | Account and asset workflows | TASK-004A, TASK-004B | 10 h |
| TASK-004A | Basic accounts and observations | TASK-004A1, TASK-004A2 | 6 h |
| TASK-007 | Backup, restore and CSV | TASK-007A, TASK-007B | 16 h |
| TASK-008 | Manual prices and valuation | TASK-008A, TASK-008B | 8 h |
| TASK-022 | Django foundation | TASK-022A, TASK-022B | 16 h |
| TASK-025 | Authentication | TASK-025A, TASK-025B | 20 h |

## Historical deferred or superseded tasks

Original task descriptions/estimates remain in baseline `5052b5b`. No original ID is reassigned to a different feature. No remaining budget or completion claim is attached here.

| ID | Original purpose | Disposition / new coverage |
|---|---|---|
| TASK-005 | Financial ledger workflows | Deferred ledger/reservation/Telegram work. Observation replay uses TASK-003/004A2/028; goal links use TASK-029; reports/email use TASK-031/032/033; composition uses TASK-008B. |
| TASK-005A | Atomic opening transactions and replay protection | Deferred ledger/reservation/Telegram work. Observation replay uses TASK-003/004A2/028; goal links use TASK-029; reports/email use TASK-031/032/033; composition uses TASK-008B. |
| TASK-005B | Income, expense and trading ledger | Deferred ledger/reservation/Telegram work. Observation replay uses TASK-003/004A2/028; goal links use TASK-029; reports/email use TASK-031/032/033; composition uses TASK-008B. |
| TASK-006 | Ledger corrections and transfers | Deferred ledger/reservation/Telegram work. Observation replay uses TASK-003/004A2/028; goal links use TASK-029; reports/email use TASK-031/032/033; composition uses TASK-008B. |
| TASK-009 | Monthly cash-flow dashboard and distribution | Actual cash-flow dashboard deferred; current wealth composition follows TASK-008B and historical snapshots TASK-010. |
| TASK-012 | Atomic cash reservations | Deferred ledger/reservation/Telegram work. Observation replay uses TASK-003/004A2/028; goal links use TASK-029; reports/email use TASK-031/032/033; composition uses TASK-008B. |
| TASK-016 | Telegram recipient and preferences | Deferred ledger/reservation/Telegram work. Observation replay uses TASK-003/004A2/028; goal links use TASK-029; reports/email use TASK-031/032/033; composition uses TASK-008B. |
| TASK-017 | Scheduled Telegram summaries | Deferred ledger/reservation/Telegram work. Observation replay uses TASK-003/004A2/028; goal links use TASK-029; reports/email use TASK-031/032/033; composition uses TASK-008B. |
| TASK-018 | Telegram goal notifications | Deferred ledger/reservation/Telegram work. Observation replay uses TASK-003/004A2/028; goal links use TASK-029; reports/email use TASK-031/032/033; composition uses TASK-008B. |

## Later Gemini release — outside 264 hours

### TASK-014 — Later Gemini adapter and consent

- **Type / priority / release / status:** Executable leaf / Must if later Gemini release is selected / Later Gemini / Not Started.
- **Estimate / WBS:** 12 h / 5.1.
- **Dependencies:** TASK-021.
- **Requirements:** FR-024.
- **Acceptance criteria:** Immutable minimized exact preview, single-use consent, bounded fake-tested adapter, redacted failures and no financial tools; provider configuration separate.
- **Decision gates:** OQ-011; separate task authorization.

### TASK-015 — Later savings and goal explanations

- **Type / priority / release / status:** Executable leaf / Must if later Gemini release is selected / Later Gemini / Not Started.
- **Estimate / WBS:** 12 h / 5.2.
- **Dependencies:** TASK-014.
- **Requirements:** FR-020, FR-021, FR-022, FR-023.
- **Acceptance criteria:** Explain approved wealth/savings/projections with warnings; no fabricated authoritative data or personalized security buy/sell advice; provider failure preserves core.
- **Decision gates:** OQ-011; separate task authorization.

## Future candidates

| ID | Candidate | Priority / estimate / status | Selection criteria |
|---|---|---|---|
| FUT-001 | Automatic prices and provider costs | Could / Not estimated / Deferred | Owner selects scope and approves requirements, dependencies and tests before work. FUT-006 does not defer the clean usable prototype layout. |
| FUT-002 | Advanced multi-currency/FX analysis | Could / Not estimated / Deferred | Owner selects scope and approves requirements, dependencies and tests before work. FUT-006 does not defer the clean usable prototype layout. |
| FUT-003 | Inflation adjustment and advanced portfolio analytics | Could / Not estimated / Deferred | Owner selects scope and approves requirements, dependencies and tests before work. FUT-006 does not defer the clean usable prototype layout. |
| FUT-004 | Recurring records and AI categorization | Could / Not estimated / Deferred | Owner selects scope and approves requirements, dependencies and tests before work. FUT-006 does not defer the clean usable prototype layout. |
| FUT-005 | Forecasting and scenarios | Could / Not estimated / Deferred | Owner selects scope and approves requirements, dependencies and tests before work. FUT-006 does not defer the clean usable prototype layout. |
| FUT-006 | Advanced responsive layouts | Could / Not estimated / Deferred | Owner selects scope and approves requirements, dependencies and tests before work. FUT-006 does not defer the clean usable prototype layout. |

Telegram remains deferred under TASK-016/017/018; detailed ledgers, expense categorization, advanced trades and cash reservations remain deferred under their original IDs. None is a hidden MVP dependency. Use the [schedule](PROJECT_SCHEDULE.md) for serial order/milestones and [RTM](../requirements/RTM.md) for requirement coverage.

## Closure boundary

M-009 closes only its accepted synthetic prototype scope. Current main already includes separately accepted TASK-022B at `a338168`; this closure does not re-accept or newly complete it, change parent rollups, select/start another task or authorize Git/deployment operations. Later financial, identity, PostgreSQL, recovery and release decisions remain at their recorded gates.
