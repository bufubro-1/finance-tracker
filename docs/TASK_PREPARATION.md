# Finance Tracker — Task Preparation Protocol

**Document:** `docs/TASK_PREPARATION.md`  
**Purpose:** Standardize pre-implementation checks before starting a development task.

## 1. Objective

Before beginning any new implementation task, the AI agent must perform a structured readiness assessment.

This process ensures that the task is properly defined, dependencies are satisfied, relevant decisions are approved, and the Git environment is safe.

Task preparation does not authorize implementation or Git mutations.

## 2. Task Identification

1. Read `docs/planning/BACKLOG.md`.
2. Identify the requested task using its exact identifier.
3. If no task identifier is provided, identify the next eligible executable backlog task.
4. Prefer executable task leaves over parent tasks.
5. Never invent task IDs.
6. Do not automatically begin another task.

For the selected task, report:
- Task ID and title
- Estimated effort
- Related milestone
- Priority and status
- Dependencies

## 3. Requirements Analysis

Read the task's linked:

- Functional requirements
- Non-functional requirements
- Business rules
- User stories
- Use cases
- Architecture and data model
- Planned test cases

Extract the acceptance criteria and identify any inconsistencies.

Do not assume that planned test cases have been implemented or executed.

## 4. Dependency Verification

Verify that prerequisite tasks have been completed and accepted.

Check:
- Implementation evidence
- Relevant test results
- Human acceptance
- Git integration status
- Required documentation updates

A task must not be classified as ready solely because its predecessor contains a passing test suite.

If required dependencies are incomplete, report a blocker.

## 5. Decision Gate

Read `docs/DECISION_LOG.md`.

Identify decisions relevant to the selected task.

For every unresolved blocking decision, report:

- Decision ID
- Description
- Available options
- Recommended choice
- Rationale
- Implementation impact

Do not approve proposed decisions on behalf of the project owner.

## 6. Git Readiness

Inspect the repository without modifying it.

Verify:
- Current branch
- HEAD commit
- Local `main` state
- Configured remotes
- Working-tree changes
- Existing Git worktrees
- Task branch conflicts
- Uncommitted or unrelated changes

Do not perform fetch, checkout, stash, reset, worktree creation, branch deletion, commit, push, or merge during preparation.

If remote freshness cannot be verified, state that explicitly.

## 7. Implementation Planning

Prepare a brief, task-specific plan including:

- Expected files or modules
- Main implementation steps
- Required tests
- Documentation impact
- Risks and assumptions
- Estimated effort
- Proposed branch name
- Proposed worktree location

Prefer the repository's current architecture and existing modules.

Do not introduce new infrastructure unless required by approved requirements.

## 8. Readiness Classification

Classify the task using one of:

**Ready**

Requirements and dependencies are satisfied, necessary decisions are approved, and no blocking issue is identified.

**Ready with Conditions**

The task is sufficiently defined, but non-blocking verification or preparation items remain.

**Blocked**

A required dependency, policy decision, or critical acceptance condition is unresolved.

Describe the reason for the classification.

## 9. Preparation Report

The agent must produce a concise readiness report containing:

1. Task identifier, title, priority, milestone, and estimated effort
2. Linked requirements and acceptance criteria
3. Dependency and predecessor acceptance status
4. Relevant approved and unresolved decisions
5. Git branch, worktree, and baseline state
6. Proposed implementation approach
7. Planned tests and verification
8. Risks, assumptions, and blockers
9. Readiness classification and recommendation

## 10. Authorization Boundary

Task preparation is strictly read-only.

Completing preparation does not authorize:

- Application implementation
- Documentation modifications
- Dependency installation
- Branch or worktree creation
- Git staging or commits
- Pull Request creation
- Pushes or merges
- Deployment

After presenting the preparation report, stop for explicit owner authorization.

Never interpret a Ready classification as authorization to begin implementation.
