# Finance Tracker — Software Requirements Specification

Status: Owner-approved Savings and Wealth MVP scope and milestone strategy (DEC-020 through DEC-026); revised requirements pending human review. Implementation status is separate: only historical TASK-001 is accepted. New Django, schema, infrastructure and planned cases are not implemented by this revision.

## Product, actors and release boundaries

Finance Tracker is a small invite-only savings, wealth and investment portfolio application. Users manually maintain current balances/holdings and optional savings movements, without recording every expense or trade. The User owns financial data; Admin manages membership/health without financial access; Operator controls deployment/backup outside application roles. Accounts are financial locations, distinct from login identities. A contribution crosses the boundary of all tracked accounts; moving between them is internal.

Initial release includes balances, manual holdings/prices, qualified wealth/history, account-linked goals, optional estimated profile, monthly authenticated reports and generic reminder email. Gemini is a later release; Telegram, detailed ledgers, expense categorization, cost-basis/trading records and cash reservations are deferred. No liabilities or automatic transactions are committed.

Prototype M-009 is a 16-hour reusable local Django slice with synthetic data, development SQLite and standard development authentication. All intermediate milestones use synthetic data. Full authentication, authorization, Admin MFA, privacy, PostgreSQL integrity/recovery and release verification are mandatory before real users or sensitive data. Intended deployment is Pi 5 (8 GB), CasaOS, Docker Compose and Cloudflare Tunnel/HTTPS; compatibility and implementation remain later work. Financial core is independent of SMTP/Gemini; remote access still depends on host/WAN/Tunnel.

Must means required for the specified release, not implemented. Later Gemini obligations do not gate the MVP. Prior requirement meanings and original acceptance text remain recoverable at baseline `5052b5b`; amended concepts below are explicit scope changes authorized by DEC-020/021, not retrospective evidence for TASK-001.

## Functional requirements

### FR-001 — Deployment configuration

The system shall load validated deployment configuration and keep external adapters disabled unless configured.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Missing optional credentials do not block core startup; errors redact secrets; development and release settings are distinct.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-022A, TASK-022B, TASK-020; US-001; UC-001; TC-001, TC-038, TC-053.
- **Source:** Charter D10 and DEC-020 through DEC-026; BR-024.

### FR-002 — Per-user reporting currency

The system shall require one reporting currency and scale per User before financial records; prevent reinterpretation after records exist.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Two users may choose different currencies; changing a used currency is rejected. Prototype fixtures explicitly choose a synthetic example currency.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-002, TASK-003; US-001; UC-001; TC-002, TC-047.
- **Source:** Charter D2 and DEC-020 through DEC-026; BR-001, BR-011.

### FR-003 — Account management

The system shall create, rename, list and archive owned savings and investment accounts.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Names are unique within an owner; history survives archive; archival changes comparison coverage and cannot manufacture savings.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-004A1, TASK-004A2, TASK-004B; US-002; UC-002; TC-003, TC-039, TC-053.
- **Source:** Charter D2 and DEC-020 through DEC-026; BR-016, BR-018.

### FR-004 — Asset definitions

The system shall maintain owned instrument definitions for cash, currencies, gold, stocks and funds with declared units.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Referenced units cannot be silently changed; instruments with history retain their identity; foreign holdings use manual reporting-currency prices.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-004A2, TASK-004B; US-003; UC-002; TC-004, TC-043.
- **Source:** Charter D2 and DEC-020 through DEC-026; BR-001, BR-011, BR-016.

### FR-005 — Dated manual prices

The system shall record dated positive exact unit prices and auditable revisions.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Future, nonfinite or invalid prices fail; historical valuations never use a price effective after the valuation date.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-008A, TASK-008B; US-008; UC-007; TC-005, TC-047.
- **Source:** Charter D1/D2 and DEC-020 through DEC-026; BR-002, BR-011, BR-013.

### FR-011 — Valuation completeness

The system shall show missing and stale balances, quantities and prices with observation dates.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Unpriced holdings make totals incomplete; carrying a value forward does not refresh it; missing values never become assumed zero.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-008A, TASK-008B, TASK-010; US-009; UC-008; TC-011, TC-072.
- **Source:** Charter D1 and DEC-020 through DEC-026; BR-002, BR-005, BR-013.

