# Finance Tracker — Documentation

Status: Savings and Wealth MVP scope, prototype strategy, intended deployment and **264-hour remaining development baseline approved by the owner**; this revised document set awaits human review. Documentation work is authorized under DEC-026 and is not application/infrastructure implementation.

## Read in this order

| Document | Purpose |
|---|---|
| [Decision Log](DECISION_LOG.md) | Approval/supersession history, open task gates and TASK-001 evidence. |
| [Charter](CHARTER.md) | Savings/wealth outcome, deliverables, constraints and release boundary. |
| [SRS](requirements/SRS.md) | Current/deferred FR/NFR/BR requirements and prototype/dashboard acceptance. |
| [User Stories](requirements/USER_STORIES.md) | User/Admin/Operator benefits and acceptance. |
| [Use Cases](requirements/USE_CASES.md) | Workflows and role boundaries. |
| [Architecture](design/ARCHITECTURE.md) | Modular monolith, services, prototype and intended deployment. |
| [Data Model](design/DATA_MODEL.md) | Observations, movements, snapshots, ownership and goal links. |
| [RTM](requirements/RTM.md) | Current/deferred traceability and scoped evidence. |
| [Backlog](planning/BACKLOG.md) | Executable leaves, dependencies, gates, historical task dispositions. |
| [WBS](planning/WBS.md) | Deliverable completion and non-additive budgets. |
| [Schedule](planning/PROJECT_SCHEDULE.md) | 264-hour baseline, prototype allocation, serial order and milestones. |
| [Test Plan](testing/TEST_PLAN.md) | Planned verification and separate historical evidence. |
| [Risk Register](planning/RISK_REGISTER.md) | Open risks and planned mitigation/recovery. |
| [Setup](SETUP.md) | Actual unchanged runtime commands, clearly separated from target. |
| [Task Preparation](TASK_PREPARATION.md) | Read-only readiness before each new task. |
| [Development Workflow](DEVELOPMENT_WORKFLOW.md) | Authorized implementation, verification and Human Review Gate. |

## Current state and release boundary

**Current acceptance update:** M-009 is Completed — Accepted on prototype revision `6c937a6`; the closure proposal is prepared against current main `a338168`, which also includes separately accepted TASK-022B and its recorded 221 passing regressions. See the [closure record](testing/M-009_CLOSURE.md). Earlier documentation-revision and task-review narratives are retained as historical snapshots; their implementation/status statements are superseded by these acceptance records. Release security, PostgreSQL, backup/recovery, deployment and real-user admission remain open.

Only TASK-001 is accepted/integrated: `5052b5b` records accepted `475492a`, 58 pytest passes and successful pip check on Linux x86_64/Python 3.14.8. These historical results were not rerun during this documentation revision. The unchanged current application is a Streamlit runtime/configuration shell, not a Django or financial application. No schema/migration, intended-host support, infrastructure, CI or deployment is claimed.

M-009 delivers a clean usable local Django slice at 16 remaining hours: Dashboard/Accounts navigation, readable cards, intuitive account form, standard development authentication and disposable synthetic SQLite. Its 8+4+4 hours are reused from existing packages. All intermediate work remains synthetic; full authentication, authorization, Admin MFA, privacy, PostgreSQL integrity, recovery and release/deployment verification precede real users or sensitive data at M-007.

Future target: Django/PostgreSQL on Raspberry Pi 5 (8 GB), CasaOS, Docker Compose and Cloudflare Tunnel/HTTPS. Compatibility/versions/storage and operational setup remain later tasks. No unnecessary frontend framework or distributed infrastructure is required.

MVP centers on current balances/holdings, simple optional savings movements, historical snapshots, account-linked goals, optional estimates and monthly private reports/reminders. Detail ledgers, expense categories, advanced trades and cash reservations are deferred. Gemini is a later 24-hour package with one-call exact consent; Telegram is not committed. Change attribution is unknown when data cannot support it.

## Identifiers and history

FR/NFR/BR are defined in SRS; US/UC in their documents; CMP in Architecture; TC in Test Plan; TASK/FUT in Backlog; WBS packages in WBS; M milestones in Schedule; DEC/ASM/OQ in Decision Log; RISK in Risk Register. IDs are stable: retained references are not new definitions and superseded concepts are not recycled. Original baseline and complete prior wording remain in Git revision `5052b5b`; Decision Log preserves every historical DEC-001–019 record.

New prototype ID M-009 and reporting ID M-008 do not reuse existing milestone meanings. P1-01–P1-06 and W1-01–W1-04 define current scoped acceptance; old M1A-01–M1A-08 and TC-051/052 remain historical/superseded, not passed. TASK-004A is now a non-additive parent of TASK-004A1/004A2; new tasks start at TASK-022. TASK-001 remains completed under its original scope; later leaves are not silently completed.

## Revision readiness and review record

