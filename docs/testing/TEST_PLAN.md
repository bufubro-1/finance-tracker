# Finance Tracker — Software Test Plan

Status: **All cases Planned — Not Executed.** No application code, executable tests, coverage figures, or passing results exist. Documentation checks are not application tests.

DEC-018 in the [Decision Log](../DECISION_LOG.md) authorizes only TASK-001 under its documented requirements, architecture, and acceptance criteria, including relevant setup tests; execution remains explicitly held and TASK-001 is Not Started. Financial calculations, database schemas, asset management, Gemini features, and Telegram features are excluded from that task. The remaining baseline and technical policies retain their existing approval gates; no test case or acceptance criterion is changed by this synchronization.

## Objectives and scope

Prove deterministic financial correctness, validated transactions, nonduplicated goal reservations, local persistence/recovery, integration isolation, privacy, and authorized Telegram delivery. Cover all 32 FRs and 12 NFRs through [RTM](../requirements/RTM.md). Exclude banking/trading/tax compliance, liability accounting, automatic FX, cloud deployment, and multi-user concurrency; two local writers still require safe SQLite transactions.

## Strategy

| Level | Approach |
|---|---|
| Unit | Pure decimal arithmetic, holdings, savings, valuation completeness, date opportunities, rounding, and payload minimization. Use fixed dates and table-driven boundary fixtures; compare exact values rather than chart pixels. |
| Integration | Isolated temporary SQLite databases; exercise repositories and services together, rollback injection, reversal history, competing reservations, backup/restore, and fake adapters. Verify all write paths, including UI services and the notification runner. |
| System | Launch the eventual local application/runner with synthetic data; verify restart, CSV files, offline behavior, deployment/network restrictions, and bounded failure handling. |
| Acceptance | Owner follows complete asset/income/expense/transfer/goal/recovery workflows. First-core acceptance uses the applicable cases through phase 4; full release adds Gemini, Telegram, and final security/recovery checks. |

Tests accompany each development task, rather than waiting for phase 7. DEC-017 approves pytest as the test tool; its compatible version and dependency set remain unverified until TASK-001. No dependency is installed by this documentation work. Optional property-style tests can generate transaction sequences to check asset/reservation conservation without adding infrastructure.

## Environment and data

Approved development runtime under DEC-017: the current Linux environment, Python 3.14.x with locally installed 3.14.8 as the initial target, venv, pip, and pytest. OQ-004's runtime selection is resolved; dependency compatibility and exact compatible dependency versions remain unverified TASK-001 work. Report incompatibilities rather than silently changing Python or architecture. The planned application environment retains local-disk SQLite and a browser with Streamlit. Performance reference: 2 CPU cores, 8 GB RAM, SSD, 10,000 transactions, 200 assets, 20 goals. Tests run in UTC with explicit configured local timezone cases, including month/year rollover and timezone boundary dates.

Use fake Gemini/Telegram clients for deterministic failure, quota, unauthorized-recipient, and privacy checks. Live smoke tests require owner-supplied credentials, explicit consent, and only synthetic payloads; they are not a prerequisite for core testing. Do not run financial tests against a personal database or personal Telegram destination by default. Simulate provider errors rather than relying on outages.

Common fixture F-001: reporting currency TEST at scale 2 (a synthetic test identifier, not a production currency), two accounts, cash 1000 in account A, zero in B, a stock with a dated price, and two goals. Dates are injected. Additional fixtures cover missing prices, scale 0/3, allocation pressure, corrupt backups, and a fake bot private chat. Reset between cases; the listed expected results do not assume previous cases ran.

## Entry and exit criteria

**Per-task entry:** applicable requirements and proposed financial policies reviewed; isolated fixtures available; prerequisite code exists; test expectations derive from business rules rather than implementation details.

**M-001A entry:** foundation/schema and relevant technical policies are reviewed; only the opening/account/list/initial-price/local recovery slices exist; use isolated synthetic data and a fixed date. Dependencies are TASK-001–003, TASK-004A, TASK-005A, TASK-008A and TASK-007A, not the later full-parent completions.

