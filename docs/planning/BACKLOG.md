# Finance Tracker — Development Backlog

Status: Development work is **Not Started**. DEC-015 records the owner-approved M-001A milestone and reallocation; other proposed technical decisions retain their existing status. Focused verification and usage notes are included in task estimates. No application work has been performed.

## Estimate accounting and execution order

The 21 original task IDs are retained. TASK-004, TASK-005, TASK-007, and TASK-008 are **non-additive rollups**, each completed only when both A/B children are done. There are 25 executable leaf tasks and four rollups. Schedule/count leaf estimates only; never add a rollup to its children. A rollup's dependencies express completion, not a gate inherited by its early child.

| Rollup | Original budget | Early A portion | Remaining B portion |
|---|---:|---:|---:|
| TASK-004 | 8 h | TASK-004A: 4 h | TASK-004B: 4 h |
| TASK-005 | 12 h | TASK-005A: 4 h | TASK-005B: 8 h |
| TASK-007 | 4 h | TASK-007A: 2 h | TASK-007B: 2 h |
| TASK-008 | 8 h | TASK-008A: 6 h | TASK-008B: 2 h |

Execute TASK-001 → TASK-002 → TASK-003 → TASK-004A → TASK-005A → TASK-008A → TASK-007A for M-001A (32 cumulative hours). Then TASK-004B → TASK-005B → TASK-006 → TASK-007B completes M-002 at 54 hours; TASK-008B → TASK-009 → TASK-010 completes M-003 at 68 hours; TASK-011–TASK-013 preserves M-004 at 92 hours. TASK-014–TASK-021 retain the remaining 60 hours; total 152 hours.

Prerequisites: choose the supported runtime for TASK-001; review financial precision, history, asset-unit edit restrictions, and replay-guard design before TASK-002/003/005A (OQ-002/004/007). M-001A approval does not silently approve unresolved technical policies.

## Core work and first-dashboard portions

M-001A is a narrower first working dashboard. M-004 remains the first usable **complete core**, including goals, full tracking/reporting and applicable security/recovery evidence. Parent acceptance criteria below retain the original full scope; only the A portions plus TASK-001–003 are required at M-001A.

### TASK-001 — Runtime skeleton and local configuration

- **Type:** Executable leaf
- **Description:** Build the WBS 1.1 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** None
- **Related requirements:** FR-001, FR-002, FR-032; NFR-001, NFR-002, NFR-006, NFR-009
- **Acceptance criteria:** A minimal documented Python project loads validated configuration, keeps adapters off, requires initial currency, and provides loopback-first startup and trusted-device firewall guidance; no real secrets are tracked.
- **Estimated effort:** 4 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-002 — Exact monetary and date rules

- **Type:** Executable leaf
- **Description:** Build the WBS 1.2 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-001
- **Related requirements:** FR-002, FR-012, FR-013, FR-019; NFR-006, NFR-012
- **Acceptance criteria:** Pure decimal/date functions implement BR-001 through BR-012 as applicable, with boundary fixtures for rounding, unavailable savings rate, and overdue goals.
- **Estimated effort:** 4 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-003 — SQLite schema and repositories

- **Type:** Executable leaf
- **Description:** Build the WBS 1.3 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-001, TASK-002
- **Related requirements:** FR-003, FR-004, FR-006, FR-009, FR-017, FR-032; NFR-002, NFR-005, NFR-006, NFR-008
- **Acceptance criteria:** The reviewed data model becomes a versioned local schema with per-connection foreign keys, atomic unit-of-work behavior, temporary-database persistence tests, and no sensitive fixture data. The reviewed opening-command replay guard is included in schema/repository tests before TASK-005A; exact mechanism remains a proposed technical decision (DEC-016).
- **Estimated effort:** 8 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-004 — Account and asset workflows

- **Type:** Rollup — do not count or schedule separately
- **Description:** Build the WBS 2.1 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-004A, TASK-004B
- **Related requirements:** FR-003, FR-004; NFR-004
- **Acceptance criteria:** The UI supports all specified asset types and account/asset CRUD/archive rules; referenced-delete protection and field validation pass their planned checks.
- **Estimated effort:** 8 hours rollup only; included in the children, not additional.
- **Status:** Not Started

