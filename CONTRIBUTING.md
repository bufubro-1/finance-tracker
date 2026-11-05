# Contributing to Finance Tracker

Finance Tracker is a solo-developed, single-user, local-first Python project. Future contributors are welcome to follow the same small, reviewable workflow:

**Backlog Task → Branch → Implementation → Tests → Review → Merge**

Pull Requests (PRs) are optional for routine changes. Every implementation task still needs an appropriate task branch, relevant testing, and human review before merging. AI-generated changes always require human review; the solo maintainer may perform that review.

## Development Setup

Read the [documentation index](docs/README.md), [Charter](docs/CHARTER.md), and [Decision Log](docs/DECISION_LOG.md) first. Follow [AGENTS.md](AGENTS.md) for source precedence, security, and agent restrictions, and [BRANCH.md](BRANCH.md) for Git operations.

TASK-001 now provides the runtime/package skeleton, environment configuration,
minimal local Streamlit shell, and focused tests. Follow [local setup and
configuration](docs/SETUP.md) for Python 3.14.x, venv, pinned pip dependencies,
startup commands, variables, and trusted-device network guidance. The initial
tested interpreter is 3.14.8 under DEC-017.

After following the setup guide, run `python -m pytest -q` and
`python -m pip check`. The startup test opens a temporary loopback listener; the
test runner needs local socket permission. Use isolated synthetic fixtures and
private temporary paths, never personal databases or live destinations.

The owner's TASK-001 start instruction lifts DEC-018's execution hold for this
task only. Its boundary remains runtime/configuration/startup and relevant
setup tests/documentation. Financial calculations, database schemas, asset
management, Gemini features, and Telegram features remain later work. Both
adapters remain disabled. Other decision gates and remaining baseline approval
under OQ-001 are unchanged. Focused evidence does not complete broader
requirements, the first-dashboard milestone, or owner acceptance.

## Task Selection and Traceability

- Select a scoped executable task from the [backlog](docs/planning/BACKLOG.md); read dependencies, acceptance criteria, and the related [WBS](docs/planning/WBS.md) package. A/B children are executable tasks; their parents are completion rollups.
- Follow relevant [SRS requirements and business rules](docs/requirements/SRS.md), [architecture](docs/design/ARCHITECTURE.md), and [data model](docs/design/DATA_MODEL.md). Review recorded decision gates before fixing persistent financial semantics or other pending policies.
- Use the [RTM](docs/requirements/RTM.md) to connect task scope, requirements, and planned tests. Reference actual task, FR/NFR/BR, and applicable TC identifiers in the review report. Do not invent IDs or equate a mapping with implementation evidence.
- For authorized documentation or maintenance work without a backlog task, cite the owner's request and state that no task ID applies. Do not change the backlog merely to assign an ID.

## Implementation and Coding Principles

Prepare a brief plan after inspecting affected code and tests. Work on an appropriate branch under the naming rules in [BRANCH.md](BRANCH.md). Preserve unrelated changes and implement only the requested task.

Follow the documented modular monolith: keep authoritative financial calculations independent of Streamlit and external API clients. Use deterministic Decimal/integer arithmetic, explicit dates, atomic persistence, and preserved history. Prevent double-counting and over-allocation. Keep adapters optional and replaceable, and avoid unnecessary frameworks or infrastructure. Proposed technical details remain subject to their recorded reviews.

If requirements or design documents conflict, report the conflict before implementing the affected behavior. Do not silently expand scope or revise approved requirements or architecture.

## Testing Expectations

Use the [test plan](docs/testing/TEST_PLAN.md) and task acceptance criteria to choose relevant verification. Add or update meaningful tests alongside behavior changes; do not postpone essential financial or persistence tests to the final testing phase.

Use fixed dates, exact expected values, synthetic data, temporary databases, and fake integrations. Exercise affected calculation boundaries, validation, rollback, replay, history, reservation, or privacy behavior as applicable. Documentation-only work needs link, path, convention, and consistency checks rather than application tests.

Record commands/checks actually executed, outcomes, relevant environment/fixture information, and failures or omissions with reasons. Distinguish automated tests, manual checks, documentation validation, and owner acceptance. Never claim tests passed when they were not run, or claim full acceptance from a limited milestone subset.

## Documentation Updates

Update usage, configuration, and other affected documentation when authorized and necessary for the change. Requirement changes need corresponding traceability and test updates under the existing change-control process. Obtain explicit authorization before modifying approved requirements, Charter constraints, or architecture decisions; report needed updates if outside the current scope.

Keep proposed, approved, implemented, and verified status distinct. Do not mark backlog tasks, requirements, or planned test cases complete without appropriate implementation and verification evidence. This governance bootstrap does not change existing planning files or their statuses.

Under DEC-019, the proposed documentation baseline contains 13 new documentation files and four governance files. Preserve the existing README.md and docs/CHARTER.md modifications and exclude them until separate review; do not automatically stash, revert, or include them. Baseline preparation does not authorize staging, committing, pushing, merging, or changing branches.

## Commits and Review

Use Conventional Commits with the types and examples in [BRANCH.md](BRANCH.md). Keep changes focused; inspect the full diff and new files before including them in a commit. AI agents must never commit, push, or merge without explicit owner authorization for the action.

PRs are optional for routine changes and recommended for significant features, financial calculation changes, database schema changes, security-sensitive changes, and external integrations. If a PR is chosen, use the [PR template](.github/PULL_REQUEST_TEMPLATE.md), explain behavior and evidence, and link relevant task/requirement references. Agents must not automatically create PRs; creation requires an explicit owner request. Do not assume a configured remote or permission to push.

When no PR is created, **local diff review and acceptance-criteria verification are mandatory**. Record the reviewed scope/revision, test outcomes, limitations, and human acceptance in the local task report. The maintainer must review AI-generated work personally. If changes follow review, review the affected work again.

Prefer squash merges when using PRs. An explicitly approved local merge is allowed. Both paths require human review and explicit project-owner approval before merging; an agent also needs explicit authorization to execute the merge. Follow any configured remote protection without bypassing it.

## Definition of Done

A task is done only when:

- Requested acceptance criteria and relevant requirements have implementation and verification evidence; dependencies and applicable decision gates are satisfied.
- Relevant tests/checks have actual recorded results. Omitted checks and limitations are disclosed; unresolved mandatory financial-correctness, privacy, integrity, or recovery failures prevent completion.
- Necessary documentation and traceability updates are completed within authorized scope; unresolved required updates are reported rather than silently ignored.
- The reviewed diff contains only intended changes and no secrets or personal financial data.
- A human has reviewed the changes, verified acceptance criteria, and accepted the task. Merge authorization is explicit and separate from task implementation.

Being ready for review is not owner acceptance. A task may be accepted while its authorized changes await a later merge; never claim a merge occurred unless it did. Rollups and milestones require their full documented criteria, not just one completed slice.

## Responsibilities

**AI agents** inspect sources, plan briefly, implement scoped work, maintain relevant tests, run validation, surface conflicts, and provide truthful evidence and limitations. They preserve existing work and follow [AGENTS.md](AGENTS.md), including explicit authorization for commits, pushes, merges, and other restricted actions. They never automatically create PRs or approve their own changes on behalf of the owner.

**The human maintainer** selects priorities, resolves scope and policy decisions, supplies private configuration, reviews AI-generated changes, verifies acceptance evidence, accepts tasks, and explicitly approves merges. In solo development, implementation and review can be performed by the same human with a deliberate final diff review; no additional reviewer or mandatory PR is introduced.
