# Finance Tracker — Software Requirements Specification

Status: Draft specification with the M-001A acceptance profile approved under DEC-015 and runtime selection approved under DEC-017. DEC-018 authorizes TASK-001 only under the documented requirements, architecture, and acceptance criteria; execution is explicitly held and the remaining baseline is not approved by that decision. Financial calculations, database schemas, asset management, Gemini features, and Telegram features are outside TASK-001. Other proposed technical policies retain their review status. No application behavior is implemented or verified.
Baseline: [Project Charter](../CHARTER.md), read in full on 2026-11-05, and confirmed owner choices in [DECISION_LOG](../DECISION_LOG.md). This is an IEEE 29148-inspired structure, not a claim of standards certification. The Charter remains proposed; drafting this SRS does not approve it.

## 1. Introduction

### Purpose and audience

Specify testable behavior for the owner/developer, future contributors, and acceptance reviewer of Finance Tracker. Provide the basis for design, backlog, and planned tests before application development.

### Scope and product overview

A lightweight self-hosted, single-user financial dashboard manages manually recorded assets, income, expenses, savings goals, and local data. It offers optional Gemini explanations and optional Telegram notifications. Approved M-001A delivers the first working opening-only dashboard at 32 cumulative hours / end of Week 4, with essential persistence, validation, tests and recovery. The first usable complete core remains M-004 at 92 hours and includes financial tracking, dashboards, goals, backup/restore, and export. The complete Charter release also delivers Gemini and Telegram, with no requirement to enable them during ordinary use.

Excluded: multi-user management, banking integration, automatic trading/rebalancing, mobile apps, public cloud hosting, live market trading, wallet connections, and regulated personalized investment advice. Automated prices, advanced multi-currency analysis, inflation adjustments, forecasting, recurring entries, advanced analytics, AI categorization, and responsive-layout improvements are future candidates, not release commitments.

### Definitions and terminology

| Term | Meaning |
|---|---|
| Personal User | The single owner operating the dashboard and receiving authorized notifications. |
| Account | A logical location of holdings, not a bank connection or application login. |
| Asset | A unit-defined cash, currency, gold, stock, or fund instrument. |
| Base cash | Cash in the dataset reporting currency, with unit price fixed at one. |
| Reporting currency | One explicitly selected currency used for all totals, prices, and monetary amounts. |
| Posting / holding | A signed quantity change for an account/asset; a holding is the sum of effective postings. |
| Effective transaction | A posted event including any correcting/reversing events that determine the current restated history. |
| Reservation / allocation | An earmark of existing base cash for a goal; it creates no money or ownership transfer. |
| Priced subtotal | Value of holdings with available prices; incomplete when any positive holding lacks a price. |
| Asset-only net-worth estimate | Total tracked assets; explicitly excludes liabilities, which are not recorded. |
| Must / Should / Could | Release obligation / desirable nonblocking capability / optional enhancement. Must integrations can be disabled at runtime. |

## 2. Overall description

### Product perspective and users

A new modular Python monolith, with Streamlit presentation, SQLite persistence, Pandas/Plotly reporting, and isolated external API adapters. No legacy application or executable test suite exists. The owner, developer, and primary user are initially one person, comfortable with local startup and manual finance entry but not expected to understand database internals for ordinary workflows. Gemini and Telegram are supporting systems, not human users.

### Operating environment

Run on a personal computer/local server with a local-disk database. DEC-017 approves the current Linux environment, Python 3.14.x with locally installed 3.14.8 as the initial target, and venv, pip, and pytest, resolving OQ-004's runtime selection. Dependency compatibility and exact compatible dependency versions remain unverified TASK-001 work; report incompatibilities rather than silently changing Python or architecture. Access is loopback by default and optionally from explicitly trusted LAN devices. Internet is needed only for enabled external integrations. The optional notification command is invoked by a host scheduler; no always-on cloud service is required.

### Constraints

Use the Charter stack, minimize costs, keep core workflows offline, keep secrets and financial records outside Git, and keep complexity appropriate for a solo developer. No application login is planned: admitted devices can read and modify the dataset. Network restrictions are required before enabling LAN binding; this is not a public-internet deployment.

### Assumptions and dependencies

Confirmed choices DEC-002 through DEC-008 govern currency, liabilities, access, goals, consent, capacity, and Telegram scope. ASM-001 through ASM-005 cover owner-supplied credentials, host availability, local disk, manual backups, and local date/time. These are not confirmed product requirements. Proposed schema, rounding, stale-price, recovery, and replay policies retain their existing reviews under DEC-010 through DEC-014, DEC-016, and OQ-002/003/005/006/007. DEC-017's runtime approval and DEC-018's limited TASK-001 authorization do not resolve those policies or approve the remainder of OQ-001. API availability, quota, pricing, and bot access are external dependencies; no account is created by this project.

