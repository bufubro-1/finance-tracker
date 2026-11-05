# Finance Tracker — User Stories

Status: Revised scope approved; delivery is Planned except historical TASK-001 evidence. Must is relative to the assigned release. M-009 covers only synthetic startup/login/account/card portions; no whole broad story is accepted from that subset.

## US-001 — Configure my reporting settings

As a User, I want to use my own currency and timezone, so that my wealth stays comparable.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-001, FR-002, FR-032.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. Missing optional credentials do not block core startup; errors redact secrets; development and release settings are distinct.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-002 — Manage my savings and investment accounts

As a User, I want to organize my accounts, so that I can see where wealth is held.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-003.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. Names are unique within an owner; history survives archive; archival changes comparison coverage and cannot manufacture savings.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-003 — Define holdings and units

As a User, I want to maintain asset definitions, so that quantities have an explicit meaning.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-004.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. Referenced units cannot be silently changed; instruments with history retain their identity; foreign holdings use manual reporting-currency prices.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-008 — Maintain dated prices

As a User, I want to enter manual prices, so that I control portfolio valuation inputs.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-005.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. Future, nonfinite or invalid prices fail; historical valuations never use a price effective after the valuation date.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-009 — Understand current wealth

As a User, I want to see clear totals, composition and warnings, so that I understand both values and gaps.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-011, FR-012, FR-014, FR-050.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. Unpriced holdings make totals incomplete; carrying a value forward does not refresh it; missing values never become assumed zero.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-011 — Review historical snapshots

As a User, I want to view saved dated wealth, so that I can compare recorded history.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-015, FR-044.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. No current balance is backfilled into an earlier date; missing history remains missing; corrections may create a new snapshot revision, not overwrite an accepted snapshot.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-012 — Maintain savings goals

As a User, I want to set multiple targets and deadlines, so that I can track savings plans.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-016.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. Validate positive targets; allow overdue goals with a clear state; closing a goal releases its account links, not cash.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-014 — See indicative monthly saving

As a User, I want to see required monthly saving, so that I understand the remaining effort.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-019.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. Gap 1.00 over three opportunities rounds upward to 0.34 at scale 2; funded gives zero; overdue underfunded gives overdue, not division by zero; incomplete valuation qualifies the result.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-015 — Request savings and wealth explanations

As a User, I want to approve an optional explanation, so that I can understand computed summaries.

- **Priority / release:** Must / Later Gemini.
- **Requirements:** FR-020, FR-022, FR-024.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. Explain reported contributions and unknown attribution honestly; estimates are not actual spending; Gemini cannot alter computed values.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-016 — Explain goal feasibility

As a User, I want to approve a goal explanation, so that I can understand its assumptions.

- **Priority / release:** Must / Later Gemini.
- **Requirements:** FR-021, FR-024.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. Context preserves stale/missing-data warnings and includes profile estimates only when approved; goals and balances remain unchanged.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-017 — Ask explanatory questions

As a User, I want to approve a minimized question, so that I control what leaves the application.

- **Priority / release:** Must / Later Gemini.
- **Requirements:** FR-023, FR-024.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. Requests for specific security recommendations receive an explanation-only boundary; no SQL, payments, trades or writes can execute.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-020 — Export my records and recover the system

As a User / Operator, I want to export my own data or perform an operator restore, so that data stays portable and recoverable.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-029, FR-030, FR-031.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. Operator procedure verifies a backup independently; ordinary Users and application Admin cannot download a whole-system backup.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-021 — Link accounts to goals

As a User, I want to link each account to one goal, so that progress does not promise the same assets twice.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-018, FR-048.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. Each account supports at most one active goal; withdrawal or falling value can reduce progress; missing/stale values qualify progress.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-022 — Invite members

As a Admin, I want to invite or suspend members, so that membership stays controlled.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-033.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. Invitation tokens expire, are single-use and are stored as hashes; no public registration; revoked or used invitations fail.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-023 — Sign in and recover access

