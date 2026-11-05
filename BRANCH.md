# Finance Tracker — Git Branch Workflow

Use lightweight GitHub Flow: a reviewed `main` and short-lived task branches. This is a solo project; the owner can implement and review their own work, but AI-generated changes always need human review. See [CONTRIBUTING.md](CONTRIBUTING.md) and [agent instructions](AGENTS.md).

## Main Branch

`main` represents the latest reviewed and accepted project state. Do not develop features directly on `main`. Every implementation task uses an appropriate task branch. Do not create permanent development or release branches without a demonstrated need and owner agreement.

The initial governance-only bootstrap is explicitly requested as uncommitted additions on the current branch. It does not authorize application implementation or branch operations and is not an exception for future feature work.

## Branch Naming

| Purpose | Pattern | Example |
|---|---|---|
| Feature | `feat/TASK-XXX-short-description` | `feat/TASK-004A-asset-registration` |
| Fix | `fix/TASK-XXX-short-description` | `fix/TASK-002-savings-rounding` |
| Documentation | `docs/short-description` | `docs/repository-governance` |
| Refactoring | `refactor/TASK-XXX-short-description` | `refactor/TASK-003-repository-boundaries` |
| Tests | `test/TASK-XXX-short-description` | `test/TASK-005A-opening-replay` |
| Maintenance | `chore/short-description` | `chore/local-tooling` |

`TASK-XXX` means an actual identifier from the [backlog](docs/planning/BACKLOG.md), including suffixes such as `TASK-004A` and `TASK-004B`. These examples describe possible branches, not completed work or authorization to start a task. Use executable leaves for scoped work; parent rollups complete only when their children do. Keep descriptions short, lowercase, and hyphen-separated. Do not invent task IDs. For work with no backlog entry, reference the owner request and use a suitable `docs/` or `chore/` branch.

## Branch Workflow

These steps describe future authorized work; they do not grant an agent permission to commit, push, merge, or change branches in a task that prohibits it.

1. **Inspect the working tree.** Check `git status`, the current branch, and existing changes. Preserve unrelated work. Do not discard, overwrite, or automatically stash it; if it prevents safe branching, report the issue before proceeding.
2. **Check remote freshness.** Inspect `git remote -v`; do not assume a remote named `origin` exists. Fetch from the selected configured remote only when network access is available and authorized. If offline or no usable remote exists, record that remote freshness is unverified and use the latest verified local state agreed for the task.
3. **Create the task branch.** Start from up-to-date local `main`. If updating it would require a merge, an agent needs explicit authorization; diverged history must be reported rather than reset or rebased automatically. Use the naming rules above.
4. **Implement the task.** Read its dependencies, requirements, acceptance criteria, and relevant decisions first. Keep scope focused and preserve unrelated changes.
5. **Run validation.** Execute relevant tests and document actual results, failures, and checks not run. Documentation-only work uses appropriate document checks.
6. **Review the diff.** Inspect all intended changes, including new files, and check acceptance criteria, accidental edits, credentials, and personal data. Stage only intended files if staging is authorized.
7. **Commit descriptively.** Use Conventional Commits. AI agents must obtain explicit authorization before committing; task implementation alone does not authorize it.
8. **Choose whether to use a PR.** Follow the policy below. A configured remote makes a PR possible, not mandatory. Agents never create PRs automatically; an explicit owner request is required. Any required push also needs explicit authorization.
9. **Obtain human review.** Review the diff and acceptance evidence through the PR or locally. Without a PR, local diff review and acceptance-criteria verification are mandatory. Record the reviewed scope/revision, results, limitations, and human acceptance in the PR or local task report. Changes after review need renewed review of the affected work.
10. **Merge only with explicit owner approval.** Prefer a squash merge when using a PR. An explicitly approved local merge is allowed. Agents require explicit authorization to perform either operation. Branch deletion is a separate action requiring explicit authorization.

## Pull Request Policy

PRs are **optional for routine changes**. They are **recommended** for significant features, financial calculation changes, database schema changes, security-sensitive changes, and external integrations. They provide a durable place to discuss and review a diff; they do not replace testing or human judgment.

Use the [PR template](.github/PULL_REQUEST_TEMPLATE.md) when a PR is chosen. If no PR is created, apply the same acceptance and review criteria locally. Every implementation task still requires an appropriate task branch, relevant testing, and human review before merging. Do not automatically create PRs.

## Commit Convention

Use `type: concise description` in the imperative:

```text
feat: add asset registration
fix: correct savings calculation
docs: update requirements traceability
test: add transaction validation tests
refactor: simplify portfolio service
chore: configure project tooling
```

Include the actual backlog task and requirement references in the commit body or accompanying review report where applicable. Avoid unrelated changes in one commit. These examples are conventions, not permission to commit or modify requirements.

## Merge Policy

Before either a PR merge or local merge, verify:

- Relevant task acceptance criteria and requirements are satisfied with evidence; scoped delivery does not complete broader requirements.
- Relevant tests pass, or omitted checks and limitations are documented and reviewed. An unresolved mandatory financial-correctness, privacy, integrity, or recovery failure cannot be waived by documenting it.
- Necessary documentation is updated within authorized scope; unresolved protected-document changes are reported for owner approval.
- The diff contains only intended files, with no secrets or personal financial data.
- A human has reviewed the current changes and the project owner explicitly approves merging them.

Prefer squash merges for focused branches merged through PRs. Local merges may use the owner-approved merge method. Do not treat PR approval, permission to commit, or permission to push as authorization for an agent to execute a merge.

## Local Rules and GitHub Enforcement

These files document local working rules; Git does not automatically enforce branch names, review, or human approval. A local merge remains possible and must follow the agreed process.

GitHub branch protection, when separately configured by the owner, can enforce remote rules such as PR or status-check requirements. It does not protect local worktrees. Remote rules may be stricter than this optional-PR policy; report a conflict rather than bypassing protection. This governance task does not configure protection, CI, or hooks, and does not claim that any remote enforcement is enabled.