**M-001A exit:** M1A-01 through M1A-08 pass with actual recorded evidence; correct local dashboard behavior, exact totals, durable atomic openings, replay prevention and safe recovery are demonstrated; owner acceptance is recorded; no unresolved integrity, data-loss or disclosure defect remains. This is a limited first working dashboard, not M-004 or full FR/NFR acceptance.

**M-001A planned test selection:** TC-001/002/003/004/005/006/011/012/029/030/032/034/035/038/040/041/043/044/046/047, scoped to existing opening-only capabilities, plus TC-051/052 in full. TC-046 uses a small coherent opening/price fixture here; its expanded writer/10,000-record timed recovery checks remain later. Full CRUD, purchases/sales, correction, goal, denied-LAN-device and performance variants stay for their original later gates. Partial case selection must be recorded per scenario; never mark an entire broader case passed from this subset. All cases are still Planned — Not Executed.

First-dashboard fixture F-002: fresh temporary dataset with synthetic TEST reporting currency at scale 2, one account, opening cash 1000, a stock opening of 10 units with price 20 on the injected current date, and a separate positive unpriced holding for the incomplete-total variant. No goals or API clients are enabled. Replay tests preserve one logical submission key across process restart. Restore tests stop all writers, use a separate candidate file and compare financial results/history before and after. TEST is test-only, not a production currency choice.

**First usable core exit:** core FR-001 through FR-019 and FR-029 through FR-032 pass their applicable tests; relevant NFRs pass; deterministic calculations, persistence, reservation integrity, backup/restore, and safe LAN access have evidence; no unresolved data-loss, integrity, or privacy defect remains. External adapters may be absent at this milestone.

**Complete release exit:** all Must FR/NFR cases pass; proposed thresholds are approved or explicitly revised before measurement; owner acceptance and recovery/network rehearsals are recorded; defects affecting financial correctness, unauthorized disclosure, or recovery are resolved. A live integration check can be recorded as blocked by credentials/quota, but the corresponding integration deliverable cannot be called fully accepted without its agreed acceptance evidence.

For execution later, record build/revision, environment, input fixture, date, actual outcome, evidence, and defect references for each case. Use Not Run/Pass/Fail/Blocked only in execution records, never prepopulate Pass here. Review failures for shared calculation or transaction causes before changing expected values.

## Planned test cases

Each case below may expand into multiple executable parameterized tests. All use isolated synthetic data and have status **Planned — Not Executed**.

### TC-001 — Local configuration

- **Level:** Integration
- **Requirements:** FR-001
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-001.
- **Expected result:** Without API credentials, the core launches with both adapters disabled; enabling an adapter with missing credentials produces a redacted configuration error and leaves the core usable.
- **Status:** Planned — Not Executed

### TC-002 — Reporting currency

- **Level:** Unit + integration
- **Requirements:** FR-002
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-002.
- **Expected result:** A fresh dataset requires an explicit currency selection; later currency changes are rejected without modifying records; foreign-currency units can be priced manually in the reporting currency.
- **Status:** Planned — Not Executed

### TC-003 — Account management

- **Level:** Integration
- **Requirements:** FR-003
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-003.
- **Expected result:** Account names are unique ignoring case; an account with postings or allocations cannot be physically deleted; archiving requires zero holdings and no allocations.
- **Status:** Planned — Not Executed

### TC-004 — Asset management

- **Level:** Integration
- **Requirements:** FR-004
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-004.
- **Expected result:** Each asset records a name, type, unit, and optional quoted currency; duplicate account holdings are aggregated by asset ID; referenced assets cannot be physically deleted; base cash has a fixed unit value of one.
- **Status:** Planned — Not Executed

### TC-005 — Manual price history

- **Level:** Unit + integration
- **Requirements:** FR-005
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-005.
- **Expected result:** Positive finite prices and effective dates are validated; superseded observations remain auditable; correcting a price recomputes affected reports; future-dated prices are rejected.
- **Status:** Planned — Not Executed

### TC-006 — Holding transactions