### TASK-004A — Basic account, asset registration, and listing

- **Type:** Executable leaf
- **Description:** Deliver WBS 2.1.1 as an existing-budget portion; include its focused tests and usage notes.
- **Priority:** Must
- **Dependencies:** TASK-003
- **Related requirements:** FR-003, FR-004; NFR-004
- **Acceptance criteria:** A localhost Streamlit form creates/selects a basic account, validates cash/currency/gold/stock/fund registration fields, and produces a normalized opening intent for the shared service contract. An asset-list view reads committed repository holdings with units and clear outcomes. This leaf prepares the form/read path; TASK-005A connects atomic financial persistence. It does not save a new definition separately before an opening or directly update balances. Valid form input survives errors.
- **Estimated effort:** 4 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-004B — Remaining account and asset management

- **Type:** Executable leaf
- **Description:** Deliver WBS 2.1.2 as an existing-budget portion; include its focused tests and usage notes.
- **Priority:** Must
- **Dependencies:** TASK-004A
- **Related requirements:** FR-003, FR-004; NFR-004
- **Acceptance criteria:** Complete rename/edit/archive/delete workflows and referenced-record safeguards, applying the reviewed unit-immutability policy. All original account/asset acceptance criteria pass; existing openings and historical prices are not reinterpreted.
- **Estimated effort:** 4 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-005 — Financial ledger workflows

- **Type:** Rollup — do not count or schedule separately
- **Description:** Build the WBS 2.2 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-005A, TASK-005B
- **Related requirements:** FR-006, FR-007, FR-008, FR-032; NFR-005, NFR-008
- **Acceptance criteria:** Openings, purchases, sales, income, expenses, and explained adjustments create correct atomic postings; restart and validation fixtures pass.
- **Estimated effort:** 12 hours rollup only; included in the children, not additional.
- **Status:** Not Started

### TASK-005A — Atomic opening transactions and replay protection

- **Type:** Executable leaf
- **Description:** Deliver WBS 2.2.1 as an existing-budget portion; include its focused tests and usage notes.
- **Priority:** Must
- **Dependencies:** TASK-004A
- **Related requirements:** FR-006, FR-032; NFR-005, NFR-008
- **Acceptance criteria:** One validated registration commits the new asset definition, opening transaction/posting, and optional initial price in one unit of work. Holdings derive from postings; openings are excluded from income/expenses. Invalid or failed writes leave no orphan or partial record. Retried submissions/reruns cannot create duplicate openings, including after restart; a conflicting reuse is rejected. TC-040, TC-043 and TC-051 applicable checks pass.
- **Estimated effort:** 4 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-005B — Remaining income, expense, and trading ledger

- **Type:** Executable leaf
- **Description:** Deliver WBS 2.2.2 as an existing-budget portion; include its focused tests and usage notes.
- **Priority:** Must
- **Dependencies:** TASK-005A, TASK-004
- **Related requirements:** FR-006, FR-007, FR-008, FR-032; NFR-005, NFR-008
- **Acceptance criteria:** Add manual purchases/sales, income, expenses, and explained adjustments using the same validated posting model. Preserve opening replay protection and atomicity, reject invalid/negative holdings, and run the original ledger regression cases.
- **Estimated effort:** 8 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-006 — Corrections and transfers

- **Type:** Executable leaf
- **Description:** Build the WBS 2.3 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-005
- **Related requirements:** FR-009, FR-010; NFR-005, NFR-008
- **Acceptance criteria:** Linked reversal/replacement and transfer workflows preserve history, respect historical holdings/current reservations, and never affect income/expense incorrectly.
- **Estimated effort:** 8 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-007 — Backup, restore, and CSV