- **Request / task:** Owner-approved documentation revision; no task ID applies. Application tasks listed here are future work.
- **Baseline / branch / checkout:** `5052b5b`; `docs/product-architecture-revision`; original clean checkout. Two existing other worktrees were inspected and left untouched. Local main was six commits ahead of recorded origin/main; no fetch, so remote freshness is unverified.
- **Authorization:** Owner approved scope, 264 h and 16 h prototype allocation, added usable interface and intended CasaOS/Compose environment, and explicitly authorized protected documentation/governance edits. No staging/commit/push/PR/merge/deploy or application/infrastructure work.
- **Readiness:** Ready with Conditions for documentation; implementation gates stay open for precision/replay, thresholds, identity recovery, schedules, backup policy, hardware/runtime compatibility and provider setup.
- **Review status:** Prepared for human review after document validation. Owner acceptance of this exact diff is pending; no application task is started by this report.

## Revision changes and actual validation

Changed 18 Markdown files: Charter, Decision Log, SRS, Use Cases, User Stories, Architecture, Data Model, RTM, WBS, Project Schedule, Backlog, Test Plan, Risk Register, this index, root README, Setup, AGENTS.md and CONTRIBUTING.md. The 13 requested product/planning artifacts and five supporting documents are the complete changed-file boundary.

- Replaced ledger-driven MVP requirements with manual balance/holding observations, simple movement annotations, immutable snapshots, account-linked goals and optional profile estimates. Unsupported attribution stays unknown; reports generate with stale/missing data and emails contain no financial details.
- Preserved Django/PostgreSQL, invite-only membership, Admin/User privacy, required Admin MFA and mandatory real-data release gates. Recorded Pi 5 (8 GB), CasaOS, Docker Compose and Cloudflare Tunnel/HTTPS as intended, unverified later deployment work.
- Added M-009/P1-01–P1-06 clean usable prototype criteria and allocated 8+4+4 hours from existing work. Twenty-nine remaining MVP leaves total 264 hours; 16 prototype +248 subsequent hours. Later Gemini is a separate 24-hour package. Original task/requirement/WBS identities and historical decision wording/status/consequences are retained or explicitly retired.
- Reconciled TASK-001's accepted status and separated its historical test evidence from new planned requirements/cases. Existing runtime setup commands remain intact beneath a current-state preface.

Document checks executed on 2026-11-05 against this branch:

| Command / check | Actual result |
|---|---|
| `python3 -B /tmp/check_finance_docs.py` | Passed: 22 tracked Markdown files, 99 resolving local links, balanced fences/tables and unique canonical definitions across 13 checked identifier namespaces. Temporary checker/metadata live outside the repository. |
| Functional/nonfunctional RTM checks within that command | Passed: 40 active FRs (35 MVP and five later Gemini), 11 deferred FRs and 13 NFRs have appropriate current or historical mappings. Selected tests declare their mapped requirements; active tasks never depend on deferred leaves. |
| Schedule/WBS/backlog checks within that command | Passed: dependency order, matching acceptance criteria, executable-leaf budgets, non-additive parents, prototype allocation and all eight current milestone positions. M-009/001/001A/002/003/004/008/007 are 16/106/128/134/142/168/204/264 remaining hours. |
| Historical/preservation checks within that command | Passed: all 19 original decision wordings/statuses/consequences and prior identifier references preserved; unchanged tracked files byte-match baseline. Agent restricted-operation rules and contribution review/commit rules preserved. |
| Diagram source/arithmetic review | ER catalog has 21 entities; references resolve. Gantt spacing recalculates to 231 days /33 weeks at eight effort hours/week. This is source review, not renderer execution. |
| Added-diff credential-signature scan and manual scope/content review | Six credential-signature patterns found zero matches; examples are synthetic. No application, test, dependency, CI, infrastructure or workflow file changes. |
| `git diff --check` | Passed; no whitespace errors. |
| `git status --short --branch`, branch/HEAD/staging checks | Only the 18 intended Markdown files modified on `docs/product-architecture-revision`; HEAD remains `5052b5b`; nothing staged or committed. |

Not run: application tests or `pip check` (documentation-only change; no new runtime claims); Django/PostgreSQL/Pi/CasaOS/Docker/Cloudflare/SMTP/Gemini checks (not implemented or authorized here); Mermaid/PlantUML rendering (`command -v mmdc`, `command -v mermaid` and `command -v plantuml` found no renderer); remote fetch (freshness remains unverified). The recorded 58 TASK-001 passes remain historical.

Remaining decisions are OQ-002/003/005/006/007/008/009/010/011 at their task gates: financial limits/revision/replay policy, numerical thresholds, scheduler behavior, backup operations, intended-host compatibility, providers/domain and identity/MFA/later-AI details. They do not block review of this documentation revision, and they are not silently approved by it. **Stopped at Human Review Gate; acceptance of the current diff is pending.** No application task, staging, commit, push, PR, merge or deployment follows automatically.