### FR-012 — Tracked wealth totals

The system shall calculate total tracked assets from cash and priced holdings without double-counting.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Cash 1000 plus 10 units priced at 20 equals 1200; goal links add nothing; liabilities are explicitly excluded; incomplete totals are qualified.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-002, TASK-008A, TASK-008B; US-009; UC-008; TC-012, TC-035, TC-068.
- **Source:** Charter D1 and DEC-020 through DEC-026; BR-002, BR-005, BR-011.

### FR-014 — Portfolio distribution

The system shall display composition consistent with the priced wealth subtotal.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Distribution sums to that subtotal; unknown values appear separately; empty or zero-value portfolios show guidance rather than invented percentages.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-008B; US-009; UC-008; TC-014.
- **Source:** Charter D1 and DEC-020 through DEC-026; BR-005.

### FR-015 — Historical wealth

The system shall display dated, immutable wealth snapshots with their coverage and freshness limitations.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** No current balance is backfilled into an earlier date; missing history remains missing; corrections may create a new snapshot revision, not overwrite an accepted snapshot.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-010; US-011; UC-008; TC-015, TC-069.
- **Source:** Charter D1 and DEC-020 through DEC-026; BR-013, BR-019.

### FR-016 — Savings goals

The system shall create and edit multiple owned savings goals with targets and deadlines.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Validate positive targets; allow overdue goals with a clear state; closing a goal releases its account links, not cash.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-011; US-012; UC-009; TC-016.
- **Source:** Charter D3 and DEC-020 through DEC-026; BR-020.

### FR-018 — Goal progress

The system shall measure goal progress from linked account values without locking or duplicating assets.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Each account supports at most one active goal; withdrawal or falling value can reduce progress; missing/stale values qualify progress.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-029; US-021; UC-018; TC-018, TC-071.
- **Source:** Charter D3 and DEC-020 through DEC-026; BR-005, BR-020.

### FR-019 — Indicative monthly savings

The system shall calculate indicative monthly saving needed from remaining goal value and deadline.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Gap 1.00 over three opportunities rounds upward to 0.34 at scale 2; funded gives zero; overdue underfunded gives overdue, not division by zero; incomplete valuation qualifies the result.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-002, TASK-013; US-014; UC-011; TC-019, TC-047.
- **Source:** Charter D3 and DEC-020 through DEC-026; BR-009, BR-011, BR-020.

### FR-020 — Savings explanations

The system shall offer user-initiated explanations of approved savings and wealth summaries.

- **Priority / release:** Must / Later Gemini
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Explain reported contributions and unknown attribution honestly; estimates are not actual spending; Gemini cannot alter computed values.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-015; US-015; UC-012; TC-020, TC-049.
- **Source:** Charter D4 and DEC-020 through DEC-026; BR-012.

### FR-021 — Goal feasibility explanations

The system shall explain deterministic goal projections using approved context.

- **Priority / release:** Must / Later Gemini
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Context preserves stale/missing-data warnings and includes profile estimates only when approved; goals and balances remain unchanged.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-015; US-016; UC-012; TC-021, TC-049.
- **Source:** Charter D4 and DEC-020 through DEC-026; BR-012.

### FR-022 — AI summaries

The system shall display optional AI summaries separately from deterministic reports.

- **Priority / release:** Must / Later Gemini
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Output is labeled unverified explanation and cannot become an authoritative saved financial figure.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-015; US-015; UC-012; TC-022, TC-049.
- **Source:** Charter D4 and DEC-020 through DEC-026; BR-012.

### FR-023 — Financial explanation questions

The system shall allow approved explanatory questions without execution tools or personalized security buy/sell recommendations.

- **Priority / release:** Must / Later Gemini
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Requests for specific security recommendations receive an explanation-only boundary; no SQL, payments, trades or writes can execute.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-015; US-017; UC-012; TC-023, TC-049.
- **Source:** Charter D4 and DEC-020 through DEC-026; BR-012.

### FR-024 — Per-request Gemini consent

The system shall preview and approve the exact minimized question and summary for one call.

