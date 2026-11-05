# Finance Tracker — AI Agent Instructions

## Project Context

Finance Tracker is an invite-only self-hosted savings, wealth and investment portfolio tracker. Approved target: Python modular monolith, Django server-rendered UI and PostgreSQL; intended host Raspberry Pi 5 (8 GB), CasaOS, Docker Compose and Cloudflare Tunnel/HTTPS. Implementation and compatibility verification remain later tasks. Use **Finance Tracker** under DEC-001 and start with the [documentation index](docs/README.md), [Charter](docs/CHARTER.md) and [Decision Log](docs/DECISION_LOG.md).

Track manually maintained balances/holdings, simple savings contributions/withdrawals, snapshots, account-linked goals, optional estimated profile and monthly private reports with generic email reminders. Do not require detailed expense/trade ledgers, transaction categorization or cash reservations. Report unsupported change attribution as unknown. Gemini is later and request-approved; Telegram is deferred.

TASK-001 is accepted/integrated at `5052b5b`; its current Streamlit runtime shell and focused tests are historical implemented scope. Django, financial persistence, infrastructure and the remaining tasks are not implemented by this documentation revision. Do not reopen TASK-001 or claim its recorded 58 tests were rerun. Approved remaining planning baseline: 264 h at 8 h/week, including a 16 h prototype allocated from existing leaves.

M-009 is a local synthetic Django prototype with standard development authentication, clean navigation/cards/form and disposable SQLite via ORM. All intermediate demonstrations use synthetic data. Full authentication, authorization, Admin MFA, privacy, PostgreSQL integrity, recovery and deployment/system verification remain mandatory release gates before real users or sensitive data. Application Admin never receives financial-record access; host/database operator is a separate trust boundary.

The owner authorized this protected-document revision only under DEC-026. Revised artifacts await human review; scope/estimate approval does not authorize app/infrastructure implementation, commits, pushes, merges or deployment. Earlier baseline approval/exclusion statements are historical and superseded as recorded in the Decision Log.

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

1. Identify its actual backlog task, dependencies, and unresolved decision gates. Use executable leaves, including A/B and numbered child subtasks, rather than implementing an entire rollup accidentally.
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

- Follow the owner's approved Turkish application-interface language. Write user-facing pages, navigation, form labels, help text, validation errors, notifications and empty/success/error states in Turkish; configure Django's built-in interface messages and HTML language accordingly. Preserve the project name **Finance Tracker** under DEC-001. This interface-language rule does not itself require translating source identifiers or project documentation.
- Follow the documented modular monolith and keep UI, services, persistence, and external adapters at their documented boundaries.
- Keep financial calculations deterministic and independently testable. Supply dates/clocks explicitly where needed.
- Use precise Python Decimal arithmetic for monetary calculations and exact integer minor units where documented. Binary floats must not enter authoritative calculations or financial persistence; chart conversions are presentation only.
- Preserve observation/revision and snapshot history, atomic writes, ownership integrity and recoverability. Review precision, rounding, revision and replay mechanisms at their recorded gates rather than silently approving them.
- Prevent double-counting of assets, opening values and movement annotations. Internal tracked-account movement creates no external contribution; a goal links whole accounts, adds no wealth and locks no funds. Missing movement/valuation evidence means unknown attribution, not invented performance.
- Keep core financial calculations and persistence independent of SMTP and later Gemini. Emails contain no financial details; Gemini needs exact one-call consent. Telegram is deferred, not a release prerequisite.
- Do not introduce unnecessary frameworks, services, infrastructure, or dependencies.

## Security Rules

- Never commit API keys, credentials, personal financial records, databases, exports, or backups. Respect existing ignore rules and use synthetic fixtures.
- Never send financial context to Gemini without explicit request-specific approval of the exact minimized payload and question. Changed payloads require new approval; approval permits one call. Do not log sensitive prompts or credentials.
- Keep the prototype and existing Streamlit shell on loopback with synthetic data. Release ingress requires the reviewed HTTPS Tunnel/private-origin topology and application authentication/authorization; never expose the database, CasaOS management UI or Docker socket through the application. No real users/sensitive data before the full release gate.
- Never perform financial transactions automatically, including payments, trades, or investment actions. Manually recording financial events is governed by the documented validation and persistence rules.
- Restrict reminder email to the intended verified User address and approved schedule; no financial content, report attachments or bearer report access. Membership/reset tokens are separate single-use authentication workflows. Telegram remains deferred; no inbound bot interface is authorized.
- Keep external integrations isolated from authoritative financial logic. Gemini output cannot execute SQL, invoke financial-write tools, alter computed figures/records or provide personalized security buy/sell recommendations.
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