## 3. Functional requirements

All requirements below are planned. Priority is relative to the complete Charter release, not a claim of implementation. Dependencies name prerequisite capabilities, not mandatory code initialization order.

### FR-001 — Local configuration

The system shall load deployment paths, integration enablement, and credentials from environment variables, with external integrations disabled by default.

- **Priority:** Must
- **Rationale:** Keep local deployment reproducible without exposing secrets.
- **Acceptance criteria:** Without API credentials, the core launches with both adapters disabled; enabling an adapter with missing credentials produces a redacted configuration error and leaves the core usable.
- **Dependencies:** None
- **Source:** Charter §4.1 Data Management; §9; §11.

### FR-002 — Reporting currency

The system shall require one reporting currency and its minor-unit scale before the first financial record, and reject changes after financial records exist.

- **Priority:** Must
- **Rationale:** Avoid mixing incomparable amounts or silently reinterpreting historical records.
- **Acceptance criteria:** A fresh dataset requires an explicit currency selection; later currency changes are rejected without modifying records; foreign-currency units can be priced manually in the reporting currency.
- **Dependencies:** FR-001
- **Source:** Charter §4.1 Asset Management; owner decision DEC-002.

### FR-003 — Account management

The system shall allow the user to create, rename, view, archive, and delete unused logical accounts.

- **Priority:** Must
- **Rationale:** Represent locations of manually tracked holdings without banking integrations.
- **Acceptance criteria:** Account names are unique ignoring case; an account with postings or allocations cannot be physically deleted; archiving requires zero holdings and no allocations.
- **Dependencies:** FR-002
- **Source:** Charter §2; §12 financial records.

### FR-004 — Asset management

The system shall allow the user to create, edit, view, archive, and delete unused asset definitions for cash, currencies, gold, stocks, and funds.

- **Priority:** Must
- **Rationale:** Cover all Charter asset classes.
- **Acceptance criteria:** Each asset records a name, type, unit, and optional quoted currency; duplicate account holdings are aggregated by asset ID; referenced assets cannot be physically deleted; base cash has a fixed unit value of one.
- **Dependencies:** FR-002, FR-003
- **Source:** Charter §4.1 Asset Management; §12.

### FR-005 — Manual price history

The system shall let the user record and correct dated manual unit prices in the reporting currency for non-base-cash assets.

- **Priority:** Must
- **Rationale:** Support initial portfolio valuation without market feeds.
- **Acceptance criteria:** Positive finite prices and effective dates are validated; superseded observations remain auditable; correcting a price recomputes affected reports; future-dated prices are rejected.
- **Dependencies:** FR-004
- **Source:** Charter §4.1 Asset Management; §10.

### FR-006 — Holding transactions

The system shall record opening holdings, manual acquisitions, disposals, and quantity adjustments with dated posting history.

- **Priority:** Must
- **Rationale:** Connect portfolio quantities and cash movements without inventing investment income.
- **Acceptance criteria:** A purchase of 200 reduces base cash by 200 and adds the purchased quantity atomically; a sale records its cash proceeds; opening balances and adjustments are excluded from income and expenses; insufficient holdings are rejected. One opening registration saves its new asset definition, opening posting and optional initial price atomically; invalid/failing submissions leave no partial records. Replaying one logical submission cannot duplicate it, including after restart; conflicting key reuse is rejected. The exact replay mechanism remains DEC-016/OQ-007.
- **Dependencies:** FR-003, FR-004
- **Source:** Charter §4.1 Asset Management; §12.

### FR-007 — Income recording

The system shall record dated income with a positive base-currency amount, account, category, and optional note.

- **Priority:** Must
- **Rationale:** Provide accurate monthly income.
- **Acceptance criteria:** Valid income increases account base cash once; missing account, zero/negative amount, excess monetary precision, and future dates are rejected without partial writes.
- **Dependencies:** FR-006
- **Source:** Charter §3 objective 2; §12.

### FR-008 — Expense recording

The system shall record dated expenses with a positive base-currency amount, account, category, and optional note.

- **Priority:** Must
- **Rationale:** Provide accurate spending and protect reserved savings.
- **Acceptance criteria:** Valid expense reduces base cash once; an expense exceeding unreserved cash is rejected with a release-allocation instruction; invalid inputs leave balances unchanged.
- **Dependencies:** FR-006
- **Source:** Charter §3 objective 2; §12.

### FR-009 — Record correction and deletion

The system shall allow the user to correct or logically delete financial transactions while preserving the original audit history.

