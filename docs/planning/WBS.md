# Finance Tracker — Work Breakdown Structure

Status: Approved 264-hour remaining planning baseline; deliverables Not Started except accepted historical TASK-001. WBS leaf budgets include focused tests and notes. Parent/rollup rows are non-additive; completed/deferred/later work is excluded from the MVP total.

## Package accounting

| Package | Executable leaves | Hours |
|---|---|---|
| Django foundation, CI and Pi compatibility | TASK-022A, TASK-022B, TASK-023, TASK-024 | 28 |
| Authentication, invitations, roles and Admin MFA | TASK-025A, TASK-025B, TASK-026, TASK-027 | 48 |
| PostgreSQL observations and ownership | TASK-003 | 20 |
| Rules, account updates, movements, valuation and history | TASK-002, TASK-004A1, TASK-004A2, TASK-004B, TASK-028, TASK-008A, TASK-008B, TASK-010 | 36 |
| Goals | TASK-011, TASK-029, TASK-013 | 12 |
| Optional profile | TASK-030 | 8 |
| Reports, scheduling and generic reminder email | TASK-031, TASK-032, TASK-033 | 36 |
| Recovery and exports | TASK-007A, TASK-007B | 16 |
| System verification | TASK-019 | 24 |
| Deployment rehearsal and release documentation | TASK-020, TASK-021 | 36 |

Total: **264 h**, including M-009's **8+4+4=16 h** from existing packages. The remaining portion is 248 h; no separate prototype budget is added. TASK-001's historical 4 h estimate and later Gemini's 24 h are not counted. The earlier seven-phase 152-hour baseline is superseded under DEC-025 and remains historical, not a concurrent budget.

## Executable deliverables

### 1.4.1 — Prototype Django shell and dashboard

- **Backlog / effort:** TASK-022A; 8 h.
- **Deliverable / Definition of Done:** Local Django package, final user-model foundation, Dashboard/Accounts navigation, clean template layout, readable account cards and synthetic-data banner work on loopback. No SPA/frontend framework or deployment. Include startup and navigation checks.
- **Dependencies:** TASK-001; decision gates None.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 1.7.1 — Prototype standard Django authentication

- **Backlog / effort:** TASK-025A; 4 h.
- **Deliverable / Definition of Done:** Locally provisioned synthetic identity can log in/out using Django hashing, sessions and CSRF; protected pages reject anonymous access. No public signup, invitation emails or claim of production security.
- **Dependencies:** TASK-022A; decision gates None.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 2.1.1.1 — Prototype account creation and balances

- **Backlog / effort:** TASK-004A1; 4 h.
- **Deliverable / Definition of Done:** An intuitive form creates an owned savings account with exact nonnegative synthetic opening balance and clear currency; cards show the saved balance and total. Valid input survives errors; empty state explains next action. Refresh/restart retains records; owner demonstrates the complete path.
- **Dependencies:** TASK-025A; decision gates None.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 1.4.2 — Complete Django configuration and boundaries

- **Backlog / effort:** TASK-022B; 8 h.
- **Deliverable / Definition of Done:** Complete separate development/release settings, private secrets handling, redacted configuration errors and service boundaries; retain working prototype UI. No infrastructure deployment.
- **Dependencies:** TASK-004A1; decision gates None.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 1.5 — GitHub Actions CI

- **Backlog / effort:** TASK-023; 6 h.
- **Deliverable / Definition of Done:** Reviewed CI runs applicable synthetic checks without production secrets; add PostgreSQL integration coverage as persistence is introduced. No automatic deployment.
- **Dependencies:** TASK-022B; decision gates None.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 1.6 — Pi and deployment compatibility assessment

- **Backlog / effort:** TASK-024; 6 h.
- **Deliverable / Definition of Done:** Check intended Pi 5 8 GB/CasaOS/Docker Compose/Cloudflare environment, ARM64 Python/dependency/image compatibility and storage assumptions using synthetic data. Record unsupported combinations; no silently selected OS/image versions or deployment.
- **Dependencies:** TASK-022B; decision gates OQ-004, OQ-008.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 1.7.2 — Invite-only release authentication

- **Backlog / effort:** TASK-025B; 16 h.
- **Deliverable / Definition of Done:** Extend existing Django identity model to email/password membership, expiring hashed single-use invitations, verified-email reset, throttling, suspension/session revocation and secure-cookie/CSRF tests. Synthetic tests only.
- **Dependencies:** TASK-025A, TASK-022B; decision gates OQ-010.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 1.8 — Roles, ownership policy and private health

- **Backlog / effort:** TASK-026; 16 h.
- **Deliverable / Definition of Done:** Admin/User access matrix, deny-by-default service guards and sanitized health views pass synthetic checks. No financial admin models, impersonation, arbitrary password changes or takeover through email/role edits. Financial-path isolation is completed by TASK-003 and verified by TASK-019.
- **Dependencies:** TASK-025B; decision gates OQ-010.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 1.9 — Required Admin MFA