- **Priority / release:** Must / Later Gemini
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Cancel makes zero calls; changed context/question invalidates consent; replay cannot consume approval twice; labels, notes and credentials are excluded from generated context.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-014; US-015, US-016, US-017; UC-012, UC-017; TC-024, TC-036, TC-049.
- **Source:** Charter D4 and DEC-020 through DEC-026; BR-012.

### FR-029 — Operator backup

The system shall provide a consistent protected PostgreSQL backup, separate from user exports.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Operator procedure verifies a backup independently; ordinary Users and application Admin cannot download a whole-system backup.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-007A, TASK-007B, TASK-020; US-020; UC-015; TC-029, TC-046, TC-068.
- **Source:** Charter D10 and DEC-020 through DEC-026; BR-024.

### FR-030 — Validated operator restore

The system shall restore only after candidate validation, explicit operator confirmation and a recoverable safety backup.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Invalid candidates leave live data intact; stop writers, verify restored ownership/figures, invalidate sessions and pause outbound jobs before reviewed resumption.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-007A, TASK-007B, TASK-020; US-020; UC-015; TC-030, TC-034, TC-046, TC-068.
- **Source:** Charter D10 and DEC-020 through DEC-026; BR-024.

### FR-031 — Private CSV export

The system shall export only the authenticated User's exact records and relevant metadata.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** No other user, credentials or tokens appear; neutralize spreadsheet formulas; CSV is not a disaster-recovery backup.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-007B; US-020; UC-016; TC-031, TC-058.
- **Source:** Charter D8/D10 and DEC-020 through DEC-026; BR-024.

### FR-032 — Durable integration-independent core

The system shall persist committed core data and keep local financial workflows independent of Gemini and SMTP.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Committed observations survive restart; failed updates roll back; remote access depends on WAN/tunnel, but domain calculations require no external API.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-022A, TASK-003, TASK-004A2, TASK-020; US-001; UC-001; TC-032, TC-040.
- **Source:** Charter D2/D10 and DEC-020 through DEC-026; BR-023.

### FR-033 — Invite-only membership

The system shall permit account enrollment only through a valid invitation to the intended email.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Invitation tokens expire, are single-use and are stored as hashes; no public registration; revoked or used invitations fail.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-025B; US-022; UC-019; TC-054.
- **Source:** Charter D8 and DEC-020 through DEC-026; BR-024.

### FR-034 — Authentication and sessions

The system shall authenticate using Django password/session foundations, then complete email/password login and recovery for release.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Prototype uses a locally provisioned synthetic identity; release verifies email ownership, generic reset responses, revocation and secure cookies; suspended users lose access.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-025A, TASK-025B; US-023; UC-020; TC-055, TC-053.
- **Source:** Charter D8 and DEC-020 through DEC-026; BR-024.

### FR-035 — Admin/User privilege separation

The system shall allow Admin to manage membership without access to private financial workflows.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** No impersonation, arbitrary password setting or financial model admin; reset can only be sent to the existing verified address; protected email/role changes cannot enable takeover.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-026; US-024; UC-021; TC-057.
- **Source:** Charter D8 and DEC-020 through DEC-026; BR-024.

### FR-036 — Financial ownership isolation

The system shall enforce authenticated ownership on every financial read, write, cache, export, snapshot and scheduled job.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** User A and Admin cannot access B through identifiers, forms, downloads or jobs; cross-owner relationships fail atomically; no client-supplied owner override.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-003, TASK-026, TASK-019; US-025; UC-022; TC-057, TC-058.
- **Source:** Charter D8 and DEC-020 through DEC-026; BR-024.

### FR-037 — Manual balance and holding observations

The system shall let users enter their current cash balances and holding quantities without transaction-by-transaction entry.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** An initial observation establishes starting wealth, not a contribution; validate exact nonnegative amounts; investment totals derive from cash and holdings, never an added duplicate account total.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-004A1, TASK-004A2; US-026; UC-023; TC-059, TC-053, TC-068.
- **Source:** Charter D2 and DEC-020 through DEC-026; BR-002, BR-016, BR-023.

### FR-038 — Simple savings movements