- **Level:** Unit + integration
- **Requirements:** FR-006
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-006.
- **Expected result:** A purchase of 200 reduces base cash by 200 and adds the purchased quantity atomically; a sale records its cash proceeds; opening balances and adjustments are excluded from income and expenses; insufficient holdings are rejected. Opening registration and replay protection also meet FR-006/M1A-04/M1A-06, including rollback and no duplicate records.
- **Status:** Planned — Not Executed

### TC-007 — Income recording

- **Level:** Unit + integration
- **Requirements:** FR-007
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-007.
- **Expected result:** Valid income increases account base cash once; missing account, zero/negative amount, excess monetary precision, and future dates are rejected without partial writes.
- **Status:** Planned — Not Executed

### TC-008 — Expense recording

- **Level:** Unit + integration
- **Requirements:** FR-008
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-008.
- **Expected result:** Valid expense reduces base cash once; an expense exceeding unreserved cash is rejected with a release-allocation instruction; invalid inputs leave balances unchanged.
- **Status:** Planned — Not Executed

### TC-009 — Record correction and deletion

- **Level:** Integration
- **Requirements:** FR-009
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-009.
- **Expected result:** A correction creates linked replacement/reversal records in one transaction; deletion reverses the effective record; repeated deletion is rejected; changed historical balances and reservations are revalidated before commit.
- **Status:** Planned — Not Executed

### TC-010 — Account transfers

- **Level:** Unit + integration
- **Requirements:** FR-010
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-010.
- **Expected result:** A 100 transfer creates equal source/destination cash changes; total assets and monthly income/expense remain unchanged; self-transfer and insufficient unreserved funds are rejected.
- **Status:** Planned — Not Executed

### TC-011 — Valuation completeness

- **Level:** Unit + integration
- **Requirements:** FR-011
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-011.
- **Expected result:** Any positive unpriced holding yields an incomplete priced subtotal, never an assumed zero value; a stale price remains in the subtotal with a warning; the stale threshold is configurable.
- **Status:** Planned — Not Executed

### TC-012 — Total assets and net-worth estimate

- **Level:** Unit + integration
- **Requirements:** FR-012
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-012.
- **Expected result:** For cash 1000 and an asset valued at 200, both figures equal 1200; the dashboard states liabilities are not tracked; goal reservations add nothing; incomplete prices qualify both figures.
- **Status:** Planned — Not Executed

### TC-013 — Monthly cash-flow reporting

- **Level:** Unit + integration
- **Requirements:** FR-013
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-013.
- **Expected result:** Income 300 and expenses 100 produce savings 200 and a 66.67% display rate; transfers and investments do not change these totals; zero/negative income produces an unavailable rate.
- **Status:** Planned — Not Executed

### TC-014 — Asset distribution

- **Level:** Unit + integration
- **Requirements:** FR-014
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-014.
- **Expected result:** Distribution values sum to the displayed priced subtotal; unknown holdings are listed separately; an empty or zero-value portfolio shows an empty state instead of misleading percentages.
- **Status:** Planned — Not Executed

### TC-015 — Historical trends

- **Level:** Unit + integration
- **Requirements:** FR-015
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-015.
- **Expected result:** Past dates use prices effective no later than that date; earlier dates without prices remain incomplete; corrections refresh affected periods; latest prices are not applied retroactively.
- **Status:** Planned — Not Executed

### TC-016 — Savings goal management

- **Level:** Unit + integration
- **Requirements:** FR-016
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-016.
- **Expected result:** Two simultaneous goals can be saved; invalid targets are rejected; past deadlines are allowed and labeled overdue when underfunded; deleting or archiving a goal explicitly releases its active reservations atomically.
- **Status:** Planned — Not Executed

### TC-017 — Savings reservations

- **Level:** Unit + integration
- **Requirements:** FR-017
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-017.
- **Expected result:** With cash 1000, reserving 700 leaves 300 available; another reservation of 400 is rejected; reservations across goals never exceed each source account cash balance; releases and cash edits preserve this invariant atomically.
- **Status:** Planned — Not Executed

### TC-018 — Goal progress

