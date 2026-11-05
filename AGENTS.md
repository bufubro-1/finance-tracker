# Finance Tracker — AI Agent Instructions

## Project Context

Finance Tracker helps one user track assets, income, expenses, and savings goals. It is a local-first Python modular monolith: Streamlit UI, local SQLite storage, Pandas for presentation data, and Plotly charts. Gemini explanations and Telegram notifications are optional integrations; core financial workflows must work offline without either integration.

Start with the [documentation index](docs/README.md) and [Project Charter](docs/CHARTER.md). Requirements, design, delivery work, and verification are documented in the sources below. Use **Finance Tracker** in new artifacts under DEC-001 in the [Decision Log](docs/DECISION_LOG.md).

At governance creation, application development is Not Started: no application, migrations, dependency manifest, or executable test suite exists. Planned application tests are unexecuted. The Charter remains Proposed — Pending Owner Approval; DEC-015 approves the first-dashboard milestone and schedule, not every technical proposal. Governance approval does not change these product-document statuses.

## Source of Truth

Read relevant documents in this order:

1. Approved project decisions in the [Decision Log](docs/DECISION_LOG.md) and constraints in the [Charter](docs/CHARTER.md).
2. [Software Requirements Specification and business rules](docs/requirements/SRS.md), supplemented by linked stories and use cases.
3. [Architecture](docs/design/ARCHITECTURE.md) and [data model](docs/design/DATA_MODEL.md).
4. [Requirements Traceability Matrix](docs/requirements/RTM.md).
5. [Development backlog](docs/planning/BACKLOG.md), [WBS](docs/planning/WBS.md), and [test plan](docs/testing/TEST_PLAN.md).

Respect each decision's approval status. Proposed mechanisms and thresholds are not approved merely because a lower-level document uses them. If sources conflict, report the specific conflict and obtain clarification before implementing affected behavior; do not silently select a convenient interpretation. Resolve recorded approval points at their task gates. These instructions govern development conduct and add no product requirements.

## Task Execution Workflow

For every development task:

1. Identify its actual backlog task, dependencies, and unresolved decision gates. Use executable leaves, including A/B subtasks, rather than implementing an entire rollup accidentally.
2. Read its functional requirements, applicable non-functional requirements/business rules, and acceptance criteria.
3. Inspect affected code and tests; report absent prerequisites accurately.
4. Prepare a brief implementation plan and identify appropriate validation. Follow the [branch workflow](BRANCH.md): every implementation task uses an appropriate task branch.
5. Implement only the requested scope; preserve unrelated work and uncommitted changes.
6. Add or update relevant tests based on requirements and financial invariants. Documentation-only changes need relevant document checks rather than invented application tests.
7. Execute appropriate validation using isolated synthetic data. Record actual commands, outcomes, and checks not run with reasons.
8. Report changes, task/requirement references, and test results. Prepare the diff for human review; follow [CONTRIBUTING.md](CONTRIBUTING.md).
9. Identify remaining issues, limitations, and any approval or documentation updates needed.

For authorized documentation or maintenance work with no backlog entry, reference the owner's request and state that no task ID applies; do not invent IDs or edit the backlog without authorization.

Do not mark a task, requirement, test case, or milestone complete without implementation and verification evidence appropriate to its acceptance criteria. Partial milestone coverage does not complete broader requirements. AI-generated changes require human review. A Pull Request (PR) is optional; without one, local diff review and acceptance-criteria verification are mandatory before merging. Never create PRs automatically; create one only on explicit owner request.

## Implementation Principles

- Follow the documented modular monolith and keep UI, services, persistence, and external adapters at their documented boundaries.
- Keep financial calculations deterministic and independently testable. Supply dates/clocks explicitly where needed.
- Use precise Python Decimal arithmetic for monetary calculations and exact integer minor units where documented. Binary floats must not enter authoritative calculations or financial persistence; chart conversions are presentation only.
- Preserve transaction history, atomic writes, referential integrity, and recoverability. Review the proposed precision, rounding, correction, and replay mechanisms at their recorded gates rather than silently approving them.
- Prevent double-counting of assets, transfers, opening holdings, and savings allocations. Goal reservations earmark existing cash and never increase total assets.
- Keep Gemini and Telegram optional at runtime and isolated from core logic. They remain later complete-release deliverables under the existing plan.
- Do not introduce unnecessary frameworks, services, infrastructure, or dependencies.

## Security Rules

- Never commit API keys, credentials, personal financial records, databases, exports, or backups. Respect existing ignore rules and use synthetic fixtures.
- Never send financial context to Gemini without explicit request-specific approval of the exact minimized payload and question. Changed payloads require new approval; approval permits one call. Do not log sensitive prompts or credentials.
- Never expose Streamlit directly to the public internet. Default to loopback; trusted LAN access requires the documented network restrictions. Admitted devices have full access; do not imply an application login exists.
- Never perform financial transactions automatically, including payments, trades, or investment actions. Manually recording financial events is governed by the documented validation and persistence rules.
- Restrict Telegram delivery to the explicitly configured and validated private recipient and approved content/schedules. Initial Telegram behavior is notifications only: no inbound command processing, polling, or webhook.
- Keep external integrations isolated from authoritative financial logic. Gemini output cannot execute SQL, invoke financial-write tools, or alter computed figures or records.
- Use fakes for integration tests. Live checks require explicit owner consent, synthetic payloads, and owner-supplied credentials; never use personal datasets or destinations by default.

## Agent Restrictions

Without explicit project-owner authorization for the action, agents must not:

- Commit changes, push to remote repositories, or merge branches, including local and squash merges.
- Delete branches or rewrite Git history, including rebases, resets, and amended commits that rewrite existing commits.
- Execute destructive database operations, such as dropping data, replacing a dataset, or running destructive migrations.
- Modify approved requirements, Charter constraints, or architecture decisions.
- Introduce major dependencies or architectural changes.
- Deploy the application.

An instruction to implement a task, a workflow example, or approval of an implementation plan does not itself authorize commits, pushes, or merges. Do not discard, overwrite, or automatically stash unrelated work. Report needed protected-document changes and obtain authorization before editing them. Never create PRs automatically.

Never claim that a change was tested unless the stated test was actually executed. Distinguish document checks, automated application tests, manual checks, and owner acceptance; report failures and omissions plainly.

### Development Workflow

For every implementation task, read and follow `docs/DEVELOPMENT_WORKFLOW.md` before making changes.

The workflow defines the standard task lifecycle, including requirements analysis, Git isolation, implementation, testing, review preparation, human approval, committing, and merging.

Follow the existing authorization restrictions in this file and `BRANCH.md`.

Do not interpret workflow instructions as permission to perform restricted Git operations.

Stop at the Human Review Gate unless the project owner explicitly authorizes the next operation.


### Task Preparation

Before beginning a new implementation task, follow `docs/TASK_PREPARATION.md`.

Perform a read-only readiness assessment covering requirements, dependencies, approved decisions, Git state, implementation approach, and test obligations.

Report readiness as Ready, Ready with Conditions, or Blocked.

Preparation does not authorize implementation or Git operations.

Once the project owner approves implementation, follow `docs/DEVELOPMENT_WORKFLOW.md` and the existing governance rules.

Never automatically proceed to the next backlog task.
