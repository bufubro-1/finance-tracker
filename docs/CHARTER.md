# Finance Tracker — Project Charter

Status: **Owner-approved Savings and Wealth MVP direction and 264-hour planning baseline; revised document pending human review.** Approval comes from the owner's scope/prototype approval and documentation-revision instruction recorded in [Decision Log](DECISION_LOG.md). It does not authorize application implementation or protected Git/deployment operations.

## Purpose and users

Finance Tracker helps a small invited group understand savings, tracked wealth, investment holdings and progress toward goals through simple manually maintained information. It minimizes ongoing data entry: users need not record each expense, purchase, trade or financial transaction.

User owns private accounts, observations, profiles and reports. Admin manages membership and sanitized system health without application access to Users' financial records. The host/database operator is a separate operational trust boundary; application privacy does not prevent an operator with host access from reading backups or databases.

## Initial release deliverables

| Deliverable | Outcome |
|---|---|
| D1 — Usable wealth dashboard | Current cash balances/holdings, dated prices, composition, historical snapshots, freshness and incomplete-value labels. |
| D2 — Simple financial maintenance | Manual balance/quantity updates with optional savings contributions/withdrawals recorded once; preserve observation revisions and show unknown attribution when data is insufficient. |
| D3 — Savings goals | Account-linked goal progress and indicative monthly saving without locked funds. |
| D6 — Project documentation | Actual setup, target architecture, workflows, privacy/limitations and operator deployment/recovery procedures. |
| D7 — Private monthly reporting | Immutable prior-calendar-month reports inside authenticated application; configurable schedules and generic advance reminder emails. |
| D8 — Membership and privacy | Invite-only email/password accounts; strict Admin/User permissions, User isolation, required Admin MFA, session controls and private exports. |
| D9 — Optional financial profile | Self-reported monthly income/expense estimates with explicit review dates, separate from actual balances and savings. |
| D10 — Recoverable self-hosted platform | PostgreSQL, verified backup/restore, CI, intended Pi/CasaOS/Compose/Tunnel setup and controlled manually authorized deployment. |

D4 retains its original Gemini deliverable identity for the later release; D5 retains its original Telegram identity as deferred, outside current commitments. Neither ID is reused for email or reporting. D1/D2/D3/D6 preserve their surviving purposes with explicitly revised scope; D7–D10 are new deliverables. Original complete wording remains at Git revision `5052b5b`.

## Delivery and release boundaries

Deliver an **Early Working Prototype (M-009) at 16 remaining development hours**: locally running Django, standard development authentication, clear Dashboard/Accounts navigation, readable account cards and intuitive account creation/balance viewing using synthetic data. Use simple server-rendered templates and minimal CSS, without a separate frontend framework. Loopback only; disposable development SQLite via Django ORM is permitted for this milestone. Prototype work is reused and included in the total.

All intermediate demonstrations use synthetic data. Before any real users or sensitive data: complete authentication, ownership authorization, Admin MFA, privacy, PostgreSQL integrity, recovery, system verification and reviewed deployment gates at M-007; obtain separate operational authorization. Passing the prototype or foundation milestone grants no exception.

Remaining development baseline: **264 hours / 33 development weeks at 8 hours/week**, including the prototype's 16 hours. Uncertainty range 224–336 hours / 28–42 weeks; no calendar start or deadline is approved. Documentation-revision effort and TASK-001's completed historical scope are excluded. See [schedule](planning/PROJECT_SCHEDULE.md) for leaf accounting and milestones.

## Architecture and intended environment

Python modular monolith, Django server-rendered presentation, deterministic independent Decimal/integer domain services and PostgreSQL. Intended host: **Raspberry Pi 5 (8 GB), CasaOS, Docker Compose, Cloudflare Tunnel with HTTPS**. App, database, scheduled command and tunnel remain a small single-host deployment. ARM64 images, OS/CasaOS compatibility, supported versions and operating procedures are later verification tasks; none is implemented or claimed compatible here. Keep the approved Python 3.14.x development selection unless the owner explicitly revises it.

Core financial calculations and persistence work without Gemini/SMTP. Remote use depends on host/WAN/Tunnel availability. Cloudflare handles application traffic in transit; SMTP receives addressing and generic notification content. These are documented dependencies, not a promise of browser-offline operation.

## Financial and scope constraints

- One reporting currency per User, fixed after first financial record; foreign units receive manual reporting-currency prices. No automatic FX or prices.
- Track assets only and label liabilities as excluded. Opening balances, profile estimates, internal transfers and goal links never create new savings or duplicate wealth.
- Current balance/quantity observations are authoritative inputs; optional movements explain changes, not additional postings. No general accounting ledger is required.
- Show change attribution as unknown when movement completeness, comparable coverage or valuation quality is insufficient. No automatic investment-profit or return-rate claims.
- Goal-linked accounts support at most one active goal each. Goal progress tracks value and may fall; funds remain withdrawable.
- Reports remain authenticated; emails carry no financial details. Stale or absent updates never block generation.

## Later enhancements and exclusions

Gemini savings planning/explanations are a later 24-hour planning package outside the 264 hours: deterministic Python figures remain authoritative, each minimized exact payload/question needs explicit one-call approval, and personalized security buy/sell recommendations are excluded. Telegram is a deferred candidate, not a committed release. Detailed expense categorization, transaction ledgers, advanced trade/cost-basis records, cash reservations, automated prices/FX, forecasting and advanced analytics require future selection and approval.

No banking integration, automatic payments/trades, public registration, commercial service, debt accounting or mobile application is committed. Avoid unnecessary services, brokers and frontend complexity.

## Success and governance

Success requires an owner demonstration of synthetic prototype navigation/account creation without reading implementation details; the released User can maintain holdings, understand qualified wealth/contributions, track goals and read monthly reports. Other Users and Admin must be unable to access private records; committed data must survive restart and verified recovery. Release acceptance requires actual evidence for every mandatory requirement and owner acceptance; none of that future evidence is claimed here. TASK-001 remains accepted; future tasks/milestones remain Not Started.

Owner chooses priorities and policies; developer implements scoped tasks; User maintains financial inputs; operator maintains host/recovery. Use [AGENTS.md](../AGENTS.md), [BRANCH.md](../BRANCH.md), [preparation](TASK_PREPARATION.md) and [workflow](DEVELOPMENT_WORKFLOW.md). Each task and restricted operation needs its applicable authorization. This documentation revision stops at the Human Review Gate.
