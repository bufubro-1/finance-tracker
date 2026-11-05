# Finance Tracker — Work Breakdown Structure

Status: Planned application deliverables; all packages are **Not Started**. DEC-015 approves the M-001A allocation, not implementation completion. The existing repository is an input. Each executable package includes its focused tests and usage notes.

## Accounting and milestone gates

The seven Charter phase budgets remain 16 + 32 + 20 + 24 + 16 + 20 + 24 = **152 hours**. Phases describe deliverable ownership; selected phase 2/3 portions now execute earlier. WBS 2.1, 2.2, 2.4, and 3.1 are non-additive parent rollups with A/B leaf children. The 25 leaf packages alone total 152 hours.

### M-001A — First Working Dashboard: Definition of Done

Target: **32 cumulative hours / end of Week 4**, after M-001's 16-hour foundation. Required leaves: 1.1, 1.2, 1.3, 2.1.1, 2.2.1, 3.1.1, and 2.4.1. Together they consume 32 hours already present in the baseline.

M-001A is done only when all M1A-01 through M1A-08 acceptance checks in [SRS](../requirements/SRS.md) have evidence: localhost startup without external APIs; basic account/manual asset registration and listing; exact valuation with dates/partial-total warnings; validated atomic opening writes and rollback; durable restart; duplicate-submission prevention; safe backup/restore; and recorded owner acceptance with no unresolved integrity, data-loss, or disclosure defect. Include calculation, persistence, invalid-input, rollback, replay, missing-price, and recovery checks. Store evidence later; no check is marked passed now.

The opening workflow uses the intended SQLite schema, postings and unit of work. No throwaway database, independent editable balance, float arithmetic, or weakened recovery path is allowed. Early inputs are existing holdings, not purchases; openings are excluded from income/expense. Corrections, transfers, full reports and goals remain later capabilities. Resolve prerequisite technical policies before their implementation.

M-004 remains at **92 cumulative hours / elapsed week 11.5**, with its original complete-core Definition of Done. M-002 now occurs at 54 hours; M-003 stays at 68 hours. See [schedule](PROJECT_SCHEDULE.md) for timing and [test plan](../testing/TEST_PLAN.md) for the milestone evidence profile.

## Deliverable hierarchy

## 1.0 Project Foundation

### 1.1 Runtime skeleton and local configuration

- **Description:** Build the WBS 1.1 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** Runtime skeleton and local configuration capability, focused test evidence, and usage notes.
- **Dependencies:** None; existing repository and planning documents are inputs.
- **Definition of Done:** A minimal documented Python project loads validated configuration, keeps adapters off, requires initial currency, and provides loopback-first startup and trusted-device firewall guidance; no real secrets are tracked.
- **Backlog and effort:** TASK-001; 4 hours preliminary, counted once as a leaf.

### 1.2 Exact monetary and date rules

- **Description:** Build the WBS 1.2 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** Exact monetary and date rules capability, focused test evidence, and usage notes.
- **Dependencies:** 1.1.
- **Definition of Done:** Pure decimal/date functions implement BR-001 through BR-012 as applicable, with boundary fixtures for rounding, unavailable savings rate, and overdue goals.
- **Backlog and effort:** TASK-002; 4 hours preliminary, counted once as a leaf.

### 1.3 SQLite schema and repositories

- **Description:** Build the WBS 1.3 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** SQLite schema and repositories capability, focused test evidence, and usage notes.
- **Dependencies:** 1.1, 1.2.
- **Definition of Done:** The reviewed data model becomes a versioned local schema with per-connection foreign keys, atomic unit-of-work behavior, temporary-database persistence tests, and no sensitive fixture data. The reviewed opening-command replay guard is included in schema/repository tests before TASK-005A; exact mechanism remains a proposed technical decision (DEC-016).
- **Backlog and effort:** TASK-003; 8 hours preliminary, counted once as a leaf.

## 2.0 Financial Tracking

### 2.1 Account and asset workflows

- **Description:** Build the WBS 2.1 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** Completed child capabilities; parent is a non-additive rollup.
- **Dependencies:** 2.1.1, 2.1.2.
- **Definition of Done:** The UI supports all specified asset types and account/asset CRUD/archive rules; referenced-delete protection and field validation pass their planned checks. Both children must be complete before this parent is complete.
- **Backlog and effort:** TASK-004; 8 hours rollup only, already counted in its children.

### 2.1.1 Basic account, asset registration, and listing