- **Backlog / effort:** TASK-027; 12 h.
- **Deliverable / Definition of Done:** Admin enrollment/challenge/recovery and session invalidation work; no Admin operations before MFA; lost-factor process does not grant financial access.
- **Dependencies:** TASK-026; decision gates OQ-010.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 1.2 — Exact wealth, savings and date rules

- **Backlog / effort:** TASK-002; 6 h.
- **Deliverable / Definition of Done:** Pure exact rules cover observation valuation, net contributions, unknown attribution, per-user dates and indicative goal contributions. Reject excess precision/nonfinite/overflow; no expense/trade/reservation engine.
- **Dependencies:** TASK-001; decision gates OQ-002.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 1.3 — PostgreSQL observations and ownership

- **Backlog / effort:** TASK-003; 20 h.
- **Deliverable / Definition of Done:** Versioned PostgreSQL schema/repositories enforce owner relationships, atomic update batches, durable replay/version checks and exact persistence. Test actual PostgreSQL constraints/concurrency; disposable prototype data needs no migration.
- **Dependencies:** TASK-002, TASK-022B, TASK-026; decision gates OQ-002, OQ-007.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 2.1.1.2 — Complete balance and holding observations

- **Backlog / effort:** TASK-004A2; 2 h.
- **Deliverable / Definition of Done:** Extend the existing form/model path to full account holdings and dated observations; exact validation, atomicity, conflict detection and replay service tests use the shared PostgreSQL foundation. Preserve the prototype workflow.
- **Dependencies:** TASK-004A1, TASK-003; decision gates OQ-002, OQ-007.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 2.1.2 — Account lifecycle and observation revision

- **Backlog / effort:** TASK-004B; 4 h.
- **Deliverable / Definition of Done:** Rename/archive and owned asset definitions preserve history; revision reasons and superseded observations remain available; referenced unit changes cannot reinterpret history.
- **Dependencies:** TASK-004A2; decision gates OQ-002.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 3.1.1 — Manual prices and current wealth

- **Backlog / effort:** TASK-008A; 6 h.
- **Deliverable / Definition of Done:** Dated prices, cash/holding totals and warnings work in the shared dashboard; missing values are incomplete, not zero; no independently added investment-account total.
- **Dependencies:** TASK-004B, TASK-002; decision gates OQ-003.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 2.4.1 — Essential PostgreSQL backup and restore

- **Backlog / effort:** TASK-007A; 10 h.
- **Deliverable / Definition of Done:** Synthetic round-trip preserves ownership, observations and exact figures; invalid candidate leaves live data intact; verify safety backup, stopped writers, rollback, session invalidation and paused jobs. No personal data admitted yet.
- **Dependencies:** TASK-003, TASK-008A; decision gates OQ-006.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 2.5 — Classified savings updates

- **Backlog / effort:** TASK-028; 6 h.
- **Deliverable / Definition of Done:** Optional dated contributions/withdrawals/internal movement annotations save with observations once. Starting wealth is excluded; no double addition. Incomplete intervals or changed coverage give unknown attribution; matching replay is idempotent and conflicting key reuse fails.
- **Dependencies:** TASK-004A2, TASK-002; decision gates OQ-007.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 3.1.2 — Valuation revisions and distribution

- **Backlog / effort:** TASK-008B; 2 h.
- **Deliverable / Definition of Done:** Complete owned price revisions and composition views; per-holding rounded values sum exactly and warnings persist; reuse shared revision/persistence behavior.
- **Dependencies:** TASK-008A, TASK-028; decision gates None.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 3.3 — Historical wealth snapshots

- **Backlog / effort:** TASK-010; 6 h.
- **Deliverable / Definition of Done:** Freeze coherent snapshot values and provenance, not a transaction-ledger reconstruction; missing past data stays missing; comparable interval residual only with valid completeness assertion and source revisions.
- **Dependencies:** TASK-008B, TASK-028; decision gates None.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 4.1 — Goal lifecycle

- **Backlog / effort:** TASK-011; 4 h.
- **Deliverable / Definition of Done:** Owned multiple goals with valid targets/deadlines and explicit closure; no cash reservation behavior.
- **Dependencies:** TASK-008A; decision gates None.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 4.4 — Account-linked goal progress

- **Backlog / effort:** TASK-029; 4 h.
- **Deliverable / Definition of Done:** Owned account links have one active goal per account; concurrent assignments cannot duplicate funding; value/withdrawal changes affect progress without locking money.
- **Dependencies:** TASK-011, TASK-003; decision gates None.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 4.3 — Indicative saving projections

- **Backlog / effort:** TASK-013; 4 h.
- **Deliverable / Definition of Done:** Use linked values, remaining target and local deadline; show funded/overdue/incomplete states and upward-rounded amount; do not infer actual income or investment returns.
- **Dependencies:** TASK-029, TASK-002; decision gates None.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 4.5 — Optional profile and review dates

- **Backlog / effort:** TASK-030; 8 h.
- **Deliverable / Definition of Done:** Users manually maintain optional income/expense estimates and explicitly confirm unchanged information; estimated surplus stays separate; no profile requirement for reports.
- **Dependencies:** TASK-025B, TASK-003; decision gates None.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 2.4.2 — Owned export and expanded recovery

