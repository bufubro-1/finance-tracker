# Finance Tracker — Development Workflow

**Version:** 1.0  
**Scope:** All implementation tasks  
**Development Model:** Solo Developer + AI Coding Agent  
**Branch Strategy:** Lightweight GitHub Flow

## 1. Purpose

This document defines the standard lifecycle for implementing development tasks in Finance Tracker.

Its purpose is to minimize repetitive instructions while maintaining requirement traceability, code quality, data integrity, and human oversight.

This workflow must be followed alongside `AGENTS.md`, `BRANCH.md`, and `CONTRIBUTING.md`.

If these documents conflict, the existing governance rules and approved project decisions take precedence.

## 2. Task Execution

Before implementation starts, complete the read-only preparation process in [TASK_PREPARATION.md](TASK_PREPARATION.md) and present its readiness report. Preparation and implementation are separate authorization phases: after preparation, stop for explicit owner authorization to begin implementation. A Ready classification does not authorize implementation or Git mutations.

When the project owner requests implementation of a backlog task, execute the following stages.

### Stage 1 — Task Discovery

1. Locate the requested task in `docs/planning/BACKLOG.md`.
2. Read linked requirements, business rules, architecture, and test cases.
3. Verify dependencies and approved decisions.
4. Identify blockers before modifying files.
5. Prepare a concise implementation plan.

Do not implement tasks with unresolved blocking decisions.

### Stage 2 — Git Preparation

1. Inspect the current repository state.
2. Identify the reviewed baseline.
3. Check existing branches and worktrees.
4. Preserve uncommitted changes.
5. Create an isolated task branch following `BRANCH.md`.
6. Use a separate Git worktree when the current working tree contains unrelated changes.

Do not stash, reset, discard, overwrite, or rewrite existing work.

Do not assume a remote exists or is up to date without verification.

### Stage 3 — Implementation

1. Implement only the selected task.
2. Follow the approved architecture and data model.
3. Keep financial calculations deterministic.
4. Preserve transaction history and financial data integrity.
5. Add or update appropriate tests.
6. Update directly affected documentation.

Do not introduce unrelated features or silently modify approved requirements.

### Stage 4 — Automated Verification

Perform relevant checks:

- Unit tests
- Integration tests when applicable
- Configuration validation
- Financial calculation test cases
- Static checks where available
- Git diff and whitespace checks
- Secret and sensitive-data checks
- Documentation and traceability consistency

Do not claim success for unexecuted checks.

Mandatory financial, privacy, and data-recovery acceptance criteria cannot be bypassed by documenting their failure.

### Stage 5 — Review Preparation

Produce a concise report containing:

- Task identifier
- Branch and worktree
- Changed files
- Implementation summary
- Tests executed and results
- Acceptance criteria coverage
- Known limitations
- Security considerations
- Remaining blockers

**Stop at the Human Review Gate.**

Do not commit, push, create a Pull Request, merge, or delete branches without explicit authorization.

### Stage 6 — Human Review

The project owner reviews the implementation.

Possible outcomes:

- **Accept:** All mandatory acceptance criteria are satisfied.
- **Accept with Conditions:** Only explicitly accepted non-blocking limitations remain.
- **Request Changes:** Corrections or additional verification are required.

If changes are requested, return to the relevant implementation or verification stage.

Do not treat silence or a passing test suite as human approval.

### Stage 7 — Commit

After explicit authorization:

1. Review the current diff.
2. Stage only the approved task files.
3. Inspect the staged diff.
4. Check for secrets and unrelated changes.
5. Create one or more authorized Conventional Commits.
6. Report commit hashes and remaining worktree changes.

Commit authorization does not imply merge or push authorization.

### Stage 8 — Merge

After separate explicit merge authorization:

1. Verify the approved task commit.
2. Confirm the merge target and reviewed baseline.
3. Preserve unrelated work and uncommitted files.
4. Perform appropriate integration checks.
5. Follow `BRANCH.md` merge rules.
6. Verify the result.
7. Report the merge outcome.

Never delete branches or worktrees without separate authorization.

### Stage 9 — Task Closure

Include task-closure documentation updates in the reviewed changes where possible. Otherwise, they require a separately authorized and reviewed documentation change. Do not automatically edit documentation after merging.

After successful integration and verified acceptance:

1. Verify that the development task status follows the repository's documentation rules.
2. Verify that test evidence and known limitations are recorded.
3. Verify that related traceability records are updated when applicable.
4. Identify the next eligible backlog task.

Do not automatically begin the next task.

## 3. Default Automation Boundaries

The AI agent may independently:

- Read documentation and source code
- Prepare implementation plans
- Modify authorized task files
- Write relevant tests
- Execute non-destructive tests
- Inspect diffs
- Produce review reports

Explicit authorization is required for:

- Commits
- Pushes
- Pull Request creation
- Merges
- Branch deletion
- Git history rewriting
- Destructive database operations
- Major architecture changes
- Deployment
- Approved requirement changes

A workflow instruction does not constitute standing authorization for restricted operations.

## 4. Completion Criteria

A task is considered complete only when:

- Its mandatory acceptance criteria are met.
- Relevant tests have been executed successfully.
- Changes have undergone human review.
- Known limitations are recorded.
- An authorized commit has been created.
- Integration has been completed when required by the task workflow.
- Documentation and task status accurately reflect the implementation.

## 5. Usage

To start a task:

`Implement TASK-XXX following AGENTS.md and docs/DEVELOPMENT_WORKFLOW.md.`

To request a review:

`Review the current task against its acceptance criteria.`

To request a commit:

`I approve the reviewed changes. Commit only the current task.`

To request a merge:

`I authorize merging the accepted task into main after integration checks.`

Each authorization is limited to the explicitly identified task and operation.