The system shall optionally record external savings contributed/withdrawn alongside a balance update.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Save observations and annotations once atomically; contributions do not increase the entered balance again; internal tracked-account movements have zero net contribution; skipped classification is allowed.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-028; US-027; UC-024; TC-060, TC-067.
- **Source:** Charter D2 and DEC-020 through DEC-026; BR-017, BR-023.

### FR-039 — Honest change attribution

The system shall separate recorded wealth change, reported net contributions and supported residual change.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Without comparable endpoints and explicit interval-completeness confirmation, show attribution unknown; 10000 to 11200 with complete net contributions 1000 gives residual 200, never an automatic return percentage or investment-profit claim.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-028, TASK-010; US-028; UC-025; TC-061.
- **Source:** Charter D1/D2 and DEC-020 through DEC-026; BR-018.

### FR-040 — Optional financial profile

The system shall maintain optional self-reported monthly income/expense estimates and explicit review dates.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Omitting the profile does not block tracking or reports; estimated surplus is labeled; profile values never create balances or movements.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-030; US-029; UC-026; TC-062.
- **Source:** Charter D9 and DEC-020 through DEC-026; BR-021.

### FR-041 — Monthly schedule preferences

The system shall allow each User to choose a monthly reporting schedule in their timezone.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Schedules require explicit enablement; schedule edits affect future occurrences and do not overwrite earlier reports; local month boundaries are used.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-032; US-030; UC-027; TC-063.
- **Source:** Charter D7 and DEC-020 through DEC-026; BR-022.

### FR-042 — Generic reminder email

The system shall send a reminder before the configured report occurrence to the verified User email.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Subject/body/link contain no financial figures, goal or account names, attachments or bearer access to reports; email failure cannot block reporting.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-033; US-030; UC-027; TC-064, TC-045.
- **Source:** Charter D7 and DEC-020 through DEC-026; BR-022, BR-024.

### FR-043 — Authenticated saved monthly reports

The system shall generate and store a private report for the previous local calendar month even without recent updates.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Show missing/stale inputs and profile review dates; report reads require owner authentication; regeneration creates a new revision and no automatic Gemini call.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-031, TASK-032; US-031; UC-028; TC-066, TC-063.
- **Source:** Charter D7 and DEC-020 through DEC-026; BR-019, BR-021, BR-022, BR-024.

### FR-044 — Immutable snapshots

The system shall store the exact source versions, values and limitations used by wealth snapshots and saved reports.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Concurrent edits cannot create mixed-version snapshots; record period/as-of time, generated time, coverage, calculation version and revision; no silent historical replacement.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-010, TASK-031; US-011, US-031; UC-008, UC-028; TC-069.
- **Source:** Charter D1/D7 and DEC-020 through DEC-026; BR-019, BR-023.

### FR-045 — Sanitized system health

The system shall expose operational health and account administration to Admin without financial contents.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Show service status and sanitized job/backup failures; no balances, holdings, financial filenames, report bodies, prompts or per-user wealth totals.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-026, TASK-020; US-024; UC-021; TC-073.
- **Source:** Charter D8 and DEC-020 through DEC-026; BR-024.

### FR-046 — CI verification

The system shall run repository checks and applicable synthetic tests in GitHub Actions.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** CI uses no production data or deployment credentials, tests PostgreSQL behavior when introduced, and does not auto-deploy.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-023; US-032; UC-029; TC-070.
- **Source:** Charter D10 and DEC-020 through DEC-026; BR-024.

### FR-047 — Controlled deployment

The system shall document a reviewed, manually authorized deployment to Pi 5 (8 GB), CasaOS, Docker Compose and Cloudflare Tunnel.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Verify ARM64/runtime/images, persistence, restart, HTTPS/proxy settings, private database access and rollback before release; no workflow or plan grants deployment authority.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-024, TASK-020, TASK-021; US-032; UC-029; TC-044, TC-065.
- **Source:** Charter D6/D10 and DEC-020 through DEC-026; BR-024.

### FR-048 — Goal account links

The system shall link complete owned accounts to goals without reserving cash.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Database and service checks prevent an account funding two active goals; closure releases links atomically; no withdrawal restrictions.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-029; US-021; UC-018; TC-071.
- **Source:** Charter D3 and DEC-020 through DEC-026; BR-020.

### FR-049 — Observation revisions