- **Level:** Unit + integration
- **Requirements:** FR-018
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-018.
- **Expected result:** Reserved 250 against target 1000 gives 25% and remaining 750; progress bars cap at 100% while excess funding is shown separately; released funds immediately reduce progress.
- **Status:** Planned — Not Executed

### TC-019 — Required contributions

- **Level:** Unit + integration
- **Requirements:** FR-019
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-019.
- **Expected result:** For remaining target 900 and three opportunities, the contribution is 300; funded goals return zero; overdue underfunded goals show overdue with no monthly amount; amounts round upward to a minor unit.
- **Status:** Planned — Not Executed

### TC-020 — Spending explanations

- **Level:** Unit + integration
- **Requirements:** FR-020
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-020.
- **Expected result:** A valid approved monthly aggregate can be explained; all displayed financial totals retain their deterministic source values; an unavailable API yields a recoverable error.
- **Status:** Planned — Not Executed

### TC-021 — Goal feasibility explanations

- **Level:** Unit + integration
- **Requirements:** FR-021
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-021.
- **Expected result:** The request includes approved target/progress/contribution summaries; missing history is disclosed; Gemini cannot change the target, reservation, or calculated monthly contribution.
- **Status:** Planned — Not Executed

### TC-022 — Natural-language summaries

- **Level:** Unit + integration
- **Requirements:** FR-022
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-022.
- **Expected result:** A summary is labeled AI-generated and separate from computed figures; portfolio completeness warnings accompany the context; generated text creates no financial records.
- **Status:** Planned — Not Executed

### TC-023 — Financial questions

- **Level:** Unit + integration
- **Requirements:** FR-023
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-023.
- **Expected result:** The question and selected context appear in the preview; no arbitrary tools, SQL, trading, or financial-write capability is supplied to Gemini; the response is labeled explanatory.
- **Status:** Planned — Not Executed

### TC-024 — Per-request AI consent

- **Level:** Integration
- **Requirements:** FR-024
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-024.
- **Expected result:** Canceling the preview makes no API call; editing the question or financial context invalidates prior approval; approval permits one call and cannot be reused by a Streamlit rerun; generated context excludes tokens, account labels, and record notes; the exact user-typed question is visible for approval.
- **Status:** Planned — Not Executed

### TC-025 — Authorized Telegram destination

- **Level:** Integration
- **Requirements:** FR-025
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-025.
- **Expected result:** Missing, group, mismatched, or unvalidated recipient configuration fails closed; a deliberate non-financial connection test confirms the destination; incoming commands are not processed and reveal no data.
- **Status:** Planned — Not Executed

### TC-026 — Scheduled Telegram summaries

- **Level:** Integration
- **Requirements:** FR-026
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-026.
- **Expected result:** A configured due period creates one delivery record; rerunning an acknowledged period does not resend; a missed schedule sends at most the latest due period after restart; timeout ambiguity is surfaced.
- **Status:** Planned — Not Executed

### TC-027 — Goal reminders and updates

- **Level:** Integration
- **Requirements:** FR-027
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-027.
- **Expected result:** A configured reminder includes the selected goal progress, deadline, and deterministic contribution; duplicate runner invocations do not resend acknowledged occurrences; released/deleted goals do not generate stale updates.
- **Status:** Planned — Not Executed

### TC-028 — Notification preferences

- **Level:** Integration
- **Requirements:** FR-028
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-028.
- **Expected result:** No scheduled financial message is enabled by default; configuration requires a timezone, recipient, content preview/approval, and chosen schedule; disabling a rule prevents new attempts, while a network request already in flight may complete and remains visible in delivery status.
- **Status:** Planned — Not Executed

### TC-029 — Consistent local backup

- **Level:** Integration
- **Requirements:** FR-029; NFR-011
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-029.
- **Expected result:** A completed backup opens independently and passes integrity checks; failed writes produce no success message or usable-looking partial backup; active writes cannot create a torn snapshot.
- **Status:** Planned — Not Executed

### TC-030 — Validated restore