- **Priority:** Must
- **Rationale:** Meet edit/delete success criteria without erasing provenance.
- **Acceptance criteria:** A correction creates linked replacement/reversal records in one transaction; deletion reverses the effective record; repeated deletion is rejected; changed historical balances and reservations are revalidated before commit.
- **Dependencies:** FR-006, FR-007, FR-008
- **Source:** Charter §12 assets and transactions CRUD.

### FR-010 — Account transfers

The system shall move base-currency cash between two distinct accounts as one atomic transfer.

- **Priority:** Must
- **Rationale:** Prevent transfers from being counted as income or expenses.
- **Acceptance criteria:** A 100 transfer creates equal source/destination cash changes; total assets and monthly income/expense remain unchanged; self-transfer and insufficient unreserved funds are rejected.
- **Dependencies:** FR-003, FR-006
- **Source:** Charter §2 multiple accounts; derived BR-004.

### FR-011 — Valuation completeness

The system shall identify missing and outdated prices with observation dates on portfolio totals and charts.

- **Priority:** Must
- **Rationale:** Avoid misleading totals from unknown or stale prices.
- **Acceptance criteria:** Any positive unpriced holding yields an incomplete priced subtotal, never an assumed zero value; a stale price remains in the subtotal with a warning; the stale threshold is configurable.
- **Dependencies:** FR-005, FR-006
- **Source:** Charter §10 incorrect portfolio valuation.

### FR-012 — Total assets and net-worth estimate

The system shall calculate total assets and an explicitly labeled asset-only net-worth estimate from current holdings and valid manual prices.

- **Priority:** Must
- **Rationale:** Provide the Charter dashboard while exposing the absence of liabilities.
- **Acceptance criteria:** For cash 1000 and an asset valued at 200, both figures equal 1200; the dashboard states liabilities are not tracked; goal reservations add nothing; incomplete prices qualify both figures.
- **Dependencies:** FR-011
- **Source:** Charter §4.1 Dashboard; owner decision DEC-003.

### FR-013 — Monthly cash-flow reporting

The system shall report monthly income, expenses, savings, and savings rate using effective financial transactions.

- **Priority:** Must
- **Rationale:** Make spending and saving measurable.
- **Acceptance criteria:** Income 300 and expenses 100 produce savings 200 and a 66.67% display rate; transfers and investments do not change these totals; zero/negative income produces an unavailable rate.
- **Dependencies:** FR-007, FR-008, FR-009, FR-010
- **Source:** Charter §4.1 Dashboard; §12.

### FR-014 — Asset distribution

The system shall show asset distribution by asset type with values consistent with the portfolio subtotal.

- **Priority:** Must
- **Rationale:** Explain portfolio composition.
- **Acceptance criteria:** Distribution values sum to the displayed priced subtotal; unknown holdings are listed separately; an empty or zero-value portfolio shows an empty state instead of misleading percentages.
- **Dependencies:** FR-011, FR-012
- **Source:** Charter §4.1 Dashboard.

### FR-015 — Historical trends

The system shall display historical asset values and monthly cash-flow trends using dated transactions and prices.

- **Priority:** Must
- **Rationale:** Support historical financial review.
- **Acceptance criteria:** Past dates use prices effective no later than that date; earlier dates without prices remain incomplete; corrections refresh affected periods; latest prices are not applied retroactively.
- **Dependencies:** FR-005, FR-009, FR-013
- **Source:** Charter §4.1 Dashboard.

### FR-016 — Savings goal management

The system shall create, edit, view, archive, and logically delete multiple goals with positive target amounts and target dates.

- **Priority:** Must
- **Rationale:** Represent distinct savings outcomes.
- **Acceptance criteria:** Two simultaneous goals can be saved; invalid targets are rejected; past deadlines are allowed and labeled overdue when underfunded; deleting or archiving a goal explicitly releases its active reservations atomically.
- **Dependencies:** FR-002
- **Source:** Charter §4.1 Financial Goals.

### FR-017 — Savings reservations

The system shall allocate and release existing base-currency cash to goals without moving or duplicating funds.

- **Priority:** Must
- **Rationale:** Prevent double-counting across goals.
- **Acceptance criteria:** With cash 1000, reserving 700 leaves 300 available; another reservation of 400 is rejected; reservations across goals never exceed each source account cash balance; releases and cash edits preserve this invariant atomically.
- **Dependencies:** FR-006, FR-016
- **Source:** Charter §4.1 Financial Goals; owner decision DEC-005.

### FR-018 — Goal progress

The system shall show reserved cash, remaining target, and completion percentage for each goal.

- **Priority:** Must
- **Rationale:** Make progress visible without treating goals as extra assets.
- **Acceptance criteria:** Reserved 250 against target 1000 gives 25% and remaining 750; progress bars cap at 100% while excess funding is shown separately; released funds immediately reduce progress.
- **Dependencies:** FR-017
- **Source:** Charter §4.1 Financial Goals.

