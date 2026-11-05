# Finance Tracker — Documentation

This documentation establishes requirements, proposed design, delivery planning, and a test strategy before application development. The project is a single-user, local-first modular Python application using Streamlit, SQLite, Pandas, Plotly, optional Gemini, and optional Telegram notifications.

**Status:** Planning. No application code, migrations, database, executable tests, dependency installation, deployment, Git commit, or push was produced by this assignment. All implementation tasks are Not Started; all application test cases are Planned — Not Executed. The existing [Project Charter](CHARTER.md) remains Proposed — Pending Owner Approval.

Readiness decisions in the [Decision Log](DECISION_LOG.md): DEC-017 approves the current Linux environment, Python 3.14.x (initial local target 3.14.8), venv, pip, and pytest. Dependency compatibility and exact compatible dependency versions remain unverified TASK-001 work; report incompatibilities rather than silently changing Python or architecture. DEC-018 authorizes only TASK-001's documented runtime/configuration/startup and relevant documentation/test scope, with integrations disabled by default; execution remains explicitly held. It does not approve financial calculations, database schemas, asset management, Gemini or Telegram features, or the remaining baseline and technical proposals.

DEC-019 preserves and excludes the existing root README.md and docs/CHARTER.md edits from the proposed 17-file baseline: the 13 new documentation files plus four governance files. No staging, commit, push, merge, or branch change is authorized by baseline preparation.

## Structure and reading order

| Order | Document | Purpose |
|---|---|---|
| 1 | [CHARTER.md](CHARTER.md) | Primary source for objectives, boundaries, technology, deliverables, and success criteria. Existing file; not edited by this documentation task. |
| 2 | [DECISION_LOG.md](DECISION_LOG.md) | Confirmed owner choices, proposed design decisions, assumptions, and open approvals. |
| 3 | [requirements/SRS.md](requirements/SRS.md) | Testable functional/non-functional requirements, terminology, constraints, and financial rules. |
| 4 | [requirements/USE_CASES.md](requirements/USE_CASES.md) | Actor interactions and editable UML use-case diagram. |
| 5 | [requirements/USER_STORIES.md](requirements/USER_STORIES.md) | User benefits, acceptance scenarios, and capability dependencies. |
| 6 | [design/ARCHITECTURE.md](design/ARCHITECTURE.md) | Component responsibilities, interfaces, data flows, deployment, and security boundaries. |
| 7 | [design/DATA_MODEL.md](design/DATA_MODEL.md) | Proposed relational schema, integrity/history rules, precision, and editable ER diagram. |
| 8 | [planning/WBS.md](planning/WBS.md) | Deliverable hierarchy and work-package completion criteria. |
| 9 | [planning/PROJECT_SCHEDULE.md](planning/PROJECT_SCHEDULE.md) | Preliminary effort, relative weeks, milestones, dependencies, and editable Gantt. |
| 10 | [planning/BACKLOG.md](planning/BACKLOG.md) | Actionable tasks, dependencies, acceptance criteria, estimates, and optional future candidates. |
| 11 | [planning/RISK_REGISTER.md](planning/RISK_REGISTER.md) | Qualitative risk matrix, mitigations, contingencies, and review triggers. |
| 12 | [testing/TEST_PLAN.md](testing/TEST_PLAN.md) | Planned verification strategy and cases; no execution claims. |
| 13 | [requirements/RTM.md](requirements/RTM.md) | Cross-document requirement coverage and explicit implementation/evidence gaps. |

The 13 documentation deliverables are this index, the decision log, four requirements documents, two design documents, four planning documents, and one test plan. The existing Charter is an additional preserved source document.

## Identifiers and relationships

| Prefix | Meaning / definition location |
|---|---|
| FR-### / NFR-### / BR-### | Functional requirements, non-functional requirements, business rules — SRS. |
| US-### / UC-### | User story / use case — respective requirements document. |
| CMP-### | Planned component — architecture catalog. |
| TC-### | Planned test case — test plan. |
| 1.0, 1.1, 2.1.1, … | WBS phase / package / split leaf; parent budgets are non-additive — WBS. |
| TASK-###, TASK-###A/B / FUT-### | Original task or completion rollup, executable split / future candidate — backlog. |
| M-###, M-001A / M1A-01–M1A-08 | Planned milestone / scoped first-dashboard acceptance checks — schedule and SRS. |
| RISK-### | Risk — risk register. |
| DEC-### / ASM-### / OQ-### | Decision / assumption / open question — decision log. |