- **Type:** Rollup — do not count or schedule separately
- **Description:** Build the WBS 2.4 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-007A, TASK-007B
- **Related requirements:** FR-029, FR-030, FR-031; NFR-011
- **Acceptance criteria:** A valid round trip passes with stopped writers; corrupt input preserves live data; consistent backup and safe CSV export are documented and checked.
- **Estimated effort:** 4 hours rollup only; included in the children, not additional.
- **Status:** Not Started

### TASK-007A — Essential first-dashboard backup and restore

- **Type:** Executable leaf
- **Description:** Deliver WBS 2.4.1 as an existing-budget portion; include its focused tests and usage notes.
- **Priority:** Must
- **Dependencies:** TASK-003, TASK-005A
- **Related requirements:** FR-029, FR-030; NFR-011
- **Acceptance criteria:** Before personal data is used, create a consistent SQLite backup and provide a documented stopped-writer restore with schema/integrity/business validation, explicit replacement confirmation, a safety backup, and rollback/reopen checks. A small opening/price fixture round-trips, and corrupt/incompatible candidates leave live data unchanged. Core safety checks are not deferred to TASK-007B.
- **Estimated effort:** 2 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-007B — CSV export and remaining recovery verification

- **Type:** Executable leaf
- **Description:** Deliver WBS 2.4.2 as an existing-budget portion; include its focused tests and usage notes.
- **Priority:** Must
- **Dependencies:** TASK-007A, TASK-006
- **Related requirements:** FR-029, FR-030, FR-031; NFR-011
- **Acceptance criteria:** Add the documented safe CSV export and remaining recovery coverage for the expanded ledger. Repeat essential round-trip/invalid-restore checks and exercise backup during writes; later goal-related acceptance remains part of M-004 and final release verification.
- **Estimated effort:** 2 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-008 — Manual prices and valuation

- **Type:** Rollup — do not count or schedule separately
- **Description:** Build the WBS 3.1 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-008A, TASK-008B
- **Related requirements:** FR-005, FR-011, FR-012; NFR-007, NFR-012
- **Acceptance criteria:** Dated manual prices, per-holding rounding, partial valuation, stale warnings, and asset-only labels pass deterministic fixtures.
- **Estimated effort:** 8 hours rollup only; included in the children, not additional.
- **Status:** Not Started

### TASK-008A — Initial manual prices and first dashboard valuation

- **Type:** Executable leaf
- **Description:** Deliver WBS 3.1.1 as an existing-budget portion; include its focused tests and usage notes.
- **Priority:** Must
- **Dependencies:** TASK-003, TASK-004A, TASK-005A
- **Related requirements:** FR-005, FR-011, FR-012; NFR-007, NFR-012
- **Acceptance criteria:** Enter dated initial reporting-currency prices, keep base cash valued at one, and display per-holding values plus the exact total/asset-only estimate. Show price dates, configurable stale warnings, unpriced holdings and incomplete subtotals, and an empty state. Cash 1000 plus 10 units at 20 totals 1200. Use exact arithmetic and agreed rounding; no income/expense/distribution charts are required yet.
- **Estimated effort:** 6 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-008B — Price corrections and valuation completion

- **Type:** Executable leaf
- **Description:** Deliver WBS 3.1.2 as an existing-budget portion; include its focused tests and usage notes.
- **Priority:** Must
- **Dependencies:** TASK-008A, TASK-006
- **Related requirements:** FR-005, FR-011, FR-012; NFR-007, NFR-012
- **Acceptance criteria:** Complete auditable price corrections and validate totals after reversals, transfers, and the expanded ledger. Meet all original valuation criteria and applicable performance checks without changing accepted rounding or completeness semantics.
- **Estimated effort:** 2 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-009 — Monthly dashboard and distribution

- **Type:** Executable leaf
- **Description:** Build the WBS 3.2 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-008
- **Related requirements:** FR-013, FR-014; NFR-004, NFR-007
- **Acceptance criteria:** Plotly/Pandas presentation uses authoritative service results, consistent distribution totals, clear empty states, and correct monthly savings.
- **Estimated effort:** 8 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-010 — Historical reporting