### FR-019 — Required contributions

The system shall calculate a deterministic required monthly contribution from the unfunded target and remaining monthly contribution opportunities.

- **Priority:** Must
- **Rationale:** Support planning independently of Gemini.
- **Acceptance criteria:** For remaining target 900 and three opportunities, the contribution is 300; funded goals return zero; overdue underfunded goals show overdue with no monthly amount; amounts round upward to a minor unit.
- **Dependencies:** FR-018
- **Source:** Charter §4.1 Financial Goals.

### FR-020 — Spending explanations

The system shall offer user-initiated Gemini explanations of approved spending aggregates.

- **Priority:** Must
- **Rationale:** Explain patterns without delegating financial arithmetic.
- **Acceptance criteria:** A valid approved monthly aggregate can be explained; all displayed financial totals retain their deterministic source values; an unavailable API yields a recoverable error.
- **Dependencies:** FR-013, FR-024
- **Source:** Charter §4.1 AI Integration; D4.

### FR-021 — Goal feasibility explanations

The system shall offer user-initiated Gemini explanations of deterministic savings-goal projections.

- **Priority:** Must
- **Rationale:** Explain the gap between required contributions and recorded savings.
- **Acceptance criteria:** The request includes approved target/progress/contribution summaries; missing history is disclosed; Gemini cannot change the target, reservation, or calculated monthly contribution.
- **Dependencies:** FR-019, FR-024
- **Source:** Charter §4.1 AI Integration; D4.

### FR-022 — Natural-language summaries

The system shall provide user-initiated Gemini summaries of approved financial aggregates.

- **Priority:** Must
- **Rationale:** Make calculated summaries easier to understand.
- **Acceptance criteria:** A summary is labeled AI-generated and separate from computed figures; portfolio completeness warnings accompany the context; generated text creates no financial records.
- **Dependencies:** FR-012, FR-013, FR-024
- **Source:** Charter §4.1 AI Integration; D4.

### FR-023 — Financial questions

The system shall allow the user to submit a financial question to Gemini with explicitly approved context.

- **Priority:** Must
- **Rationale:** Support the Charter question workflow within an explanatory boundary.
- **Acceptance criteria:** The question and selected context appear in the preview; no arbitrary tools, SQL, trading, or financial-write capability is supplied to Gemini; the response is labeled explanatory.
- **Dependencies:** FR-024
- **Source:** Charter §4.1 AI Integration; §12.

### FR-024 — Per-request AI consent

The system shall preview the exact minimized summary and question before each Gemini transmission and require an explicit send action.

- **Priority:** Must
- **Rationale:** Make external disclosure deliberate.
- **Acceptance criteria:** Canceling the preview makes no API call; editing the question or financial context invalidates prior approval; approval permits one call and cannot be reused by a Streamlit rerun; generated context excludes tokens, account labels, and record notes; the exact user-typed question is visible for approval.
- **Dependencies:** FR-001
- **Source:** Charter §6 D4 approved summaries; §11; owner decision DEC-006.

### FR-025 — Authorized Telegram destination

The system shall send Telegram content only to the single explicitly configured and validated private-chat recipient.

- **Priority:** Must
- **Rationale:** Prevent financial reports reaching unauthorized chats.
- **Acceptance criteria:** Missing, group, mismatched, or unvalidated recipient configuration fails closed; a deliberate non-financial connection test confirms the destination; incoming commands are not processed and reveal no data.
- **Dependencies:** FR-001
- **Source:** Charter §4.1 Telegram; §11; owner decision DEC-008.

### FR-026 — Scheduled Telegram summaries

The system shall deliver enabled weekly or monthly deterministic financial summaries to the authorized recipient while the local runner is available.

- **Priority:** Must
- **Rationale:** Provide periodic reports without an external service dependency.
- **Acceptance criteria:** A configured due period creates one delivery record; rerunning an acknowledged period does not resend; a missed schedule sends at most the latest due period after restart; timeout ambiguity is surfaced.
- **Dependencies:** FR-013, FR-025, FR-028
- **Source:** Charter §4.1 Telegram; D5.

### FR-027 — Goal reminders and updates

The system shall send enabled goal reminders and progress updates through the authorized Telegram destination.

- **Priority:** Must
- **Rationale:** Keep savings goals visible outside the dashboard.
- **Acceptance criteria:** A configured reminder includes the selected goal progress, deadline, and deterministic contribution; duplicate runner invocations do not resend acknowledged occurrences; released/deleted goals do not generate stale updates.
- **Dependencies:** FR-018, FR-019, FR-025, FR-028
- **Source:** Charter §3 objective 5; §4.1 Telegram.