As a User, I want to use secure sign-in and recovery, so that my records remain private.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-034.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. Prototype uses a locally provisioned synthetic identity; release verifies email ownership, generic reset responses, revocation and secure cookies; suspended users lose access.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-024 — Administer without financial access

As a Admin, I want to manage users and sanitized health with MFA, so that operations do not expose private finances.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-035, FR-045, FR-051.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. No impersonation, arbitrary password setting or financial model admin; reset can only be sent to the existing verified address; protected email/role changes cannot enable takeover.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-025 — Keep my records isolated

As a User, I want to have every financial path enforce ownership, so that others cannot read or change my data.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-036.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. User A and Admin cannot access B through identifiers, forms, downloads or jobs; cross-owner relationships fail atomically; no client-supplied owner override.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-026 — Update balances and holdings simply

As a User, I want to enter current observations, so that I need not record every financial transaction.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-037, FR-049.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. An initial observation establishes starting wealth, not a contribution; validate exact nonnegative amounts; investment totals derive from cash and holdings, never an added duplicate account total.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-027 — Classify contributions and withdrawals

As a User, I want to annotate savings alongside updates, so that contributions are counted once.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-038.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. Save observations and annotations once atomically; contributions do not increase the entered balance again; internal tracked-account movements have zero net contribution; skipped classification is allowed.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-028 — See honest change attribution

As a User, I want to see unknown when the data is insufficient, so that I am not shown invented performance.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-039.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. Without comparable endpoints and explicit interval-completeness confirmation, show attribution unknown; 10000 to 11200 with complete net contributions 1000 gives residual 200, never an automatic return percentage or investment-profit claim.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-029 — Maintain an optional profile

As a User, I want to review estimated income and expenses, so that planning assumptions stay explicit.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-040, FR-050.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. Omitting the profile does not block tracking or reports; estimated surplus is labeled; profile values never create balances or movements.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-030 — Configure reports and reminders

As a User, I want to choose a monthly schedule, so that I can review information before generation.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-041, FR-042.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. Schedules require explicit enablement; schedule edits affect future occurrences and do not overwrite earlier reports; local month boundaries are used.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-031 — Read private monthly reports

As a User, I want to view saved authenticated reports, so that I can review prior periods even with stale data.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-043, FR-044, FR-050.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. Show missing/stale inputs and profile review dates; report reads require owner authentication; regeneration creates a new revision and no automatic Gemini call.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## US-032 — Operate a controlled release

As a Operator, I want to use verified CI and deployment procedures, so that the small self-hosted system remains maintainable.

- **Priority / release:** Must / MVP.
- **Requirements:** FR-046, FR-047.
- **Acceptance:** Given the specified owned/synthetic workspace, the linked requirements pass their stated success and rejection scenarios. CI uses no production data or deployment credentials, tests PostgreSQL behavior when introduced, and does not auto-deploy.
- **Dependencies:** Authentication/owned settings as applicable; task DAG in [Backlog](../planning/BACKLOG.md). No deferred ledger/reservation prerequisites.

## Historical stories

Retained identifiers; original acceptance at baseline `5052b5b`.

| ID | Original concept | Status / replacement |
|---|---|---|
| US-004 | Record purchases, sales and openings | Deferred; current value comes from US-021/026/027/028/030/031 as applicable. |
| US-005 | Record income and expenses | Deferred; current value comes from US-021/026/027/028/030/031 as applicable. |
| US-006 | Correct or delete ledger entries | Deferred; current value comes from US-021/026/027/028/030/031 as applicable. |
| US-007 | Transfer cash through ledger postings | Deferred; current value comes from US-021/026/027/028/030/031 as applicable. |
| US-010 | Review actual monthly income/expenses/savings | Deferred; current value comes from US-021/026/027/028/030/031 as applicable. |
| US-013 | Reserve and release goal cash | Deferred; current value comes from US-021/026/027/028/030/031 as applicable. |
| US-018 | Configure Telegram destination | Deferred; current value comes from US-021/026/027/028/030/031 as applicable. |
| US-019 | Receive Telegram summaries and goal reminders | Deferred; current value comes from US-021/026/027/028/030/031 as applicable. |