- **Type:** Executable leaf
- **Description:** Build the WBS 3.3 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-009
- **Related requirements:** FR-015
- **Acceptance criteria:** Historical reports use effective transactions and dated prices, expose gaps, and recalculate after corrections without applying future prices backward.
- **Estimated effort:** 4 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-011 — Savings goal workflows

- **Type:** Executable leaf
- **Description:** Build the WBS 4.1 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-009
- **Related requirements:** FR-016
- **Acceptance criteria:** Multiple goals support valid target/date editing and confirmed reservation release on closure; invalid targets and overdue states are covered.
- **Estimated effort:** 4 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-012 — Atomic cash reservations

- **Type:** Executable leaf
- **Description:** Build the WBS 4.2 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-011, TASK-006
- **Related requirements:** FR-017, FR-018; NFR-005, NFR-007, NFR-008
- **Acceptance criteria:** Allocations, releases, cash debits, and corrections share the reservation invariant; competing-write fixtures cannot over-allocate; progress never increases total assets.
- **Estimated effort:** 12 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-013 — Contribution projections and goal views

- **Type:** Executable leaf
- **Description:** Build the WBS 4.3 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-012
- **Related requirements:** FR-019; NFR-004, NFR-012
- **Acceptance criteria:** Monthly opportunity counting, upward-rounded contributions, deadline-today, overdue, excess-funded, and zero-gap views match the documented rules.
- **Estimated effort:** 8 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

## Complete Charter release — remaining phases 5–7

Gemini and Telegram are optional to enable but remain required complete-release deliverables.

### TASK-014 — Gemini boundary and consent

- **Type:** Executable leaf
- **Description:** Build the WBS 5.1 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-009
- **Related requirements:** FR-024; NFR-002, NFR-003, NFR-006, NFR-010
- **Acceptance criteria:** An environment-configured adapter accepts only immutable per-request approved payloads, redacts errors, uses a bounded timeout, and is replaced by fakes in automated tests.
- **Estimated effort:** 8 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-015 — AI explanation workflows

- **Type:** Executable leaf
- **Description:** Build the WBS 5.2 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-014, TASK-013
- **Related requirements:** FR-020, FR-021, FR-022, FR-023; NFR-003, NFR-010
- **Acceptance criteria:** Spending, summary, goal feasibility, and question workflows label AI output, disclose partial context, and have no path to financial writes; failures preserve core availability.
- **Estimated effort:** 8 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-016 — Telegram recipient and preferences

- **Type:** Executable leaf
- **Description:** Build the WBS 6.1 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-001
- **Related requirements:** FR-025, FR-028; NFR-002, NFR-003, NFR-006
- **Acceptance criteria:** One validated private destination, non-financial connection test, report-field consent, timezone, and disabled-by-default schedules are configurable; no inbound commands are handled.
- **Estimated effort:** 6 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-017 — Scheduled summary runner

- **Type:** Executable leaf
- **Description:** Build the WBS 6.2 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-016, TASK-009, TASK-007
- **Related requirements:** FR-026; NFR-003, NFR-010
- **Acceptance criteria:** A local scheduled command claims unique due occurrences, checks the allowlist, delivers deterministic summaries, and handles downtime, retries, ambiguity, and duplicate invocation.
- **Estimated effort:** 10 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-018 — Goal notifications

- **Type:** Executable leaf
- **Description:** Build the WBS 6.3 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-017, TASK-013
- **Related requirements:** FR-027; NFR-010
- **Acceptance criteria:** Enabled reminders/progress updates use current deterministic goal data and unique occurrence keys; deleted goals and disabled rules do not send.
- **Estimated effort:** 4 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-019 — System and acceptance verification