- **Level:** Integration
- **Requirements:** FR-030; NFR-011
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-030.
- **Expected result:** Invalid/corrupt/unsupported backups leave the live dataset unchanged; application and runner writers are stopped before replacement; a supported round trip preserves balances, prices, goals, and history.
- **Status:** Planned — Not Executed

### TC-031 — CSV export

- **Level:** Integration
- **Requirements:** FR-031
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-031.
- **Expected result:** Exports carry stable IDs, currency/scale, dates, and exact decimal text; credentials are excluded; spreadsheet-formula text is neutralized and documented; CSV is not advertised as a restore backup.
- **Status:** Planned — Not Executed

### TC-032 — Offline persistence

- **Level:** Integration
- **Requirements:** FR-032; NFR-005
- **Setup and steps:** Use an isolated synthetic dataset; exercise the success and rejection paths in FR-032.
- **Expected result:** After restart all committed records remain; disabled, unreachable, or unconfigured APIs do not block core reads/writes; a failed transaction leaves no partial postings or reservations.
- **Status:** Planned — Not Executed

### TC-033 — Competing reservations and cash debits

- **Level:** Integration
- **Requirements:** FR-008, FR-009, FR-010, FR-017; NFR-008
- **Setup and steps:** Two connections act on cash 1000: one reserves 700 while the other reserves/spends 400.
- **Expected result:** Only an invariant-preserving sequence commits; total reservations never exceed cash and rejection leaves no partial rows.
- **Status:** Planned — Not Executed

### TC-034 — Corrupt and incompatible restore

- **Level:** System
- **Requirements:** FR-030; NFR-011
- **Setup and steps:** Hash a populated live dataset; attempt restore from corrupt bytes and a valid SQLite file with unsupported schema.
- **Expected result:** Both candidates are rejected before replacement; live file hash and computed figures are unchanged.
- **Status:** Planned — Not Executed

### TC-035 — Decimal valuation and aggregate rounding

- **Level:** Unit
- **Requirements:** FR-005, FR-012, FR-014; NFR-012
- **Setup and steps:** At a two-decimal scale calculate 0.10 + 0.20 and two holdings each valued at 0.005 before rounding.
- **Expected result:** Addition is exactly 0.30; half-even rounds each 0.005 holding to 0.00 and summed displayed total is 0.00; calculation order matches BR-002.
- **Status:** Planned — Not Executed

### TC-036 — Cancel and stale AI consent

- **Level:** Integration
- **Requirements:** FR-024; NFR-003
- **Setup and steps:** Prepare a question and preview; cancel. Then prepare another preview and change the underlying summary before send. Finally approve a stable payload, send it, and simulate a Streamlit rerun.
- **Expected result:** Cancellation sends zero requests; changed context invalidates consent; only a newly approved payload can be sent; the consumed approval cannot trigger another call on rerun. Generated context excludes labels/notes, and the question is shown verbatim for approval.
- **Status:** Planned — Not Executed

### TC-037 — Trusted-device network boundary

- **Level:** System
- **Requirements:** FR-001; NFR-001
- **Setup and steps:** Use one explicitly allowed and one denied LAN device against the documented deployment; also inspect default binding.
- **Expected result:** Default bind is loopback; the allowed device can access, the denied device cannot; no public exposure or application login is claimed.
- **Status:** Planned — Not Executed

### TC-038 — Secret and record exclusion

- **Level:** System
- **Requirements:** FR-001, FR-024, FR-031; NFR-002
- **Setup and steps:** Use fake keys, account notes, financial prompts, data files, exports, and backups; inspect git-ignore behavior, tracked files, errors, and logs.
- **Expected result:** Seeded secrets/financial context are absent from logs and tracked files; sensitive paths are ignored and owner-restricted; no real credentials are used.
- **Status:** Planned — Not Executed

### TC-039 — Owner workflow usability

- **Level:** Acceptance
- **Requirements:** FR-007, FR-010, FR-017; NFR-004
- **Setup and steps:** Owner follows only labels/help to enter income, transfer cash, and reserve funds in a populated synthetic dataset.
- **Expected result:** Proposed: each task finishes within three minutes; units, save/error outcomes, preserved input, and empty states are understandable.
- **Status:** Planned — Not Executed