IDs are stable and unique within their namespace. Repeating an ID as a reference is expected; duplicate definitions are not. Use a new ID for a new concept and mark a removed concept superseded rather than recycling its number.

The Charter establishes scope. Requirements specify behavior and constraints. Stories explain user value; use cases describe interactions. Design components and entities show the proposed solution. WBS/backlog/schedule organize future work. Test cases define evidence to collect later. The RTM links these layers; a mapping or document is not proof that a requirement is implemented or a test has passed.

Must/Should/Could represent delivery priority. All current baseline FRs and NFRs are Must for the complete Charter release; optional future backlog items use Should/Could. Runtime-optional Gemini and Telegram remain complete-release deliverables. Approved M-001A delivers an opening-only first working dashboard at 32 hours / end of Week 4. M-004 remains the first usable complete core after phase 4, at 92 hours / mid-Week 12, with goals, full tracking/reporting, backup/restore/export and safe local access.

## Baseline summary

- 32 functional requirements, 12 non-functional requirements, and 15 business rules.
- 20 user stories, 17 use cases, 10 planned components, and 52 planned application test cases, all unexecuted.
- 21 original task IDs retained: four are non-additive completion rollups and their eight A/B children produce 25 executable leaves overall, plus six separate future candidates.
- Approved preliminary baseline: 152 hours at eight hours/week = 19 development weeks. M-001A is 32 cumulative hours; M-004 is unchanged at 92 hours; M-002 moves from 48 to 54 hours. Uncertainty range: 128–192 hours / 16–24 weeks. No calendar start date or deadline is approved.
- Confirmed choices: one reporting currency/manual base-currency prices; assets-only estimate; network restrictions; base-cash goal reservations; per-request AI consent; notifications-only Telegram.

## Documentation quality review

Documentation review updated for approved DEC-015 on 2026-11-05. These results concern documentation only; no application tests run:

| Check | Result |
|---|---|
| Requested structure | All 13 new documents present; no application files created. |
| Identifier definitions and references | Unique definitions and all references resolved across the documented namespaces. |
| Acceptance criteria and required fields | All 32 FRs, 12 NFRs, 20 stories, 17 use cases and 25 executable task leaves have their required fields; all four rollups retain completion criteria. |
| Functional traceability | All 32 FRs map to stories, use cases, planned components, planned tests and executable WBS/backlog leaves; the M1A-01–M1A-08 profile maps scoped checks to early leaves without claiming complete FR acceptance. |
| Non-functional traceability | All 12 NFRs map to components, executable tasks and planned cases; SRS/RTM/test-case references agree, including TC-051 replay and TC-052 first-dashboard acceptance. |
| Dependencies and estimates | Requirement/story/task dependency graphs and serial order are checked; WBS/backlog/schedule agree; 25 leaf estimates total 152 hours / 19 weeks. Four rollup estimates are excluded. M-001A/M-004/full release remain 32/92/152 hours. |
| Links, tables, and examples | Local document links resolve; table widths/fences checked; financial examples and Gantt duration arithmetic recalculated. |
| Charter and scope review | D1–D6 represented; excluded/future capabilities separated; derived technical policies explicitly proposed rather than silently approved. |
| Diagram review | Component/data-flow/deployment and ER text reviewed; 11 ER entities match their catalog; UML use cases match specifications. Source-level checks only: no Mermaid/PlantUML renderer was available. |
| Status and preservation | Tasks remain Not Started; tests remain Planned — Not Executed. The root README, Charter and repository configuration match pre-update hashes; existing edits were preserved. Only the 13 authorized documentation artifacts were updated. |