- **Type:** Executable leaf
- **Description:** Build the WBS 7.1 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-007, TASK-010, TASK-013, TASK-015, TASK-018
- **Related requirements:** FR-001, FR-002, FR-003, FR-004, FR-005, FR-006, FR-007, FR-008, FR-009, FR-010, FR-011, FR-012, FR-013, FR-014, FR-015, FR-016, FR-017, FR-018, FR-019, FR-020, FR-021, FR-022, FR-023, FR-024, FR-025, FR-026, FR-027, FR-028, FR-029, FR-030, FR-031, FR-032; NFR-004, NFR-007
- **Acceptance criteria:** Execute the planned release tests on synthetic data, resolve Must failures, record actual results, and run the owner acceptance scenarios with external calls opt-in.
- **Estimated effort:** 10 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-020 — Deployment and recovery rehearsal

- **Type:** Executable leaf
- **Description:** Build the WBS 7.2 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-019
- **Related requirements:** FR-001, FR-025, FR-029, FR-030, FR-032; NFR-001, NFR-002, NFR-009, NFR-011
- **Acceptance criteria:** A clean supported local setup, trusted/denied-device checks, offline restart, and timed restore rehearsal produce evidence; warnings and residual limitations are documented.
- **Estimated effort:** 6 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

### TASK-021 — Usage documentation and local release

- **Type:** Executable leaf
- **Description:** Build the WBS 7.3 deliverable using the proposed architecture and the linked requirements; include the focused verification needed to demonstrate the behavior.
- **Priority:** Must
- **Dependencies:** TASK-020
- **Related requirements:** FR-001, FR-002, FR-025, FR-028, FR-029, FR-030, FR-031, FR-032; NFR-009, NFR-011
- **Acceptance criteria:** Installation, configuration examples, workflows, scheduling, limitations, backup/recovery, and release notes match observed behavior; no credentials/data enter Git; owner reviews the local release.
- **Estimated effort:** 8 hours, preliminary; includes focused tests and notes.
- **Status:** Not Started

## Optional future enhancements — outside release estimates

These are Charter §13 candidates, not approved requirements or hidden prerequisites. Each needs owner selection and new requirements/tests before implementation. No estimate is included in the 152-hour baseline.

| Task ID | Title / description | Priority | Dependencies | Related requirements | Acceptance criteria for future selection | Effort | Status |
|---|---|---|---|---|---|---|---|
| FUT-001 | Evaluate automatic market prices and rate-provider costs | Could | TASK-021; owner scope decision | None; future Charter §13 | Define supported sources, freshness/fallback rules, privacy, licensing, and approved requirements before building. | Not estimated | Not Started |
| FUT-002 | Evaluate multi-currency analysis | Could | TASK-021; owner scope decision | None; future Charter §13 | Specify FX history, conversion semantics, migration, and approved acceptance examples. | Not estimated | Not Started |
| FUT-003 | Evaluate inflation-adjusted and advanced portfolio analytics | Could | TASK-021; owner scope decision | None; future Charter §13 | Select metrics and data sources and approve deterministic calculation examples. | Not estimated | Not Started |
| FUT-004 | Evaluate recurring entries and AI categorization | Could | TASK-021; owner scope decision | None; future Charter §13 | Define duplicate-prevention and human-approval boundaries before authorizing writes. | Not estimated | Not Started |
| FUT-005 | Evaluate forecasting and scenarios | Could | TASK-021; owner scope decision | None; future Charter §13 | Define assumptions, uncertainty labels, and nonauthoritative forecast outputs. | Not estimated | Not Started |
| FUT-006 | Improve responsive dashboard layouts | Should | TASK-021; owner scope decision | None; future Charter §13 | Agree target viewport sizes and usability criteria; retain core calculation semantics. | Not estimated | Not Started |

## Next development task and maintenance

TASK-001 is the first executable development task after the owner reviews the planning baseline. It establishes configuration and safe startup; TASK-002 then fixes money/date rules before schema and ledger implementation. This documentation assignment does not begin either task.

Re-estimate after M-001, M-001A, and M-004. Preserve approved targets unless the owner explicitly revises them; do not trim financial safeguards to meet a timebox. Change a status only with evidence; dependencies are not a reason to label every future task Blocked. Later execution may use In Progress, Blocked, or Completed, but none is asserted here. Major scope changes require a decision record and traceability updates first.