### TC-040 — Atomic failure and restart

- **Level:** Integration
- **Requirements:** FR-006, FR-009, FR-017, FR-032; NFR-005
- **Setup and steps:** Inject failure between postings/reversal/allocation changes before commit; restart after a successful separate commit.
- **Expected result:** Failed operation leaves all logical records unchanged; successful committed data survives restart exactly.
- **Status:** Planned — Not Executed

### TC-041 — Business-layer isolation

- **Level:** Unit
- **Requirements:** FR-012, FR-013, FR-019, FR-032; NFR-006
- **Setup and steps:** Import domain modules and exercise core calculations with no UI or API packages initialized; inject a fixed date.
- **Expected result:** Calculations run without network calls, Streamlit imports, external credentials, or implicit current-clock dependence.
- **Status:** Planned — Not Executed

### TC-042 — Proposed dataset performance

- **Level:** System
- **Requirements:** FR-012, FR-013, FR-017; NFR-007
- **Setup and steps:** On the proposed reference host populate 10,000 transactions, 200 assets, 20 goals; warm once and measure 30 dashboard reads and 30 ordinary writes.
- **Expected result:** At least 95% of reads take at most 2 seconds and 95% of writes at most 1 second; API and browser rendering excluded; report host and measured values.
- **Status:** Planned — Not Executed

### TC-043 — Schema and input integrity

- **Level:** Integration
- **Requirements:** FR-003, FR-004, FR-006, FR-009, FR-017; NFR-008
- **Setup and steps:** Attempt orphan postings/allocations, nonfinite decimals, out-of-range integers, invalid dates, and negative historical holdings through every write entry point.
- **Expected result:** Foreign keys and application validators reject each case atomically; foreign_key_check and integrity_check pass afterward.
- **Status:** Planned — Not Executed

### TC-044 — Clean local deployment

- **Level:** System
- **Requirements:** FR-001, FR-002, FR-032; NFR-009
- **Setup and steps:** On a clean supported Linux host follow installation/configuration instructions without API credentials, write a sample record, and restart.
- **Expected result:** Core launches on loopback and retains the record; the documented procedure has no cloud account dependency.
- **Status:** Planned — Not Executed

### TC-045 — External failure matrix

- **Level:** Integration
- **Requirements:** FR-020, FR-021, FR-022, FR-023, FR-025, FR-026, FR-027, FR-032; NFR-010
- **Setup and steps:** Fake Gemini/Telegram responses: timeout, 429 with Retry-After, 401/403, server error, malformed payload, and disabled adapter.
- **Expected result:** Proposed 15-second timeout is honored; Gemini never auto-retries; Telegram attempts ≤3 for definite transient failures, respects provider delay, and marks ambiguous sends uncertain; no core mutation or secret leak.
- **Status:** Planned — Not Executed

### TC-046 — Backup during writes and recovery rehearsal

- **Level:** Integration + system
- **Requirements:** FR-029, FR-030; NFR-011
- **Setup and steps:** Create a backup while another connection writes; stop writers and rehearse restore on 10,000 transactions with a pre-restore backup.
- **Expected result:** Backup is a consistent committed snapshot; restore preserves relationships and figures and is reversible; proposed restore time ≤10 minutes; record recovery point.
- **Status:** Planned — Not Executed

### TC-047 — Numeric and date boundaries

- **Level:** Unit
- **Requirements:** FR-002, FR-005, FR-006, FR-007, FR-008, FR-016, FR-019; NFR-012
- **Setup and steps:** Try excess fractional digits, 64-bit overflow, NaN/infinity, zero/negative inputs, a non-two-decimal currency, deadline today, year rollover, and overdue goals.
- **Expected result:** Inputs reject rather than silently lose precision; date opportunities follow BR-009; contribution rounds upward, e.g. gap 1.00 / 3 gives 0.34 at scale 2.
- **Status:** Planned — Not Executed

### TC-048 — Unauthorized Telegram and unsupported commands