The system shall correct manual observations while preserving their earlier values and provenance.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** A revision records its original and reason; historical snapshots stay unchanged; stale concurrent edits fail; no immutable transaction-ledger subsystem is required.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-004A2, TASK-004B, TASK-008B; US-026; UC-023; TC-059, TC-067.
- **Source:** Charter D2 and DEC-020 through DEC-026; BR-016, BR-019, BR-023.

### FR-050 — Freshness and review indicators

The system shall track observation dates, recording dates and explicit profile review dates independently.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** Viewing a page never refreshes data; confirming unchanged information is explicit; missing/stale data stays visible in dashboards, goals and reports.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-008A, TASK-010, TASK-030, TASK-031; US-009, US-029, US-031; UC-008, UC-026, UC-028; TC-072, TC-062.
- **Source:** Charter D1/D7/D9 and DEC-020 through DEC-026; BR-013, BR-021.

### FR-051 — Required Admin MFA

The system shall require second-factor enrollment, challenge and safe recovery for application Admin.

- **Priority / release:** Must / MVP
- **Rationale:** Support the approved savings/wealth scope and privacy boundaries.
- **Acceptance criteria:** No Admin operations before MFA; lost-factor recovery is controlled and invalidates relevant sessions; prototype synthetic login is explicitly not this release acceptance.
- **Dependencies:** Applicable ownership/currency prerequisites and task DAG in the backlog; no deferred ledger or reservation dependency.
- **Trace:** TASK-027; US-024; UC-021; TC-056.
- **Source:** Charter D8 and DEC-020 through DEC-026; BR-024.

## Retained requirements outside the MVP

These identifiers are not recycled. Their original behavior remains at baseline `5052b5b`; they require future approval before implementation.

| ID | Original requirement | Disposition / MVP successor |
|---|---|---|
| FR-006 | Holding transactions | Deferred ledger/reservations; simplified observations, movements and linked goals use FR-037/038/039/048. |
| FR-007 | Income recording | Deferred ledger/reservations; simplified observations, movements and linked goals use FR-037/038/039/048. |
| FR-008 | Expense recording | Deferred ledger/reservations; simplified observations, movements and linked goals use FR-037/038/039/048. |
| FR-009 | Record correction and deletion | Deferred ledger/reservations; simplified observations, movements and linked goals use FR-037/038/039/048. |
| FR-010 | Account transfers | Deferred ledger/reservations; simplified observations, movements and linked goals use FR-037/038/039/048. |
| FR-013 | Monthly cash-flow reporting | Deferred ledger/reservations; simplified observations, movements and linked goals use FR-037/038/039/048. |
| FR-017 | Savings reservations | Deferred ledger/reservations; simplified observations, movements and linked goals use FR-037/038/039/048. |
| FR-025 | Authorized Telegram destination | Deferred Telegram; FR-041/042/043 are distinct new capabilities. |
| FR-026 | Scheduled Telegram summaries | Deferred Telegram; FR-041/042/043 are distinct new capabilities. |
| FR-027 | Goal reminders and updates | Deferred Telegram; FR-041/042/043 are distinct new capabilities. |
| FR-028 | Notification preferences | Deferred Telegram; FR-041/042/043 are distinct new capabilities. |

## Non-functional requirements

### NFR-001 — Authenticated network boundary

- **Priority:** Must for MVP (provider-specific Gemini checks later).
- **Acceptance criteria:** Prototype is loopback-only with synthetic data. Release uses HTTPS tunnel ingress, private origin/database, validated host/proxy/CSRF settings and application authentication; tunnel admission alone grants no rights.
- **Verification:** TC-053, TC-065; TASK-022A, TASK-026, TASK-020.

### NFR-002 — Secrets and private records

- **Priority:** Must for MVP (provider-specific Gemini checks later).
- **Acceptance criteria:** Keep credentials, tokens, financial records, exports and backups outside Git and sanitized logs; restrict mounted data and secret-file access.
- **Verification:** TC-038; TASK-022B, TASK-003, TASK-020.

### NFR-003 — External privacy