### FR-028 — Notification preferences

The system shall let the user enable, disable, and configure Telegram report/reminder schedules and approved content in the dashboard.

- **Priority:** Must
- **Rationale:** Keep financial sharing optional and predictable.
- **Acceptance criteria:** No scheduled financial message is enabled by default; configuration requires a timezone, recipient, content preview/approval, and chosen schedule; disabling a rule prevents new attempts, while a network request already in flight may complete and remains visible in delivery status.
- **Dependencies:** FR-025
- **Source:** Charter §4.1 Telegram; §11.

### FR-029 — Consistent local backup

The system shall produce a consistent local SQLite backup without including external credentials.

- **Priority:** Must
- **Rationale:** Reduce financial-data loss risk.
- **Acceptance criteria:** A completed backup opens independently and passes integrity checks; failed writes produce no success message or usable-looking partial backup; active writes cannot create a torn snapshot.
- **Dependencies:** FR-032
- **Source:** Charter §4.1 Data Management; §11.

### FR-030 — Validated restore

The system shall restore a supported local backup only after validation, explicit replacement confirmation, and a recoverable pre-restore backup.

- **Priority:** Must
- **Rationale:** Avoid destroying valid data during recovery.
- **Acceptance criteria:** Invalid/corrupt/unsupported backups leave the live dataset unchanged; application and runner writers are stopped before replacement; a supported round trip preserves balances, prices, goals, and history.
- **Dependencies:** FR-029
- **Source:** Charter §4.1 Data Management; §11.

### FR-031 — CSV export

The system shall export financial records, holdings/prices, goals, and allocations as documented CSV files.

- **Priority:** Must
- **Rationale:** Provide portable user-owned data.
- **Acceptance criteria:** Exports carry stable IDs, currency/scale, dates, and exact decimal text; credentials are excluded; spreadsheet-formula text is neutralized and documented; CSV is not advertised as a restore backup.
- **Dependencies:** FR-006, FR-016, FR-017
- **Source:** Charter §4.1 Data Management.

### FR-032 — Offline persistence

The system shall persist committed core records locally and keep financial tracking, dashboard, goals, backup, restore, and export usable without either external API.

- **Priority:** Must
- **Rationale:** Honor local-first operation and optional integrations.
- **Acceptance criteria:** After restart all committed records remain; disabled, unreachable, or unconfigured APIs do not block core reads/writes; a failed transaction leaves no partial postings or reservations.
- **Dependencies:** FR-001, FR-002
- **Source:** Charter §9 constraints; §12.

## 4. Non-functional requirements

All NFRs are Must release constraints. Numerical thresholds labeled proposed require owner review; their tests remain planned.

### NFR-001 — LAN access security

The deployment shall restrict dashboard access to explicitly trusted devices on a private network.

- **Priority:** Must
- **Rationale:** Protect accurate, private, maintainable local operation.
- **Acceptance criteria:** From an allowed device the dashboard is reachable; from a denied device it is blocked. Bind loopback by default, require explicit LAN binding/firewall setup, and document that allowed devices have full access without login.
- **Verification:** TC-037 in [TEST_PLAN](../testing/TEST_PLAN.md).

### NFR-002 — Secrets and local records

Secrets and financial files shall remain outside version control and sanitized application logs.

- **Priority:** Must
- **Rationale:** Protect accurate, private, maintainable local operation.
- **Acceptance criteria:** Synthetic .env, database, export, backup, and log files are ignored; repository/log inspection finds no seeded credentials, account notes, or financial prompts. OS permissions limit data paths to the owner.
- **Verification:** TC-038 in [TEST_PLAN](../testing/TEST_PLAN.md).

### NFR-003 — External privacy

External requests shall contain only user-approved minimized content.

- **Priority:** Must
- **Rationale:** Protect accurate, private, maintainable local operation.
- **Acceptance criteria:** Canceled Gemini requests cause zero calls; generated context contains no secrets, account labels, or free-form record notes; the verbatim question is separately shown for approval, without claiming automatic detection of personal details typed by the user; Telegram sends only approved report fields to the allowlisted private chat.
- **Verification:** TC-036, TC-048, TC-049 in [TEST_PLAN](../testing/TEST_PLAN.md).

### NFR-004 — Usability

Common financial workflows shall expose units, validation errors, save outcomes, and clear empty states.

- **Priority:** Must
- **Rationale:** Protect accurate, private, maintainable local operation.
- **Acceptance criteria:** Proposed threshold: the owner completes income entry, a transfer, and a goal reservation on a populated fixture within three minutes each, following only field labels and help; validation preserves valid form values.
- **Verification:** TC-039 in [TEST_PLAN](../testing/TEST_PLAN.md).

### NFR-005 — Reliability