- **Description:** Deliver WBS 2.1.1 as an existing-budget portion; include its focused tests and usage notes.
- **Expected deliverable:** Basic account, asset registration, and listing capability, focused test evidence, and usage notes.
- **Dependencies:** 1.3.
- **Definition of Done:** A localhost Streamlit form creates/selects a basic account, validates cash/currency/gold/stock/fund registration fields, and produces a normalized opening intent for the shared service contract. An asset-list view reads committed repository holdings with units and clear outcomes. This leaf prepares the form/read path; TASK-005A connects atomic financial persistence. It does not save a new definition separately before an opening or directly update balances. Valid form input survives errors.
- **Backlog and effort:** TASK-004A; 4 hours preliminary, counted once as a leaf.

### 2.1.2 Remaining account and asset management

- **Description:** Deliver WBS 2.1.2 as an existing-budget portion; include its focused tests and usage notes.
- **Expected deliverable:** Remaining account and asset management capability, focused test evidence, and usage notes.
- **Dependencies:** 2.1.1.
- **Definition of Done:** Complete rename/edit/archive/delete workflows and referenced-record safeguards, applying the reviewed unit-immutability policy. All original account/asset acceptance criteria pass; existing openings and historical prices are not reinterpreted.
- **Backlog and effort:** TASK-004B; 4 hours preliminary, counted once as a leaf.

### 2.2 Financial ledger workflows

- **Description:** Build the WBS 2.2 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** Completed child capabilities; parent is a non-additive rollup.
- **Dependencies:** 2.2.1, 2.2.2.
- **Definition of Done:** Openings, purchases, sales, income, expenses, and explained adjustments create correct atomic postings; restart and validation fixtures pass. Both children must be complete before this parent is complete.
- **Backlog and effort:** TASK-005; 12 hours rollup only, already counted in its children.

### 2.2.1 Atomic opening transactions and replay protection

- **Description:** Deliver WBS 2.2.1 as an existing-budget portion; include its focused tests and usage notes.
- **Expected deliverable:** Atomic opening transactions and replay protection capability, focused test evidence, and usage notes.
- **Dependencies:** 2.1.1.
- **Definition of Done:** One validated registration commits the new asset definition, opening transaction/posting, and optional initial price in one unit of work. Holdings derive from postings; openings are excluded from income/expenses. Invalid or failed writes leave no orphan or partial record. Retried submissions/reruns cannot create duplicate openings, including after restart; a conflicting reuse is rejected. TC-040, TC-043 and TC-051 applicable checks pass.
- **Backlog and effort:** TASK-005A; 4 hours preliminary, counted once as a leaf.

### 2.2.2 Remaining income, expense, and trading ledger

- **Description:** Deliver WBS 2.2.2 as an existing-budget portion; include its focused tests and usage notes.
- **Expected deliverable:** Remaining income, expense, and trading ledger capability, focused test evidence, and usage notes.
- **Dependencies:** 2.2.1, 2.1.
- **Definition of Done:** Add manual purchases/sales, income, expenses, and explained adjustments using the same validated posting model. Preserve opening replay protection and atomicity, reject invalid/negative holdings, and run the original ledger regression cases.
- **Backlog and effort:** TASK-005B; 8 hours preliminary, counted once as a leaf.

### 2.3 Corrections and transfers

- **Description:** Build the WBS 2.3 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** Corrections and transfers capability, focused test evidence, and usage notes.
- **Dependencies:** 2.2.
- **Definition of Done:** Linked reversal/replacement and transfer workflows preserve history, respect historical holdings/current reservations, and never affect income/expense incorrectly.
- **Backlog and effort:** TASK-006; 8 hours preliminary, counted once as a leaf.

### 2.4 Backup, restore, and CSV

- **Description:** Build the WBS 2.4 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** Completed child capabilities; parent is a non-additive rollup.
- **Dependencies:** 2.4.1, 2.4.2.
- **Definition of Done:** A valid round trip passes with stopped writers; corrupt input preserves live data; consistent backup and safe CSV export are documented and checked. Both children must be complete before this parent is complete.
- **Backlog and effort:** TASK-007; 4 hours rollup only, already counted in its children.

### 2.4.1 Essential first-dashboard backup and restore

- **Description:** Deliver WBS 2.4.1 as an existing-budget portion; include its focused tests and usage notes.
- **Expected deliverable:** Essential first-dashboard backup and restore capability, focused test evidence, and usage notes.
- **Dependencies:** 1.3, 2.2.1.
- **Definition of Done:** Before personal data is used, create a consistent SQLite backup and provide a documented stopped-writer restore with schema/integrity/business validation, explicit replacement confirmation, a safety backup, and rollback/reopen checks. A small opening/price fixture round-trips, and corrupt/incompatible candidates leave live data unchanged. Core safety checks are not deferred to TASK-007B.
- **Backlog and effort:** TASK-007A; 2 hours preliminary, counted once as a leaf.