- **Priority:** Must for MVP (provider-specific Gemini checks later).
- **Acceptance criteria:** Generic email contains no financial details; later Gemini requires exact one-call consent; Cloudflare transit and SMTP metadata dependencies are documented.
- **Verification:** TC-036, TC-049, TC-064; TASK-033, TASK-014, TASK-015.

### NFR-004 — Simple usable interface

- **Priority:** Must for MVP (provider-specific Gemini checks later).
- **Acceptance criteria:** Server-rendered Django templates provide clear navigation, readable account cards, understandable labels/units, an intuitive creation form, preserved valid input and accessible error/empty/success states. Prototype owner can sign in, create an account and find its balance using page guidance alone.
- **Verification:** TC-039, TC-053; TASK-022A, TASK-004A1, TASK-019.

### NFR-005 — Durability and atomicity

- **Priority:** Must for MVP (provider-specific Gemini checks later).
- **Acceptance criteria:** Committed data survives restart; related observations, movements, revisions and submission guards commit together or not at all.
- **Verification:** TC-040, TC-067; TASK-003, TASK-004A2, TASK-028.

### NFR-006 — Modular maintainability

- **Priority:** Must for MVP (provider-specific Gemini checks later).
- **Acceptance criteria:** Pure financial calculations accept explicit dates and run without Django models, UI imports, network access or provider credentials.
- **Verification:** TC-041; TASK-002, TASK-022B, TASK-014.

### NFR-007 — Measured Pi performance

- **Priority:** Must for MVP (provider-specific Gemini checks later).
- **Acceptance criteria:** Target 10 invited users and 3 concurrent active sessions; proposed fixture 10000 observations, 200 holdings and 20 goals per user. Proposed warmed p95 calculation/read <=2 s and ordinary write <=1 s, excluding network/browser; approve thresholds before measurement on the Pi.
- **Verification:** TC-042; TASK-024, TASK-019.

### NFR-008 — Integrity and ownership

- **Priority:** Must for MVP (provider-specific Gemini checks later).
- **Acceptance criteria:** Enforce exact values, owned references, version checks and unique active goal links for all entry points; competing updates cannot lose changes or duplicate movements.
- **Verification:** TC-043, TC-058, TC-067, TC-071; TASK-003, TASK-029, TASK-028.

### NFR-009 — Reproducible environments

- **Priority:** Must for MVP (provider-specific Gemini checks later).
- **Acceptance criteria:** Maintain separate loopback prototype and intended ARM64 Compose release procedures. CasaOS/Docker/OS/image compatibility remains later verification, not claimed support.
- **Verification:** TC-044; TASK-024, TASK-020, TASK-021.

### NFR-010 — Bounded external failures

- **Priority:** Must for MVP (provider-specific Gemini checks later).
- **Acceptance criteria:** SMTP and later Gemini failures are bounded, redacted and cannot block core records or deterministic reports; ambiguous email attempts are not blindly resent. Proposed 15 s timeout needs review.
- **Verification:** TC-045, TC-064; TASK-033, TASK-014.

### NFR-011 — Recoverability

- **Priority:** Must for MVP (provider-specific Gemini checks later).
- **Acceptance criteria:** Validate operator backups/restores independently; preserve live data on invalid restore and retain rollback path. Define recovery point/retention and approve measured targets before real data.
- **Verification:** TC-034, TC-046; TASK-007A, TASK-007B, TASK-020.

### NFR-012 — Exact numeric correctness

- **Priority:** Must for MVP (provider-specific Gemini checks later).
- **Acceptance criteria:** Use Decimal and integer minor units; reject nonfinite values, excess precision and overflow; final chart floats never feed persistence or financial calculations.
- **Verification:** TC-035, TC-047; TASK-002, TASK-003, TASK-008A.

### NFR-013 — Account and session security

- **Priority:** Must for MVP (provider-specific Gemini checks later).
- **Acceptance criteria:** Use standard password/session protections, throttling, invitation/reset expiry and revocation, User isolation and required Admin MFA; no application-admin superuser bypass. All are mandatory before real users or sensitive data.
- **Verification:** TC-054, TC-055, TC-056, TC-057, TC-058; TASK-025B, TASK-026, TASK-027, TASK-019.

## M-009 Early Working Prototype acceptance