- **Backlog / effort:** TASK-007B; 6 h.
- **Deliverable / Definition of Done:** Export only own data with exact values and safe text; repeat recovery with goals, profile, snapshots, identity/session state and job-state safeguards; whole backup remains operator-only.
- **Dependencies:** TASK-007A, TASK-010, TASK-029, TASK-030; decision gates None.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 6.4 — Saved private monthly reports

- **Backlog / effort:** TASK-031; 14 h.
- **Deliverable / Definition of Done:** Previous local calendar-month report contains available month-end values, reported movements, goal state and dated profile estimates; preserve missing data and source versions. Atomic immutable revisions, owner-only viewing and no automatic AI.
- **Dependencies:** TASK-010, TASK-013, TASK-030, TASK-007B; decision gates None.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 6.5 — Monthly reporting scheduler

- **Backlog / effort:** TASK-032; 12 h.
- **Deliverable / Definition of Done:** Single scheduled management command claims unique occurrences, survives repeated/concurrent invocation and generates reports without fresh user input or SMTP success; test timezone/month/DST/downtime behavior.
- **Dependencies:** TASK-031; decision gates OQ-005.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 6.6 — Generic reminder email

- **Backlog / effort:** TASK-033; 10 h.
- **Deliverable / Definition of Done:** Send approved generic reminders to verified email using fakes; inspect subjects/bodies/links/logs for financial details or bearer report access; failures do not block reports and ambiguity is visible.
- **Dependencies:** TASK-032, TASK-025B; decision gates OQ-005, OQ-009.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 7.1 — System, privacy and owner verification

- **Backlog / effort:** TASK-019; 24 h.
- **Deliverable / Definition of Done:** Run all MVP acceptance scenarios with synthetic multi-user fixtures, direct-ID/job/export/cache attacks, exact wealth/unknown attribution, usability and recovery. Record actual evidence and close mandatory defects.
- **Dependencies:** TASK-007B, TASK-013, TASK-030, TASK-033, TASK-023, TASK-027; decision gates None.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 7.2 — Compose deployment and recovery rehearsal

- **Backlog / effort:** TASK-020; 24 h.
- **Deliverable / Definition of Done:** After separate infrastructure/deployment authorization, validate ARM64 Compose app/database/runner/tunnel lifecycle on intended Pi/CasaOS host, private listeners/volumes, HTTPS/session settings, backup restoration, rollback and sanitized health. No sensitive data before the release gate.
- **Dependencies:** TASK-019, TASK-024; decision gates OQ-003, OQ-006, OQ-008, OQ-009, OQ-010.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

### 7.3 — Release documentation and acceptance

- **Backlog / effort:** TASK-021; 12 h.
- **Deliverable / Definition of Done:** Observed setup, account/profile/report workflows, operations, recovery, limitations and owner acceptance are recorded; no automatic commit/push/merge/deploy. Real users/sensitive data require all release gates and separate authorization.
- **Dependencies:** TASK-020; decision gates None.
- **Evidence:** Applicable requirement/test links in the backlog and RTM; no execution or acceptance claimed.

## Rollups and milestones

| Rollup | Children | Non-additive hours |
|---|---|---|
| TASK-004 | TASK-004A, TASK-004B | 10 |
| TASK-004A | TASK-004A1, TASK-004A2 | 6 |
| TASK-007 | TASK-007A, TASK-007B | 16 |
| TASK-008 | TASK-008A, TASK-008B | 8 |
| TASK-022 | TASK-022A, TASK-022B | 16 |
| TASK-025 | TASK-025A, TASK-025B | 20 |

M-009 requires TASK-022A/025A/004A1 plus P1-01–P1-06 demonstration and TC-053 evidence. M-001 is full secure foundation at 106 remaining hours; moving four account-work hours earlier explains its change from the former 102-hour proposal. M-001A remains 128 h with W1-01–W1-04; M-004 remains 168 h; M-007 remains 264 h. Milestone gates add no work outside their leaves.

All intermediate work stays synthetic. M-007 requires full authentication, authorization, Admin MFA, privacy, PostgreSQL integrity, backup/recovery, system verification, deployment rehearsal and owner acceptance before real users or sensitive data. No timebox permits removing safeguards. Later Gemini packages 5.1/5.2 map to TASK-014/015 (12 h each); no Telegram or ledger/reservation package is committed. See [backlog](BACKLOG.md) for historical task dispositions.

Historical WBS 1.1 remains accepted TASK-001 and is excluded from remaining effort. Retain original surviving leaf identities (1.2/1.3, 2.1.2, 2.4.1/2, 3.1.1/2, 3.3, 4.1/4.3, 5.1/5.2 and 7.1–7.3). WBS 2.1.1 is now a parent split into 2.1.1.1/2.1.1.2. Retired 2.2/2.3 ledger, 3.2 actual cash-flow, 4.2 reservation and 6.1–6.3 Telegram packages are not recycled. New Django/identity packages use 1.4–1.9, movements 2.5, goal links/profile 4.4/4.5 and reports/email 6.4–6.6.
