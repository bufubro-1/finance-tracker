# Finance Tracker — User Stories

Status: Planned; none implemented or accepted. Priority refers to the complete Charter release. See [SRS](SRS.md) for authoritative requirements and [RTM](RTM.md) for test coverage. Dependencies below are capability relationships; the backlog supplies execution order.

## Milestone applicability

M-001A at 32 hours delivers opening-only portions of US-001/002/003/004/008/009/020: local startup, basic account/asset creation/listing, atomic openings, initial prices/totals, persistence, and essential recovery. Acceptance is M1A-01 through M1A-08 in the SRS, verified by the milestone test profile including TC-051/052. Purchases/sales, price corrections, CSV and other complete-story scenarios stay later. No whole story or requirement is marked accepted from a partial delivery; M-004 remains 92 hours.

## US-001 — Configure a local dataset and reporting currency

**As a Personal User, I want to configure a local dataset and reporting currency, so that I can use the core without external accounts.**

- **Priority:** Must
- **Related functional requirements:** FR-001, FR-002, FR-032
- **Acceptance criteria:** Given a fresh setup without API keys, when I choose a reporting currency and save a record, then it survives restart and core features work offline.
- **Dependencies:** None

## US-002 — Manage logical accounts

**As a Personal User, I want to manage logical accounts, so that I can organize where my cash and investments are held.**

- **Priority:** Must
- **Related functional requirements:** FR-003
- **Acceptance criteria:** Given an unused account, when I rename or delete it, then the change succeeds; given a referenced account, deletion is refused with an archive explanation.
- **Dependencies:** US-001

## US-003 — Register my asset types and units

**As a Personal User, I want to register my asset types and units, so that I can track cash, currencies, gold, stocks, and funds consistently.**

- **Priority:** Must
- **Related functional requirements:** FR-004
- **Acceptance criteria:** Given an account, when I register each supported asset class, then its type and unit are retained and base cash remains valued at one.
- **Dependencies:** US-002

## US-004 — Record manual holding purchases, sales, and openings

**As a Personal User, I want to record manual holding purchases, sales, and openings, so that I can keep quantities and settlement cash consistent.**

- **Priority:** Must
- **Related functional requirements:** FR-006
- **Acceptance criteria:** Given cash 1000, when I buy an asset for 200 at a price valuing the acquired quantity at 200, then cash is 800, the asset is worth 200, and no expense is created.
- **Dependencies:** US-003

## US-005 — Record income and expenses

**As a Personal User, I want to record income and expenses, so that I can understand my monthly cash flow.**

- **Priority:** Must
- **Related functional requirements:** FR-007, FR-008
- **Acceptance criteria:** Given cash 1000, when I record income 300 and expense 100, then cash is 1200 and the monthly figures contain those entries exactly once.
- **Dependencies:** US-004

## US-006 — Correct or delete financial entries

**As a Personal User, I want to correct or delete financial entries, so that I can fix mistakes without losing the record history.**

- **Priority:** Must
- **Related functional requirements:** FR-009
- **Acceptance criteria:** Given a posted expense 100, when I correct it to 80, then the effective expense is 80 and original/reversal/replacement history remains; repeating the deletion cannot double-refund cash.
- **Dependencies:** US-005

## US-007 — Transfer cash between accounts

**As a Personal User, I want to transfer cash between accounts, so that I can move savings without inflating income or spending.**

- **Priority:** Must
- **Related functional requirements:** FR-010
- **Acceptance criteria:** Given two accounts, when I transfer 100, then one decreases and the other increases by 100 while total wealth and cash-flow totals stay unchanged.
- **Dependencies:** US-004

## US-008 — Maintain dated manual prices

**As a Personal User, I want to maintain dated manual prices, so that I can control the values used for my portfolio.**

- **Priority:** Must
- **Related functional requirements:** FR-005
- **Acceptance criteria:** Given a foreign-currency holding, when I enter a base-currency price, then it is stored with its effective date; a future or invalid price is rejected.
- **Dependencies:** US-003

## US-009 — See asset totals, composition, and valuation warnings

**As a Personal User, I want to see asset totals, composition, and valuation warnings, so that I can understand my portfolio without hiding missing data.**

- **Priority:** Must
- **Related functional requirements:** FR-011, FR-012, FR-014
- **Acceptance criteria:** Given priced cash and an unpriced stock, when I open the dashboard, then I see a priced subtotal and an incomplete warning rather than an apparently complete net-worth figure.
- **Dependencies:** US-004, US-008

## US-010 — Review monthly income, expenses, and savings

**As a Personal User, I want to review monthly income, expenses, and savings, so that I can measure my saving behavior.**