Committed records shall survive normal restart and failed multi-record operations shall be atomic.

- **Priority:** Must
- **Rationale:** Protect accurate, private, maintainable local operation.
- **Acceptance criteria:** Restart reproduces balances and allocations exactly; injected failure before commit changes no row in the logical operation. Host/disk failure recovery depends on the last valid backup; no zero-data-loss promise.
- **Verification:** TC-032, TC-040, TC-051, TC-052 in [TEST_PLAN](../testing/TEST_PLAN.md).

### NFR-006 — Maintainability

Business calculations shall be independently testable without Streamlit or external clients.

- **Priority:** Must
- **Rationale:** Protect accurate, private, maintainable local operation.
- **Acceptance criteria:** Domain modules import and run without UI/API dependencies; adapter failure tests use fakes; core calculations have no network or current-clock dependence unless a clock is explicitly supplied.
- **Verification:** TC-041 in [TEST_PLAN](../testing/TEST_PLAN.md).

### NFR-007 — Performance

Dashboard reads and ordinary financial writes shall remain usable at the initial dataset scale.

- **Priority:** Must
- **Rationale:** Protect accurate, private, maintainable local operation.
- **Acceptance criteria:** Proposed: on 2 CPU cores, 8 GB RAM, local SSD, 10,000 transactions, 200 assets, and 20 goals, 95% of 30 warmed dashboard calculations finish within 2 seconds and 95% of 30 single-operation writes within 1 second; exclude API latency and browser rendering.
- **Verification:** TC-042 in [TEST_PLAN](../testing/TEST_PLAN.md).

### NFR-008 — Data integrity

Relationships and cross-record financial invariants shall be enforced on every write path.

- **Priority:** Must
- **Rationale:** Protect accurate, private, maintainable local operation.
- **Acceptance criteria:** Foreign keys are enabled per connection; invalid references fail; two overlapping reservations cannot exceed available cash; negative holdings and invalid decimal representations are rejected; all dependent writes roll back together.
- **Verification:** TC-033, TC-043, TC-051, TC-052 in [TEST_PLAN](../testing/TEST_PLAN.md).

### NFR-009 — Local deployment

The documented local setup shall reproduce the core application without Gemini or Telegram credentials.

- **Priority:** Must
- **Rationale:** Protect accurate, private, maintainable local operation.
- **Acceptance criteria:** A clean supported Linux environment completes the documented setup, starts on loopback, persists a sample entry, and restarts successfully; no cloud-hosting account or paid API is required.
- **Verification:** TC-044, TC-052 in [TEST_PLAN](../testing/TEST_PLAN.md).

### NFR-010 — API failure handling

External calls shall have bounded timeouts and distinguish recoverable failure from financial-data failure.

- **Priority:** Must
- **Rationale:** Protect accurate, private, maintainable local operation.
- **Acceptance criteria:** Proposed timeout: 15 seconds per call. Interactive Gemini does not automatically retry; Telegram retries only transient definite failures, at most three attempts per occurrence, respecting Retry-After. Auth/config errors disable delivery with a redacted action message. Core writes remain available.
- **Verification:** TC-045 in [TEST_PLAN](../testing/TEST_PLAN.md).

### NFR-011 — Recovery

Backup and restore procedures shall protect the live dataset and expose the recovery point.

- **Priority:** Must
- **Rationale:** Protect accurate, private, maintainable local operation.
- **Acceptance criteria:** Supported backups pass integrity and relationship checks; corrupt restore attempts preserve live bytes; a stopped-writer restore is reversible from the pre-restore backup. Proposed recovery target: restore a fixture of 10,000 transactions in 10 minutes using the written procedure; recovery point is last successful user backup.
- **Verification:** TC-029, TC-030, TC-034, TC-046, TC-052 in [TEST_PLAN](../testing/TEST_PLAN.md).

### NFR-012 — Numeric correctness

Financial calculations shall use exact decimal/integer arithmetic and explicit rounding policies.

- **Priority:** Must
- **Rationale:** Protect accurate, private, maintainable local operation.
- **Acceptance criteria:** No binary floats enter persistence or business arithmetic; 0.10 + 0.20 equals 0.30; per-holding valuation rounds half-even to the reporting minor unit, totals sum those values, required contributions round upward, and out-of-range values fail before persistence.
- **Verification:** TC-035, TC-047, TC-052 in [TEST_PLAN](../testing/TEST_PLAN.md).

## M-001A acceptance profile — approved scope, planned verification

DEC-015 approves the following **Must** milestone checks. They are scoped acceptance of existing requirements, not new FR IDs or proof that the broader FRs are complete. Full CRUD, trading, corrections, cash-flow reports, history, goals and integrations retain their later acceptance. M-004 remains at 92 hours. Specific rounding/precision/replay design proposals still require their recorded reviews.