No missing planned traceability cell is intended; the updated cross-reference and budget checks are recorded below. Every requirement still has an implementation/verification evidence gap because application development has not begun. No application test has been executed. The temporary documentation-check scripts are outside the repository and are not application deliverables.

Known source issue: concurrent edits to the existing root README and Charter appeared during drafting. The Charter retains two alternate-name prose references; all new artifact titles use Finance Tracker under confirmed DEC-001. These existing files were not edited by this task. DEC-015 records the milestone/schedule approval. DEC-017 resolves OQ-004's runtime selection with compatibility verification pending; DEC-018 partially addresses OQ-001 for TASK-001 only. The rest of OQ-001, OQ-002/003/005/006/007, and ASM-001 through ASM-005 retain their existing unresolved/unvalidated status where applicable.

## M-001A consistency and conflict review

| Topic | Result / required action before implementation |
|---|---|
| Scope and architecture | The early dashboard is a subset of existing Charter D1/D2/D6 capabilities, using the same monolith, exact calculations, ledger and SQLite boundary. No scope or stack conflict was found. No application code/schema was created. |
| Earlier dependency conflict | The original full TASK-007/008 dependency on TASK-006 blocked early delivery. A/B children now distinguish safe opening-only prerequisites from expanded ledger/recovery acceptance; parent completion still requires both children. |
| Accounting and milestone gates | All original parent budgets stay fixed. The serial leaf schedule reaches M-001A at 32 h, M-002 at 54 h, M-003 at 68 h, M-004 at 92 h and M-007 at 152 h. No parent is counted again. |
| Acceptance and status | Eight explicit first-dashboard checks and a Definition of Done cover atomic openings, exact arithmetic, validation, SQLite restart, replay prevention, incomplete valuation and safe backup/restore. All 52 application cases remain Planned — Not Executed; all task leaves/rollups remain Not Started. |
| Technical decision boundary | Duplicate prevention is approved; DEC-016's proposed submission-key/fingerprint fields are a compatible schema refinement, not an approved/implemented migration. DEC-017 approves the runtime selection; verify dependency compatibility during TASK-001 after the execution hold is lifted. Resolve OQ-007 before TASK-003/005A, OQ-002 before financial semantics, the stale-price setting before TASK-008A, and backup inputs before personal data at TASK-007A. |
| Estimate risk | TASK-007A's 2 h is an allocation, not permission to omit recovery validation or a safety copy. A failed safety check blocks M-001A and requires replanning; no hidden extra hours are added. |
| Carry-forward review gaps | Referenced asset-unit edits need a policy before persistent semantics; no such edits are exposed at M-001A. Explanation-only AI handling and explicit notification-recovery acceptance remain later-phase review actions in the decision log. Their full-release coverage is not claimed complete. |
| Diagram validation | Editable Gantt durations and milestone boundaries are checked arithmetically; ER entity/attribute and component references are source-reviewed. Rendering remains unavailable without installing tools, which this task does not do. |

Validation status: **Passed** for document identifiers/references, required fields, local links, tables/fences, leaf/rollup budgets, WBS/backlog acceptance alignment, dependency graphs and serial order, all eight milestone positions, scoped acceptance/test mappings, protected-file hashes, and Gantt source arithmetic. No missing planned mapping or conflicting cumulative target was found. These are documentation checks, not application test results. Development readiness remains **Ready with Conditions** at the recorded policy gates; all application tests remain unexecuted.

## Maintenance and open decisions

OQ-001 remains open for the Charter and baseline outside DEC-018's limited TASK-001 approval. Review OQ-002/003/005/006/007 at their existing task gates: monetary/history policies, proposed thresholds, notification recovery, backup operating policy, and the persistent opening-replay mechanism. OQ-004's runtime selection is approved by DEC-017; dependency compatibility remains unverified until TASK-001. The actual reporting currency, timezone, recipient, and schedules are runtime selections, not invented personal defaults.

For a change, start with the Charter/decision record and SRS, then update affected stories/use cases, model/components, RTM, tasks/dependencies, tests, risks, and estimates together. Keep proposed/confirmed/implemented/verified status separate. The next implementation task is TASK-001, runtime skeleton and local configuration; this assignment does not start it.