- **Priority:** Must
- **Related functional requirements:** FR-013
- **Acceptance criteria:** Given income 300 and expenses 100, when I view the month, then savings are 200 and savings rate is 66.67%; transfers are excluded.
- **Dependencies:** US-005, US-006, US-007

## US-011 — Review historical financial trends

**As a Personal User, I want to review historical financial trends, so that I can compare periods using the data known for those dates.**

- **Priority:** Must
- **Related functional requirements:** FR-015
- **Acceptance criteria:** Given a price first effective this month, when I view last month, then that price is not applied backward; affected charts refresh after a correction.
- **Dependencies:** US-008, US-010

## US-012 — Create and update several savings goals

**As a Personal User, I want to create and update several savings goals, so that I can plan separate targets and deadlines.**

- **Priority:** Must
- **Related functional requirements:** FR-016
- **Acceptance criteria:** Given two different targets, when I save both, then both remain editable; deleting a funded goal requires confirming the reservation release.
- **Dependencies:** US-001

## US-013 — Reserve and release cash for goals and see progress

**As a Personal User, I want to reserve and release cash for goals and see progress, so that I can avoid promising the same savings twice.**

- **Priority:** Must
- **Related functional requirements:** FR-017, FR-018
- **Acceptance criteria:** Given cash 1000 with 700 reserved, when I try to reserve another 400 or spend 400, then the operation fails unchanged; reserving another 300 succeeds.
- **Dependencies:** US-004, US-012

## US-014 — See required monthly contributions

**As a Personal User, I want to see required monthly contributions, so that I can understand the remaining saving effort.**

- **Priority:** Must
- **Related functional requirements:** FR-019
- **Acceptance criteria:** Given a gap of 900 and three remaining monthly opportunities, when I view the goal, then it shows 300 per month; an overdue unfinished goal shows overdue instead of division by zero.
- **Dependencies:** US-013

## US-015 — Request an approved AI spending explanation or financial summary

**As a Personal User, I want to request an approved AI spending explanation or financial summary, so that I can understand the computed figures in plain language.**

- **Priority:** Must
- **Related functional requirements:** FR-020, FR-022, FR-024
- **Acceptance criteria:** Given a prepared summary, when I cancel its preview, then no Gemini request occurs; when I approve it, only the displayed minimized payload is sent and the result cannot update my records.
- **Dependencies:** US-009, US-010

## US-016 — Request an AI explanation of goal feasibility

**As a Personal User, I want to request an AI explanation of goal feasibility, so that I can understand my deterministic contribution target.**

- **Priority:** Must
- **Related functional requirements:** FR-021, FR-024
- **Acceptance criteria:** Given a contribution target and sparse history, when I approve a feasibility question, then the response carries that limitation and cannot change the target or allocations.
- **Dependencies:** US-014, US-015

## US-017 — Ask financial questions with explicit context approval

**As a Personal User, I want to ask financial questions with explicit context approval, so that I can get explanations while controlling disclosure.**

- **Priority:** Must
- **Related functional requirements:** FR-023, FR-024
- **Acceptance criteria:** Given an edited question, when I send it, then a fresh exact-context approval is required; an instruction to perform a transaction causes no financial write.
- **Dependencies:** US-015

## US-018 — Configure one authorized Telegram destination and report preferences

**As a Personal User, I want to configure one authorized Telegram destination and report preferences, so that I can control where and when financial summaries leave my device.**

- **Priority:** Must
- **Related functional requirements:** FR-025, FR-028
- **Acceptance criteria:** Given disabled notifications, when I validate a private destination and approve chosen report fields and schedule, then only that destination is eligible; group/mismatched destinations are refused.
- **Dependencies:** US-001

## US-019 — Receive scheduled summaries and goal reminders

**As a Personal User, I want to receive scheduled summaries and goal reminders, so that I can stay informed while the local runner is operating.**

- **Priority:** Must
- **Related functional requirements:** FR-026, FR-027
- **Acceptance criteria:** Given an enabled due report, when the runner is invoked twice after acknowledged delivery, then only one message is sent; after downtime only the latest due occurrence is considered.
- **Dependencies:** US-010, US-014, US-018

## US-020 — Back up, restore, and export my records

**As a Personal User, I want to back up, restore, and export my records, so that I can retain control and recover from local data loss.**

- **Priority:** Must
- **Related functional requirements:** FR-029, FR-030, FR-031
- **Acceptance criteria:** Given a valid backup, when I restore it with writers stopped, then balances and goals match; given a corrupt backup, live data is unchanged; CSV exports preserve documented values without credentials.
- **Dependencies:** US-006, US-013