| Check ID | Acceptance criterion | Related requirements | Planned verification |
|---|---|---|---|
| M1A-01 | Start the documented Streamlit application on localhost with no API keys or network dependency; choose/fix one reporting currency and scale before financial entries; show clear setup/empty states. | FR-001, FR-002, FR-032; NFR-001, NFR-002, NFR-009 | TC-001, TC-002, TC-038, TC-044 applicable local checks; TC-052 |
| M1A-02 | Create/select a basic account; manually register existing cash, currencies, gold, stocks and funds with declared units/quantities and optional initial base-currency prices; list the saved holdings, units, quantities, prices and outcomes. Registration is an opening, not a purchase or income event. | FR-003, FR-004, FR-006 | TC-003, TC-004, TC-006 opening checks; TC-052 |
| M1A-03 | Base cash is valued at one; deterministic exact arithmetic and reviewed rounding give 1200 for cash 1000 plus 10 units at 20. Show dated prices, per-holding values and total/qualified asset-only estimate. Unpriced positive holdings create an explicitly incomplete priced subtotal, never an assumed zero. Stale prices retain their value with a warning using the reviewed threshold. | FR-005, FR-011, FR-012; NFR-012 | TC-005, TC-011, TC-012, TC-035, TC-047 applicable checks; TC-052 |
| M1A-04 | Validate required fields, account/asset references, units, finite positive quantities/prices, monetary precision/bounds and nonfuture financial dates. Use SQLite foreign keys and one transaction for the new definition, opening posting and optional initial price. Injected failures/invalid inputs leave all pre-existing balances unchanged and no orphan/partial registration; never maintain a separate editable balance or store financial floats. | FR-002, FR-004, FR-005, FR-006, FR-032; NFR-005, NFR-008, NFR-012 | TC-040, TC-043, TC-047 opening checks; TC-051, TC-052 |
| M1A-05 | Restart and reopen the same SQLite dataset; committed asset definitions, postings, prices and exact total are retained. Interrupted/failed operations do not appear as committed holdings. | FR-032; NFR-005 | TC-032, TC-040, TC-044 applicable checks; TC-052 |
| M1A-06 | A rerun, double submission or retry of the same opening intent creates exactly one definition/opening/price set, including when its logical submission key is replayed after restart. Same-key different-payload reuse fails without mutation; a failed rolled-back attempt can be retried safely. Distinct explicitly new commands are not suppressed merely because values match. | FR-006, FR-032; NFR-005, NFR-008 | TC-051; TC-052 |
| M1A-07 | Before personal data is used, produce a consistent local SQLite backup; validate restore schema/integrity/relations/financial invariants before replacement, confirm replacement, stop writers, keep a safety backup, and verify reopening/rollback. A small opening/price fixture round-trips exactly; corrupt/incompatible input leaves live data unchanged. CSV is not required at this gate or represented as a backup. | FR-029, FR-030; NFR-011 | TC-029, TC-030, TC-034, TC-046 applicable small-fixture checks; TC-052 |
| M1A-08 | Record actual results for all applicable checks above, document local startup/validation/recovery and milestone limitations, and obtain owner acceptance with no unresolved integrity, data-loss or disclosure defect. The first dashboard has no direct balance edits, unit changes, income/expense/trade/transfer/correction/goal workflows or API calls; later requirements stay planned. | FR-001, FR-006, FR-029, FR-030, FR-032; NFR-005, NFR-008, NFR-011 | TC-052 and manual milestone evidence review; no execution is claimed now. |

Milestone Definition of Done: all eight checks have evidence and TASK-001, TASK-002, TASK-003, TASK-004A, TASK-005A, TASK-008A and TASK-007A are completed under their own criteria. These leaves sum to 32 hours already in the baseline. Financial/recovery safety cannot be waived to fit an estimate. See [WBS](../planning/WBS.md) and [schedule](../planning/PROJECT_SCHEDULE.md).

## 5. Business rules

The financial policies below are proposed design refinements unless explicitly backed by an owner choice. Review DEC-010 before implementing money/history rules; no regulated accounting compliance is claimed.