### 2.4.2 CSV export and remaining recovery verification

- **Description:** Deliver WBS 2.4.2 as an existing-budget portion; include its focused tests and usage notes.
- **Expected deliverable:** CSV export and remaining recovery verification capability, focused test evidence, and usage notes.
- **Dependencies:** 2.4.1, 2.3.
- **Definition of Done:** Add the documented safe CSV export and remaining recovery coverage for the expanded ledger. Repeat essential round-trip/invalid-restore checks and exercise backup during writes; later goal-related acceptance remains part of M-004 and final release verification.
- **Backlog and effort:** TASK-007B; 2 hours preliminary, counted once as a leaf.

## 3.0 Dashboard

### 3.1 Manual prices and valuation

- **Description:** Build the WBS 3.1 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** Completed child capabilities; parent is a non-additive rollup.
- **Dependencies:** 3.1.1, 3.1.2.
- **Definition of Done:** Dated manual prices, per-holding rounding, partial valuation, stale warnings, and asset-only labels pass deterministic fixtures. Both children must be complete before this parent is complete.
- **Backlog and effort:** TASK-008; 8 hours rollup only, already counted in its children.

### 3.1.1 Initial manual prices and first dashboard valuation

- **Description:** Deliver WBS 3.1.1 as an existing-budget portion; include its focused tests and usage notes.
- **Expected deliverable:** Initial manual prices and first dashboard valuation capability, focused test evidence, and usage notes.
- **Dependencies:** 1.3, 2.1.1, 2.2.1.
- **Definition of Done:** Enter dated initial reporting-currency prices, keep base cash valued at one, and display per-holding values plus the exact total/asset-only estimate. Show price dates, configurable stale warnings, unpriced holdings and incomplete subtotals, and an empty state. Cash 1000 plus 10 units at 20 totals 1200. Use exact arithmetic and agreed rounding; no income/expense/distribution charts are required yet.
- **Backlog and effort:** TASK-008A; 6 hours preliminary, counted once as a leaf.

### 3.1.2 Price corrections and valuation completion

- **Description:** Deliver WBS 3.1.2 as an existing-budget portion; include its focused tests and usage notes.
- **Expected deliverable:** Price corrections and valuation completion capability, focused test evidence, and usage notes.
- **Dependencies:** 3.1.1, 2.3.
- **Definition of Done:** Complete auditable price corrections and validate totals after reversals, transfers, and the expanded ledger. Meet all original valuation criteria and applicable performance checks without changing accepted rounding or completeness semantics.
- **Backlog and effort:** TASK-008B; 2 hours preliminary, counted once as a leaf.

### 3.2 Monthly dashboard and distribution

- **Description:** Build the WBS 3.2 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** Monthly dashboard and distribution capability, focused test evidence, and usage notes.
- **Dependencies:** 3.1.
- **Definition of Done:** Plotly/Pandas presentation uses authoritative service results, consistent distribution totals, clear empty states, and correct monthly savings.
- **Backlog and effort:** TASK-009; 8 hours preliminary, counted once as a leaf.

### 3.3 Historical reporting

- **Description:** Build the WBS 3.3 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** Historical reporting capability, focused test evidence, and usage notes.
- **Dependencies:** 3.2.
- **Definition of Done:** Historical reports use effective transactions and dated prices, expose gaps, and recalculate after corrections without applying future prices backward.
- **Backlog and effort:** TASK-010; 4 hours preliminary, counted once as a leaf.

## 4.0 Goal Management

### 4.1 Savings goal workflows

- **Description:** Build the WBS 4.1 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** Savings goal workflows capability, focused test evidence, and usage notes.
- **Dependencies:** 3.2.
- **Definition of Done:** Multiple goals support valid target/date editing and confirmed reservation release on closure; invalid targets and overdue states are covered.
- **Backlog and effort:** TASK-011; 4 hours preliminary, counted once as a leaf.

### 4.2 Atomic cash reservations

- **Description:** Build the WBS 4.2 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** Atomic cash reservations capability, focused test evidence, and usage notes.
- **Dependencies:** 4.1, 2.3.
- **Definition of Done:** Allocations, releases, cash debits, and corrections share the reservation invariant; competing-write fixtures cannot over-allocate; progress never increases total assets.
- **Backlog and effort:** TASK-012; 12 hours preliminary, counted once as a leaf.

### 4.3 Contribution projections and goal views