- **Level:** Integration + system
- **Requirements:** FR-025, FR-026, FR-027, FR-028; NFR-003
- **Setup and steps:** Try missing, group, changed, and mismatched recipient settings; invoke a delivery with a destination different from the validated configuration; send an incoming bot command.
- **Expected result:** No financial content is sent to an unvalidated recipient; destination overrides are rejected; no inbound handler responds with data or performs operations.
- **Status:** Planned — Not Executed

### TC-049 — AI hallucinations and operation requests

- **Level:** Integration
- **Requirements:** FR-020, FR-021, FR-022, FR-023, FR-024; NFR-003
- **Setup and steps:** Return invented totals, SQL-like instructions, or an investment/trade instruction from the fake Gemini adapter.
- **Expected result:** AI text is labeled unverified; authoritative numbers remain unchanged; no tool/SQL/write operation is invoked; logs contain no sensitive prompt.
- **Status:** Planned — Not Executed

### TC-050 — Historical restatement and notification downtime

- **Level:** Integration
- **Requirements:** FR-009, FR-015, FR-026, FR-027
- **Setup and steps:** Correct a backdated event/price; restart the runner after several missed periods and invoke it concurrently twice.
- **Expected result:** Trends use only effective dated prices and show restatement; only the latest due occurrence is considered; one claim wins; acknowledged messages do not repeat and uncertain results remain visible.
- **Status:** Planned — Not Executed

### TC-051 — Atomic opening submission replay prevention

- **Level:** Integration
- **Requirements:** FR-006, FR-032; NFR-005, NFR-008
- **Setup and steps:** In F-002, submit one normalized stock registration/opening/price intent with a stable logical submission key. Replay it, simulate a UI rerun/double submission, retry from a second connection, and replay after reopening the dataset. Reuse the key with changed quantity/price. Separately inject a failure between opening and price writes, then retry the rolled-back command.
- **Expected result:** Identical accepted intent returns the original result with exactly one definition, opening and price set. Changed-payload key reuse rejects without mutation. A failed transaction leaves no partial rows or consumed committed key and can retry once successfully. Distinct deliberate commands get separate identities; equal values alone do not trigger deduplication. The durable guard is reviewed under DEC-016/OQ-007.
- **Status:** Planned — Not Executed

### TC-052 — First Working Dashboard acceptance and recovery

- **Level:** System + acceptance
- **Requirements:** FR-001, FR-002, FR-003, FR-004, FR-005, FR-006, FR-011, FR-012, FR-029, FR-030, FR-032; NFR-005, NFR-008, NFR-009, NFR-011, NFR-012
- **Setup and steps:** Start locally without API credentials; initialize the reporting currency and account; register F-002 holdings through the Streamlit form; inspect the asset list/dated values and restart. Try invalid/nonfinite/overprecision/overflow/future-date inputs and an injected mid-registration failure. Repeat an accepted submission. Add an unpriced holding and an older-price variant. Create a consistent backup, confirm a stopped-writer restore with a safety copy, and try a corrupt/unsupported candidate. Record startup/recovery notes and owner acceptance against M1A-01 through M1A-08.
- **Expected result:** Cash 1000 plus 10 units at 20 gives exactly 1200 before and after restart/restore. Missing prices retain a clearly incomplete 1200 priced subtotal; stale data is dated/warned under the reviewed threshold. Invalid/failed/replayed commands create no partial/duplicate holdings or valuation drift. No API calls occur; no direct balance/unit edit path exists. Valid backup/restore preserves records and history; invalid candidates preserve the live dataset. Evidence explicitly covers the limited first dashboard, not later CRUD/trading/goals/integrations.
- **Status:** Planned — Not Executed

## Prioritization and regression

Run money/validation/ledger cases first, then reservations, persistence/recovery, reporting, and external boundaries. Re-run affected financial regressions after a calculation/schema change; run the complete release suite before calling the Charter release accepted. Network/device and timed usability/recovery checks are manual where automation cannot reproduce the real host boundary. No fixed coverage percentage replaces invariant tests.