| ID | Rule and observable example |
|---|---|
| BR-001 | Fix one reporting currency and minor-unit scale before the first record. Foreign currency is an asset unit, valued with a manually entered base-currency price. Do not mix original-currency amounts into totals. |
| BR-002 | Holdings equal effective signed postings per account/asset. Value each holding with the last active price effective on/before the valuation date; base cash price is always 1. Round each holding half-even to the currency minor unit, then sum. No borrowing, shorts, margin, or negative holdings. |
| BR-003 | Savings = monthly income − monthly expenses. Savings rate = savings / income × 100 only for income > 0, displayed to two decimal places. Income 300 and expense 100 produce 200 and 66.67%. Opening balances, transfers, adjustments, purchases/sales, and unrealized gains are excluded. |
| BR-004 | A transfer has equal/opposite base-cash postings in distinct accounts and no income/expense classification. All postings commit together. Portfolio value changes only if holdings/prices change, never by counting both a movement and its destination as new income. |
| BR-005 | Total assets is the sum of priced holdings. The asset-only net-worth estimate equals that sum and always states liabilities are excluded. Goal balances are not added. Missing prices qualify both figures as incomplete; stale observations remain included but warned. |
| BR-006 | A purchase adds a positive asset quantity and removes a stated positive base-cash settlement; a sale does the reverse. Neither is household income/expense. Record transaction fees, when entered, as separate expenses and exclude them from the stated settlement amount to avoid counting them twice. No automated order execution or gain-tax accounting is provided. |
| BR-007 | Reservations are positive base-currency minor-unit amounts per source account and goal. Sum(active reservations for account) ≤ current account base cash. Spending/transferring/trading/correcting below that bound is rejected until the user explicitly releases funds. An adjustment is not an automatic release. |
| BR-008 | Reserved goal total is the sum of its active reservations. Remaining = max(target − reserved, 0). Progress = reserved / target × 100; the bar caps at 100%, while excess remains separately visible. Editing target lower does not create or destroy cash. |
| BR-009 | With owner-local today ≤ deadline, monthly opportunities = 12 × (deadline year − current year) + deadline month − current month + 1. This includes the current and deadline month; deadline today gives one. Required monthly contribution = ceiling_to_minor_unit(remaining / opportunities). Overdue underfunded goals show overdue and no monthly amount; funded goals return zero. This assumes contributions can begin this month, not a predictive model. |
| BR-010 | Records use a user-selected local financial date, not a UTC date inferred later. Future-dated financial events/prices are rejected in v1. Corrections reverse originals at the original effective date and replace at the selected date; restated charts change and remain labeled restated. Revalidate dated holdings and today's reservations atomically. No allocation-history trend is promised. |
| BR-011 | Decimal inputs must be finite and within signed 64-bit storage bounds after monetary scaling. Monetary entries with excess fractional digits are rejected, not silently rounded. Quantity/price inputs use at most 8 fractional digits (proposed); price × quantity uses exact arithmetic before per-holding rounding. UI charts may convert final values for display only. |
| BR-012 | AI receives approved computed context and untrusted user text only. Its generated numbers/explanations are not authoritative inputs to financial calculations, reports, allocations, or writes. Any contradictory AI text remains labeled unverified explanation beside authoritative computed figures. |
| BR-013 | Proposed stale threshold: observation older than 7 calendar days. Missing price is not zero. Historical dates use only observations effective by that date; corrections intentionally restate prior results, with an audit trail rather than a claim of original-as-known reporting. |
| BR-014 | Notification content comes from deterministic summaries, not automatic Gemini calls. One private recipient and explicit content/schedule consent are required. No inbound commands, webhook, or polling endpoint exists in v1; requests sent to the bot cannot disclose data or modify records. |
| BR-015 | The local runner sends at most the latest due occurrence per enabled rule after downtime. Acknowledged occurrences never resend automatically. Definite transient failures allow at most three attempts; ambiguous outcomes are marked uncertain for explicit user resolution, since exactly-once delivery across Telegram and SQLite cannot be guaranteed. |

## 6. Coverage, priorities, and unresolved decisions

| Charter area | Requirements |
|---|---|
| Local deployment, configuration, persistence | FR-001, FR-002, FR-032; NFR-001, NFR-002, NFR-005, NFR-009 |
| Accounts, assets, quantities, transactions | FR-003 through FR-010; NFR-008, NFR-012 |
| Dashboard and manual valuation | FR-005, FR-011 through FR-015; NFR-004, NFR-007 |
| Goals | FR-016 through FR-019 |
| Gemini | FR-020 through FR-024; NFR-003, NFR-010 |
| Telegram | FR-025 through FR-028; NFR-003, NFR-010 |
| Backup, restore, CSV | FR-029 through FR-031; NFR-011 |
| Modularity and automated verification | NFR-006; all planned cases in the RTM |

All 32 functional requirements and 12 NFRs are Must for the complete baseline; Should/Could priorities are reserved for optional future backlog candidates. This avoids silently downgrading Charter deliverables. API features are runtime optional, not omitted from release acceptance.

Open approvals and proposed thresholds are centralized in [DECISION_LOG](../DECISION_LOG.md). Stories/use cases refine these requirements; they cannot silently expand scope. See [RTM](RTM.md) for planned coverage, not implementation evidence.