| Check | Acceptance | Requirement scope | Executable leaves |
|---|---|---|---|
| P1-01 | Start Django locally on loopback with synthetic data and a visible development banner; no PostgreSQL/cloud/deployment prerequisite. | FR-001, FR-032; NFR-001 | TASK-022A |
| P1-02 | Use a locally provisioned synthetic identity with standard Django hashing, sessions, login/logout and CSRF; anonymous protected-page access fails. | FR-034; NFR-013 scoped foundations only | TASK-025A |
| P1-03 | Clear Dashboard/Accounts navigation, active-page indication, readable account cards showing name/currency/balance, understandable empty state and a visible create-account action. | FR-003, FR-037; NFR-004 | TASK-022A, TASK-004A1 |
| P1-04 | Intuitive labeled account-creation form accepts exact nonnegative synthetic opening balance, explains errors, preserves valid input and displays a clear success outcome. No frontend framework/SPA. | FR-003, FR-037; NFR-004, NFR-012 scoped input checks | TASK-004A1 |
| P1-05 | Saved account/balance survives refresh and restart; synthetic opening is not recorded as new savings; no external call or public exposure. | FR-032, FR-037; NFR-005 scoped persistence | TASK-004A1 |
| P1-06 | Record focused tests and owner demonstration for sign-in, navigation, create, cards and logout, including desktop/narrow view readability. No real-user, financial privacy, MFA or production claim. | NFR-004; TC-039, TC-053 | TASK-022A, TASK-025A, TASK-004A1 |

TC-053 verifies the complete prototype; TC-039 verifies its usability subset. The 8+4+4 hours are part of the 264-hour baseline. Partial TC-039/FR/NFR evidence must be reported by scenario; it never satisfies full release security, recovery or owner acceptance.

## M-001A wealth dashboard and basic recovery acceptance

| Check | Acceptance | Evidence planned |
|---|---|---|
| W1-01 | Authenticated synthetic PostgreSQL account/holding observations and dated manual prices yield exact qualified totals, with clear account cards. | TC-059, TC-068 |
| W1-02 | Preserve missing/stale flags, owned references, revision history, atomic update/replay and restart behavior. | TC-040, TC-043, TC-067, TC-072 |
| W1-03 | A validated operator backup/restore with safety copy preserves ownership and exact wealth; invalid input leaves live data intact. | TC-034, TC-046, TC-068 |
| W1-04 | Record synthetic owner demonstration and limitations; no real-user/data admission before M-007. | TC-068 and owner review |

The old M1A-01–M1A-08 checks belonged to DEC-015's SQLite/Streamlit ledger profile. They are superseded by P1-01–P1-06 and W1-01–W1-04, not marked passed. Their original text and TC-052 remain historical.

## Financial and operational business rules