- **Description:** Build the WBS 4.3 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** Contribution projections and goal views capability, focused test evidence, and usage notes.
- **Dependencies:** 4.2.
- **Definition of Done:** Monthly opportunity counting, upward-rounded contributions, deadline-today, overdue, excess-funded, and zero-gap views match the documented rules.
- **Backlog and effort:** TASK-013; 8 hours preliminary, counted once as a leaf.

## 5.0 AI Integration

### 5.1 Gemini boundary and consent

- **Description:** Build the WBS 5.1 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** Gemini boundary and consent capability, focused test evidence, and usage notes.
- **Dependencies:** 3.2.
- **Definition of Done:** An environment-configured adapter accepts only immutable per-request approved payloads, redacts errors, uses a bounded timeout, and is replaced by fakes in automated tests.
- **Backlog and effort:** TASK-014; 8 hours preliminary, counted once as a leaf.

### 5.2 AI explanation workflows

- **Description:** Build the WBS 5.2 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** AI explanation workflows capability, focused test evidence, and usage notes.
- **Dependencies:** 5.1, 4.3.
- **Definition of Done:** Spending, summary, goal feasibility, and question workflows label AI output, disclose partial context, and have no path to financial writes; failures preserve core availability.
- **Backlog and effort:** TASK-015; 8 hours preliminary, counted once as a leaf.

## 6.0 Telegram Integration

### 6.1 Telegram recipient and preferences

- **Description:** Build the WBS 6.1 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** Telegram recipient and preferences capability, focused test evidence, and usage notes.
- **Dependencies:** 1.1.
- **Definition of Done:** One validated private destination, non-financial connection test, report-field consent, timezone, and disabled-by-default schedules are configurable; no inbound commands are handled.
- **Backlog and effort:** TASK-016; 6 hours preliminary, counted once as a leaf.

### 6.2 Scheduled summary runner

- **Description:** Build the WBS 6.2 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** Scheduled summary runner capability, focused test evidence, and usage notes.
- **Dependencies:** 6.1, 3.2, 2.4.
- **Definition of Done:** A local scheduled command claims unique due occurrences, checks the allowlist, delivers deterministic summaries, and handles downtime, retries, ambiguity, and duplicate invocation.
- **Backlog and effort:** TASK-017; 10 hours preliminary, counted once as a leaf.

### 6.3 Goal notifications

- **Description:** Build the WBS 6.3 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** Goal notifications capability, focused test evidence, and usage notes.
- **Dependencies:** 6.2, 4.3.
- **Definition of Done:** Enabled reminders/progress updates use current deterministic goal data and unique occurrence keys; deleted goals and disabled rules do not send.
- **Backlog and effort:** TASK-018; 4 hours preliminary, counted once as a leaf.

## 7.0 Testing and Documentation

### 7.1 System and acceptance verification

- **Description:** Build the WBS 7.1 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** System and acceptance verification capability, focused test evidence, and usage notes.
- **Dependencies:** 2.4, 3.3, 4.3, 5.2, 6.3.
- **Definition of Done:** Execute the planned release tests on synthetic data, resolve Must failures, record actual results, and run the owner acceptance scenarios with external calls opt-in.
- **Backlog and effort:** TASK-019; 10 hours preliminary, counted once as a leaf.

### 7.2 Deployment and recovery rehearsal

- **Description:** Build the WBS 7.2 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** Deployment and recovery rehearsal capability, focused test evidence, and usage notes.
- **Dependencies:** 7.1.
- **Definition of Done:** A clean supported local setup, trusted/denied-device checks, offline restart, and timed restore rehearsal produce evidence; warnings and residual limitations are documented.
- **Backlog and effort:** TASK-020; 6 hours preliminary, counted once as a leaf.

### 7.3 Usage documentation and local release

- **Description:** Build the WBS 7.3 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Expected deliverable:** Usage documentation and local release capability, focused test evidence, and usage notes.
- **Dependencies:** 7.2.
- **Definition of Done:** Installation, configuration examples, workflows, scheduling, limitations, backup/recovery, and release notes match observed behavior; no credentials/data enter Git; owner reviews the local release.
- **Backlog and effort:** TASK-021; 8 hours preliminary, counted once as a leaf.

## Completion discipline

A milestone or parent is not complete merely because an early portion exists. M-001A is a subset delivery of existing requirements, not full acceptance of every mapped FR/NFR. M-004 still comprises all phase 1–4 deliverables and their applicable acceptance evidence; full release also includes phases 5–7. No optional FUT candidate or documentation-maintenance effort is added to the 152-hour development baseline.