| ID | Status | Rule |
|---|---|---|
| BR-001 | Current | One reporting currency/scale per User, fixed after financial data exists; manually price foreign units in it. |
| BR-002 | Amended; rounding proposed under OQ-002 | Latest eligible balance/quantity observations and dated prices determine value. Proposed half-even rounding per holding, then sum; cash in reporting currency has price one. No negative holdings. |
| BR-003 | Deferred | Original actual income-minus-expenses and savings-rate rule requires the deferred transaction ledger. Profile estimates do not satisfy it. |
| BR-004 | Deferred | Original equal/opposite transfer postings are deferred. MVP internal-movement classification follows BR-017. |
| BR-005 | Current | Tracked wealth is priced cash/holdings once; liabilities are excluded; missing prices qualify the subtotal. Goal links and profile estimates add no assets. |
| BR-006 | Deferred | Original trade settlement, fees and transaction posting policy is outside MVP. |
| BR-007 | Deferred | Original cash-reservation bounds and spending restrictions are outside MVP. |
| BR-008 | Superseded by BR-020 | Original reservation-derived goal progress is replaced by linked account value. |
| BR-009 | Retained proposal under OQ-002 | Monthly opportunities include current and deadline month: 12*(deadline.year-today.year)+deadline.month-today.month+1 when not overdue. Ceiling-to-minor-unit of remaining/opportunities; funded zero; overdue underfunded unavailable. This is an indicative plan. |
| BR-010 | Superseded for MVP by BR-016 and BR-019 | Original reversal/replacement ledger corrections and historical-balance validation are deferred. |
| BR-011 | Exactness mandatory; limits proposed under OQ-002 | Reject NaN/infinity, excess fractional monetary digits and signed-64-bit minor-unit overflow. Proposed quantity/price precision <=8 fractional digits; use exact Decimal multiplication. Presentation-only float conversions never feed back. |
| BR-012 | Later Gemini | AI is untrusted explanation, never authoritative arithmetic or write input. Explicit exact one-call consent; no autonomous financial tools or personalized security buy/sell recommendations. |
| BR-013 | Amended; thresholds proposed under OQ-003 | Retain separate quantity/balance observation dates and price dates; missing is not zero. Proposed stale prices >7 calendar days and profile review >30 days. Page views/carry-forward do not refresh timestamps. |
| BR-014 | Deferred | Original approved-field Telegram notification rule is deferred. Email privacy follows BR-022. |
| BR-015 | Deferred | Original Telegram retry/catch-up policy is retained historically. Revised report/email policy is BR-022 pending OQ-005. |
| BR-016 | Current; revision details OQ-002 | User supplies dated balance/quantity observations; initial observations establish a baseline, not new savings. Keep effective and recorded times and original revisions. Removing a holding is a zero observation, not physical deletion of history. |
| BR-017 | Current | Movement amount is positive reporting-currency minor units with contribution/withdrawal/internal kind and effective date. Net external contributions = contributions - withdrawals; internal movements across tracked accounts =0. An annotation explains an observation and never adds to its balance. In-kind additions require a user-supplied amount or make attribution unknown. |
| BR-018 | Current | Recorded wealth change requires comparable endpoint coverage. Supported residual = end - start - net external contributions only with explicit interval-completeness assertion and adequate dated valuations. Missing classification, stale/incomplete endpoints, changed coverage or revised inputs invalidate attribution. Residual includes other effects and is not investment profit, TWR/IRR or a return percentage. |
| BR-019 | Current | Snapshots/reports freeze source versions, as-of/period, generation time, exact values, currency, coverage, warnings and calculation version. Corrections can produce a new revision; never silently overwrite a saved snapshot or backfill a past date with a newer observation. |
| BR-020 | Current | A whole owned account links to at most one active goal. Progress value=sum(linked account values), remaining=max(target-progress,0), bar caps at 100% with excess shown separately. No reserved balance or withdrawal block; incomplete value qualifies progress. Closure ends links without changing wealth. |
| BR-021 | Current | Profile income/expense values are optional monthly estimates; estimated surplus=estimated income-estimated expense, labeled as such. They never create actual savings/movements. Explicit save/review-unchanged updates review time; views do not. |
| BR-022 | Proposed operations under OQ-005 | Previous local calendar month is the report period. Report generation is independent of input freshness and email. Proposed monthly day 1-28/time, reminder lead 3 days, latest due occurrence after downtime, first repeated DST instant/next valid nonexistent instant. Unique occurrence claims prevent duplicate reports; definite email failure may retry up to 3 times, ambiguous send requires review. No financial content or bearer report link in email. |
| BR-023 | Current; replay mechanism OQ-007 | Save related observations, movements and submission guard in one database transaction. Same owner/key/payload returns the original result; changed payload rejects. Version checks prevent lost updates. No network call under write locks; snapshot reads are coherent. |
| BR-024 | Current | Owner identity is server-derived. Admin has no financial access, impersonation or account-takeover path; Users cannot choose another owner. Operator backups are outside Admin UI. Release gating applies before real users/sensitive data. CI and deployment plans never grant operational authorization. |

## Acceptance and open gates

Recorded wealth change and reported net contributions remain distinct. Only comparable complete endpoints and an explicit version-bound completeness assertion support a residual; otherwise attribution is unknown. No balance increase alone establishes investment performance.

OQ-002/003/005/006/007/008/009/010/011 retain task-specific gates in the [Decision Log](../DECISION_LOG.md). The owner approved product direction and estimates, not every numeric threshold, library, deployment version or recovery policy. [RTM](RTM.md) maps current and retired requirements; [Test Plan](../testing/TEST_PLAN.md) distinguishes historical TASK-001 evidence from planned execution.
