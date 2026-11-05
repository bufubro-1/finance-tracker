# Finance Tracker — Test Plan

Status: Cases remain Planned — Not Executed except the explicitly recorded historical/scoped evidence and deferred/superseded cases. M-009 is Completed — Accepted; see [closure evidence](M-009_CLOSURE.md). No application tests were rerun for this closure documentation. A mapping alone establishes neither execution nor acceptance.

## Strategy, environments and fixtures

Use exact unit fixtures for domain rules, synthetic multi-user PostgreSQL integration tests for ownership/transactions/concurrency, fake SMTP/Gemini boundaries, system deployment/recovery checks and owner usability demonstrations. Tests accompany each leaf; final system testing does not replace focused work.

Prototype M-009 uses current supported Linux/Python development environment, standard Django login and disposable SQLite with synthetic balances (e.g. account Example Savings, USD scale 2, 1000.00). The example currency is not an owner default. No production identity, financial data, cloud service or public exposure. Reuse its models/templates/services; SQLite success never establishes PostgreSQL behavior.

Full fixtures use two ordinary Users and a separate Admin, multiple owned accounts/assets, cash 1000 plus 10 units at 20, missing/stale observations, invalid/replayed updates and goals. Attribution fixture: start 10000, end 11200, confirmed net contribution 1000 -> supported residual 200; omit confirmation/flows or change coverage -> unknown. Dates/clocks and timezone boundaries are explicit. PostgreSQL tests use isolated disposable databases, never a personal dataset. No automatic destructive cleanup against shared data.

Intended system environment: Raspberry Pi 5 (8 GB), CasaOS, Docker Compose and Cloudflare Tunnel/HTTPS. TASK-024 verifies versions/ARM64/storage assumptions before TASK-020 separately authorized rehearsal. Proposed performance fixture is 10 users/3 active sessions, 10000 observations, 200 holdings and 20 goals per user; thresholds await OQ-003. Do not extrapolate x86 evidence to the Pi.

Use fake external services by default. Live checks need explicit consent, synthetic payloads and owner credentials/destinations; a later Gemini call additionally needs exact request-specific approval. Email tests inspect the complete subject/body/links and verify no financial content or bearer report access.

## Entry and exit gates

- **M-009 entry:** TASK-001 accepted; only task-local prototype decisions needed. No full foundation/infrastructure gate. Exit requires P1-01–P1-06, TC-053 and the prototype portion of TC-039, actual results and owner demonstration. Standard development login is not release MFA/session acceptance.
- **M-001/M-001A:** Full foundation, then W1-01–W1-04 including synthetic PostgreSQL recovery. Still no real users or sensitive data.
- **M-004/M-008:** Qualified wealth, movement attribution, goals/profile/export, then saved reports/reminders with missing data and failures. All work remains synthetic.
- **M-007:** Every MVP Must requirement passes applicable financial, authorization, MFA, privacy, PostgreSQL integrity/concurrency, backup/recovery and deployment checks; owner accepts; no unresolved mandatory defect. Real users/sensitive data wait for this gate and applicable authorization.
- **Later Gemini:** Explicitly separate cases and acceptance outside MVP. Deferred ledger/Telegram cases do not gate initial release.

Record revision/build, environment, fixture, command, actual result, evidence and limitations for each executed scenario. Broad cases can be partly exercised; never mark the whole case passed from a subset.

## Historical TASK-001 evidence

Integration commit `5052b5b` records owner-accepted `475492a`, 58 pytest passes in 0.80 s and successful pip check on Linux x86_64/Python 3.14.8. Initial sandbox attempt passed 57 but could not open the loopback socket; permitted rerun passed 58. This is historical evidence, **not execution during this revision**.

The runtime tests cover original setup subsets of TC-001/002/037/038/041/044. Requirements/cases now amended for Django/PostgreSQL/release remain planned; that evidence cannot establish their new behavior. No fresh-host install, physical LAN-device checks or new manual browser acceptance was run for the integration.

## Case catalog

### TC-001 — Deployment configuration

- **Level / release:** Integration / MVP.
- **Requirements:** FR-001.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** Missing optional credentials do not block core startup; errors redact secrets; development and release settings are distinct.
- **Status:** Planned — Not Executed.

### TC-002 — Per-user reporting currency

- **Level / release:** Integration / MVP.
- **Requirements:** FR-002.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** Two users may choose different currencies; changing a used currency is rejected. Prototype fixtures explicitly choose a synthetic example currency.
- **Status:** Planned — Not Executed.

### TC-003 — Account management

- **Level / release:** Integration / MVP.
- **Requirements:** FR-003.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** Names are unique within an owner; history survives archive; archival changes comparison coverage and cannot manufacture savings.
- **Status:** Planned — Not Executed.

### TC-004 — Asset definitions

- **Level / release:** Integration / MVP.
- **Requirements:** FR-004.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** Referenced units cannot be silently changed; instruments with history retain their identity; foreign holdings use manual reporting-currency prices.
- **Status:** Planned — Not Executed.

### TC-005 — Dated manual prices

- **Level / release:** Integration / MVP.
- **Requirements:** FR-005.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** Future, nonfinite or invalid prices fail; historical valuations never use a price effective after the valuation date.
- **Status:** Planned — Not Executed.

### TC-006 — Holding transactions

- **Level / release:** Integration / Historical/deferred.
- **Requirements:** FR-006.
- **Setup and steps:** Retained original test concept; see baseline 5052b5b for original steps.
- **Expected result:** Deferred capability is not an MVP acceptance prerequisite.
- **Status:** Deferred — Not Executed.

### TC-007 — Income recording

- **Level / release:** Integration / Historical/deferred.
- **Requirements:** FR-007.
- **Setup and steps:** Retained original test concept; see baseline 5052b5b for original steps.
- **Expected result:** Deferred capability is not an MVP acceptance prerequisite.
- **Status:** Deferred — Not Executed.

### TC-008 — Expense recording

- **Level / release:** Integration / Historical/deferred.
- **Requirements:** FR-008.
- **Setup and steps:** Retained original test concept; see baseline 5052b5b for original steps.
- **Expected result:** Deferred capability is not an MVP acceptance prerequisite.
- **Status:** Deferred — Not Executed.

### TC-009 — Record correction and deletion

- **Level / release:** Integration / Historical/deferred.
- **Requirements:** FR-009.
- **Setup and steps:** Retained original test concept; see baseline 5052b5b for original steps.
- **Expected result:** Deferred capability is not an MVP acceptance prerequisite.
- **Status:** Deferred — Not Executed.

### TC-010 — Account transfers

- **Level / release:** Integration / Historical/deferred.
- **Requirements:** FR-010.
- **Setup and steps:** Retained original test concept; see baseline 5052b5b for original steps.
- **Expected result:** Deferred capability is not an MVP acceptance prerequisite.
- **Status:** Deferred — Not Executed.

### TC-011 — Valuation completeness

- **Level / release:** Integration / MVP.
- **Requirements:** FR-011.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** Unpriced holdings make totals incomplete; carrying a value forward does not refresh it; missing values never become assumed zero.
- **Status:** Planned — Not Executed.

### TC-012 — Tracked wealth totals

- **Level / release:** Integration / MVP.
- **Requirements:** FR-012.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** Cash 1000 plus 10 units priced at 20 equals 1200; goal links add nothing; liabilities are explicitly excluded; incomplete totals are qualified.
- **Status:** Planned — Not Executed.

### TC-013 — Monthly cash-flow reporting

- **Level / release:** Integration / Historical/deferred.
- **Requirements:** FR-013.
- **Setup and steps:** Retained original test concept; see baseline 5052b5b for original steps.
- **Expected result:** Deferred capability is not an MVP acceptance prerequisite.
- **Status:** Deferred — Not Executed.

### TC-014 — Portfolio distribution

- **Level / release:** Integration / MVP.
- **Requirements:** FR-014.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** Distribution sums to that subtotal; unknown values appear separately; empty or zero-value portfolios show guidance rather than invented percentages.
- **Status:** Planned — Not Executed.

### TC-015 — Historical wealth

- **Level / release:** Integration / MVP.
- **Requirements:** FR-015.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** No current balance is backfilled into an earlier date; missing history remains missing; corrections may create a new snapshot revision, not overwrite an accepted snapshot.
- **Status:** Planned — Not Executed.

### TC-016 — Savings goals

- **Level / release:** Integration / MVP.
- **Requirements:** FR-016.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** Validate positive targets; allow overdue goals with a clear state; closing a goal releases its account links, not cash.
- **Status:** Planned — Not Executed.

### TC-017 — Savings reservations

- **Level / release:** Integration / Historical/deferred.
- **Requirements:** FR-017.
- **Setup and steps:** Retained original test concept; see baseline 5052b5b for original steps.
- **Expected result:** Deferred capability is not an MVP acceptance prerequisite.
- **Status:** Deferred — Not Executed.

### TC-018 — Goal progress

- **Level / release:** Integration / MVP.
- **Requirements:** FR-018.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** Each account supports at most one active goal; withdrawal or falling value can reduce progress; missing/stale values qualify progress.
- **Status:** Planned — Not Executed.

### TC-019 — Indicative monthly savings

- **Level / release:** Integration / MVP.
- **Requirements:** FR-019.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** Gap 1.00 over three opportunities rounds upward to 0.34 at scale 2; funded gives zero; overdue underfunded gives overdue, not division by zero; incomplete valuation qualifies the result.
- **Status:** Planned — Not Executed.

### TC-020 — Savings explanations

- **Level / release:** Integration / Later Gemini.
- **Requirements:** FR-020.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** Explain reported contributions and unknown attribution honestly; estimates are not actual spending; Gemini cannot alter computed values.
- **Status:** Planned — Not Executed.

### TC-021 — Goal feasibility explanations

- **Level / release:** Integration / Later Gemini.
- **Requirements:** FR-021.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** Context preserves stale/missing-data warnings and includes profile estimates only when approved; goals and balances remain unchanged.
- **Status:** Planned — Not Executed.

### TC-022 — AI summaries

- **Level / release:** Integration / Later Gemini.
- **Requirements:** FR-022.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** Output is labeled unverified explanation and cannot become an authoritative saved financial figure.
- **Status:** Planned — Not Executed.

### TC-023 — Financial explanation questions

- **Level / release:** Integration / Later Gemini.
- **Requirements:** FR-023.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** Requests for specific security recommendations receive an explanation-only boundary; no SQL, payments, trades or writes can execute.
- **Status:** Planned — Not Executed.

### TC-024 — Per-request Gemini consent

- **Level / release:** Integration / Later Gemini.
- **Requirements:** FR-024.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** Cancel makes zero calls; changed context/question invalidates consent; replay cannot consume approval twice; labels, notes and credentials are excluded from generated context.
- **Status:** Planned — Not Executed.

### TC-025 — Authorized Telegram destination

- **Level / release:** Integration / Historical/deferred.
- **Requirements:** FR-025.
- **Setup and steps:** Retained original test concept; see baseline 5052b5b for original steps.
- **Expected result:** Deferred capability is not an MVP acceptance prerequisite.
- **Status:** Deferred — Not Executed.

### TC-026 — Scheduled Telegram summaries

- **Level / release:** Integration / Historical/deferred.
- **Requirements:** FR-026.
- **Setup and steps:** Retained original test concept; see baseline 5052b5b for original steps.
- **Expected result:** Deferred capability is not an MVP acceptance prerequisite.
- **Status:** Deferred — Not Executed.

### TC-027 — Goal reminders and updates

- **Level / release:** Integration / Historical/deferred.
- **Requirements:** FR-027.
- **Setup and steps:** Retained original test concept; see baseline 5052b5b for original steps.
- **Expected result:** Deferred capability is not an MVP acceptance prerequisite.
- **Status:** Deferred — Not Executed.

### TC-028 — Notification preferences

- **Level / release:** Integration / Historical/deferred.
- **Requirements:** FR-028.
- **Setup and steps:** Retained original test concept; see baseline 5052b5b for original steps.
- **Expected result:** Deferred capability is not an MVP acceptance prerequisite.
- **Status:** Deferred — Not Executed.

### TC-029 — Operator backup

- **Level / release:** Integration / MVP.
- **Requirements:** FR-029.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** Operator procedure verifies a backup independently; ordinary Users and application Admin cannot download a whole-system backup.
- **Status:** Planned — Not Executed.

### TC-030 — Validated operator restore

- **Level / release:** Integration / MVP.
- **Requirements:** FR-030.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** Invalid candidates leave live data intact; stop writers, verify restored ownership/figures, invalidate sessions and pause outbound jobs before reviewed resumption.
- **Status:** Planned — Not Executed.

### TC-031 — Private CSV export

- **Level / release:** Integration / MVP.
- **Requirements:** FR-031.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** No other user, credentials or tokens appear; neutralize spreadsheet formulas; CSV is not a disaster-recovery backup.
- **Status:** Planned — Not Executed.

### TC-032 — Durable integration-independent core

- **Level / release:** Integration / MVP.
- **Requirements:** FR-032.
- **Setup and steps:** Use isolated synthetic users, fixed dates and exact fixtures; exercise success, rejection and ownership paths.
- **Expected result:** Committed observations survive restart; failed updates roll back; remote access depends on WAN/tunnel, but domain calculations require no external API.
- **Status:** Planned — Not Executed.

### TC-033 — Competing reservations and cash debits

- **Level / release:** Integration / Historical/deferred.
- **Requirements:** Historical superseded profile; baseline 5052b5b.
- **Setup and steps:** Retained historical case; original specification is in baseline 5052b5b.
- **Expected result:** Superseded/deferred; revised paths are tested under TC-053 and TC-058 through TC-073.
- **Status:** Superseded / Deferred — Not Executed.

### TC-034 — Corrupt/incompatible PostgreSQL restore

- **Level / release:** Integration / MVP.
- **Requirements:** FR-030, NFR-011.
- **Setup and steps:** Restore corrupt and unsupported candidates into an isolated rehearsal environment.
- **Expected result:** Live records and ownership remain intact; candidate is rejected before replacement.
- **Status:** Planned — Not Executed.

### TC-035 — Decimal valuation and rounding

- **Level / release:** Unit / MVP.
- **Requirements:** FR-012, NFR-012.
- **Setup and steps:** Test 0.10+0.20, minor-unit scaling and boundary per-holding products.
- **Expected result:** Exact results match approved OQ-002 policy; no binary floats or silent input rounding.
- **Status:** Planned — Not Executed.

### TC-036 — Canceled, stale and replayed Gemini consent

- **Level / release:** Integration / Later Gemini.
- **Requirements:** FR-024, NFR-003.
- **Setup and steps:** Cancel; change context; approve once and replay using a fake adapter.
- **Expected result:** Zero canceled/stale calls; at most one call per exact approval; no financial writes.
- **Status:** Planned — Not Executed.

### TC-037 — Trusted-device unauthenticated LAN boundary

- **Level / release:** Integration / Historical/deferred.
- **Requirements:** Historical superseded profile; baseline 5052b5b.
- **Setup and steps:** Retained historical case; original specification is in baseline 5052b5b.
- **Expected result:** Superseded/deferred; revised paths are tested under TC-053 and TC-058 through TC-073.
- **Status:** Superseded / Deferred — Not Executed.

### TC-038 — Secret and financial-data exclusion

- **Level / release:** System / MVP.
- **Requirements:** FR-001, FR-031, NFR-002.
- **Setup and steps:** Use synthetic sentinel secrets, notes, prompts, exports and backups; inspect tracked paths, ignore rules and logs.
- **Expected result:** No seeded credentials/financial payloads leak into Git or logs; private data paths stay restricted.
- **Status:** Planned — Not Executed.

### TC-039 — Dashboard and form usability

- **Level / release:** Acceptance / MVP.
- **Requirements:** FR-003, FR-037, NFR-004.
- **Setup and steps:** Owner follows visible navigation and labels to sign in, create a synthetic account and find its balance on a desktop and narrow viewport.
- **Expected result:** Clean readable cards, visible currency/value, clear active navigation, labeled intuitive form, preserved input and understandable errors/empty/success states; no horizontal clipping of essential controls.
- **Status:** Prototype usability subset passed and owner-accepted at `6c937a6`; broader release scenarios remain Planned — Not Executed. See [closure evidence](M-009_CLOSURE.md).

### TC-040 — Atomic update and restart

- **Level / release:** Integration / MVP.
- **Requirements:** FR-037, FR-038, FR-049, NFR-005, FR-032.
- **Setup and steps:** Inject failure between observations/movements/guard writes; separately commit and restart.
- **Expected result:** No partial update; committed exact observations and annotations survive.
- **Status:** Planned — Not Executed.

### TC-041 — Independent financial domain

- **Level / release:** Unit / MVP.
- **Requirements:** FR-012, FR-019, FR-039, NFR-006.
- **Setup and steps:** Run pure calculations with injected dates and no UI/ORM/provider initialization.
- **Expected result:** Deterministic results without Django models, Streamlit, credentials or network.
- **Status:** Planned — Not Executed.

### TC-042 — Pi workload performance

- **Level / release:** System / MVP.
- **Requirements:** NFR-007.
- **Setup and steps:** On intended host exercise 10 synthetic users and 3 active sessions with the proposed per-user fixture.
- **Expected result:** Record real host/versions/read/write timings; compare with approved OQ-003 thresholds without claiming unmeasured support.
- **Status:** Planned — Not Executed.

### TC-043 — Schema, numeric and ownership integrity

- **Level / release:** Integration / MVP.
- **Requirements:** FR-036, FR-037, FR-048, NFR-008, FR-004.
- **Setup and steps:** Against PostgreSQL try orphan/cross-owner references, negative/nonfinite/overflow values and competing goal links.
- **Expected result:** Atomic rejection, exact persistence and unique active account-goal links; SQLite prototype checks do not satisfy PostgreSQL acceptance.
- **Status:** Planned — Not Executed.

### TC-044 — Supported deployment rehearsal

- **Level / release:** System / MVP.
- **Requirements:** FR-047, NFR-009.
- **Setup and steps:** After separate authorization follow intended Pi/CasaOS/Compose procedure with synthetic fixtures; restart app/database/jobs.
- **Expected result:** Private persistent volumes, version compatibility, startup, restart and documented limitations have actual evidence; development server is not deployed.
- **Status:** Planned — Not Executed.

### TC-045 — External failure matrix

- **Level / release:** Integration / MVP.
- **Requirements:** FR-042, FR-043, FR-024, NFR-010.
- **Setup and steps:** Fake SMTP and later Gemini timeout, auth, quota, transient and ambiguous outcomes.
- **Expected result:** Core and report generation continue; bounded/redacted failures; no blind ambiguous resend or background AI.
- **Status:** Planned — Not Executed.

### TC-046 — Backup consistency and recovery

- **Level / release:** System / MVP.
- **Requirements:** FR-029, FR-030, NFR-011.
- **Setup and steps:** Back up during synthetic writes; restore after stopping writers with safety backup and rollback path.
- **Expected result:** Coherent values/owners/snapshots restore; revoke sessions and pause jobs; measure approved recovery target and disclose recovery point.
- **Status:** Planned — Not Executed.

### TC-047 — Numeric/date boundaries

- **Level / release:** Unit / MVP.
- **Requirements:** FR-002, FR-005, FR-019, NFR-012.
- **Setup and steps:** Exercise currency scales, excess precision, overflow, NaN/infinity, future observations, deadline today and overdue.
- **Expected result:** Reject invalid inputs; approved rounding/opportunity rules apply; no manufactured values.
- **Status:** Planned — Not Executed.

### TC-048 — Unauthorized Telegram and inbound commands

- **Level / release:** Integration / Historical/deferred.
- **Requirements:** Historical superseded profile; baseline 5052b5b.
- **Setup and steps:** Retained historical case; original specification is in baseline 5052b5b.
- **Expected result:** Superseded/deferred; revised paths are tested under TC-053 and TC-058 through TC-073.
- **Status:** Superseded / Deferred — Not Executed.

### TC-049 — Untrusted Gemini output and advice boundary

- **Level / release:** Integration / Later Gemini.
- **Requirements:** FR-020, FR-021, FR-022, FR-023, FR-024, NFR-003.
- **Setup and steps:** Fake invented numbers, SQL/tool instructions and requests for specific security buy/sell advice.
- **Expected result:** No authoritative number/write changes; explanation boundary and labels retained; no claim that model text is guaranteed correct.
- **Status:** Planned — Not Executed.

### TC-050 — Historical ledger restatement and Telegram downtime

- **Level / release:** Integration / Historical/deferred.
- **Requirements:** Historical superseded profile; baseline 5052b5b.
- **Setup and steps:** Retained historical case; original specification is in baseline 5052b5b.
- **Expected result:** Superseded/deferred; revised paths are tested under TC-053 and TC-058 through TC-073.
- **Status:** Superseded / Deferred — Not Executed.

### TC-051 — Atomic ledger opening replay

- **Level / release:** Integration / Historical/deferred.
- **Requirements:** Historical superseded profile; baseline 5052b5b.
- **Setup and steps:** Retained historical case; original specification is in baseline 5052b5b.
- **Expected result:** Superseded/deferred; revised paths are tested under TC-053 and TC-058 through TC-073.
- **Status:** Superseded / Deferred — Not Executed.

### TC-052 — Original SQLite/Streamlit first-dashboard acceptance

- **Level / release:** Integration / Historical/deferred.
- **Requirements:** Historical superseded profile; baseline 5052b5b.
- **Setup and steps:** Retained historical case; original specification is in baseline 5052b5b.
- **Expected result:** Superseded/deferred; revised paths are tested under TC-053 and TC-058 through TC-073.
- **Status:** Superseded / Deferred — Not Executed.

### TC-053 — Early Working Prototype end to end

- **Level / release:** System + acceptance / MVP.
- **Requirements:** FR-001, FR-003, FR-034, FR-037, NFR-004, NFR-001.
- **Setup and steps:** Start on loopback without PostgreSQL/cloud credentials; sign in with synthetic identity, navigate, create a savings account, view cards/total, validate an error, log out and restart.
- **Expected result:** All P1-01 through P1-06 checks have evidence and owner demo. Synthetic records persist; anonymous access fails; no external calls; clean usable layout.
- **Status:** Passed — Owner Accepted for P1-01–P1-06 at `6c937a6`; synthetic local prototype only. See [closure evidence](M-009_CLOSURE.md).

### TC-054 — Invitation lifecycle

- **Level / release:** Integration / MVP.
- **Requirements:** FR-033, NFR-013.
- **Setup and steps:** Use valid, expired, revoked and replayed invitations; attempt open enrollment.
- **Expected result:** Only intended email can enroll once through a valid token; hashes/logs do not expose tokens; no public signup.
- **Status:** Planned — Not Executed.

### TC-055 — Authentication, recovery and session revocation

- **Level / release:** Integration / MVP.
- **Requirements:** FR-034, NFR-013.
- **Setup and steps:** Test login/logout, suspension, reset, throttling, secure-cookie/CSRF settings and attempted admin-induced takeover.
- **Expected result:** Release controls pass; generic reset goes to existing verified address; revoked identity/session cannot access private data.
- **Status:** Planned — Not Executed.

### TC-056 — Admin MFA and recovery

- **Level / release:** Integration / MVP.
- **Requirements:** FR-051, NFR-013.
- **Setup and steps:** Try Admin operations before enrollment/challenge, after enrollment and after factor recovery.
- **Expected result:** MFA is required; recovery is controlled and invalidates sessions; it grants no financial access.
- **Status:** Planned — Not Executed.

### TC-057 — Admin/User access matrix

- **Level / release:** Integration / MVP.
- **Requirements:** FR-035, FR-036, NFR-013.
- **Setup and steps:** Try direct URLs, forged owner/role fields, financial admin registration, password/email replacement and impersonation.
- **Expected result:** Admin and other Users cannot access financial contents or assume another identity; normal permitted administration works.
- **Status:** Planned — Not Executed.

### TC-058 — All financial ownership paths

- **Level / release:** Integration / MVP.
- **Requirements:** FR-036, NFR-008, FR-031, NFR-013.
- **Setup and steps:** Exercise user A/B read/write, report, export, goal link, cache and scheduler paths using guessed IDs and cross-owner references.
- **Expected result:** No cross-user values, existence details or writes; server owner context and database relationships agree.
- **Status:** Planned — Not Executed.

### TC-059 — Manual observations and revisions

- **Level / release:** Integration / MVP.
- **Requirements:** FR-037, FR-049.
- **Setup and steps:** Save opening cash/holdings, revise a balance with reason, remove a holding through zero observation and reopen history.
- **Expected result:** No transaction ledger is required; opening adds no contribution, original is retained, account total is not added twice.
- **Status:** Planned — Not Executed.

### TC-060 — Savings classification and internal movements

- **Level / release:** Integration / MVP.
- **Requirements:** FR-038.
- **Setup and steps:** Save balance 11200 with reported contribution 1000 after baseline 10000; also withdraw, transfer between tracked accounts and leave classification absent.
- **Expected result:** Balance is 11200, not 12200; external net flows are signed once; internal net is zero; absent classification remains incomplete.
- **Status:** Planned — Not Executed.

### TC-061 — Known and unknown attribution

- **Level / release:** Integration / MVP.
- **Requirements:** FR-039.
- **Setup and steps:** Compare valid endpoints with complete movements, then omit flows, change scope, stale a price, revise a source and provide an unknown-value in-kind contribution.
- **Expected result:** Only complete comparable data yields supported residual 200 in the 10000/11200/1000 example; other cases show unknown, never automatic profit/return.
- **Status:** Planned — Not Executed.

### TC-062 — Optional profile estimates

- **Level / release:** Integration / MVP.
- **Requirements:** FR-040, FR-050.
- **Setup and steps:** Omit profile; add estimates; view; confirm unchanged; edit.
- **Expected result:** Core/reports work without profile; views do not refresh review date; estimates never create balances or actual savings.
- **Status:** Planned — Not Executed.

### TC-063 — Scheduler dates, downtime and replay

- **Level / release:** Integration / MVP.
- **Requirements:** FR-041, FR-043.
- **Setup and steps:** Inject month/year/DST boundaries, missed periods, parallel ticks, schedule edits and retry after report commit.
- **Expected result:** Approved OQ-005 occurrence policy holds; unique report per scheduled occurrence; no dependence on reminder success.
- **Status:** Planned — Not Executed.

### TC-064 — Email content and failure privacy

- **Level / release:** Integration / MVP.
- **Requirements:** FR-042, NFR-003, NFR-010.
- **Setup and steps:** Inspect fake envelope, subject, body, links and logs; fail or ambiguously acknowledge SMTP.
- **Expected result:** Verified destination and generic text only; no financial data or report bearer tokens; reporting continues independently.
- **Status:** Planned — Not Executed.

### TC-065 — HTTPS/private origin boundary

- **Level / release:** System / MVP.
- **Requirements:** FR-047, NFR-001.
- **Setup and steps:** After authorization inspect Compose ports, database reachability, Tunnel ingress, host/proxy settings, session/CSRF behavior and authenticated report URLs.
- **Expected result:** Only intended HTTPS application ingress; database/origin not directly public; tunnel never replaces application authorization.
- **Status:** Planned — Not Executed.

### TC-066 — Saved monthly report with missing information

- **Level / release:** Integration / MVP.
- **Requirements:** FR-043.
- **Setup and steps:** Generate prior-local-month report with no fresh update, absent profile and failed email; reopen after correcting inputs.
- **Expected result:** Report still exists with warnings; prior values remain; optional regeneration creates a distinct revision behind owner authentication.
- **Status:** Planned — Not Executed.

### TC-067 — Update replay and concurrent edits

- **Level / release:** Integration / MVP.
- **Requirements:** FR-038, FR-049, NFR-005, NFR-008.
- **Setup and steps:** Replay identical and changed payload keys, race updates from two connections and restart between retries.
- **Expected result:** Same intent commits once; changed key reuse or stale version rejects atomically; deliberate equal-valued new updates are not deduplicated.
- **Status:** Planned — Not Executed.

### TC-068 — Wealth dashboard and recovery acceptance

- **Level / release:** System + acceptance / MVP.
- **Requirements:** FR-011, FR-012, FR-029, FR-030, FR-037.
- **Setup and steps:** Exercise W1-01 through W1-04 using PostgreSQL synthetic fixtures; value, restart, back up and restore.
- **Expected result:** 128-hour milestone scope passes; full security/real-data release gate is still pending.
- **Status:** Planned — Not Executed.

### TC-069 — Immutable coherent snapshots

- **Level / release:** Integration / MVP.
- **Requirements:** FR-015, FR-044.
- **Setup and steps:** Freeze endpoints/report while another session revises observations; request a date before any observation.
- **Expected result:** One coherent source version; saved values stay unchanged; no future data backfilled; source changes invalidate completeness assertion.
- **Status:** Planned — Not Executed.

### TC-070 — CI controls

- **Level / release:** System / MVP.
- **Requirements:** FR-046.
- **Setup and steps:** Review/run applicable CI with synthetic fixtures and no deployment secrets.
- **Expected result:** Applicable tests/checks run; no automatic deploy or production credentials.
- **Status:** Planned — Not Executed.

### TC-071 — Goal value without reservations

- **Level / release:** Integration / MVP.
- **Requirements:** FR-018, FR-048, NFR-008.
- **Setup and steps:** Link account to goal; race a second assignment; withdraw/change value; close goal.
- **Expected result:** At most one active goal per account; progress can fall; no blocked withdrawal or new asset; close releases links only.
- **Status:** Planned — Not Executed.

### TC-072 — Data freshness propagation

- **Level / release:** Integration / MVP.
- **Requirements:** FR-050, FR-011.
- **Setup and steps:** Carry forward observations, view pages, confirm profile unchanged, omit prices and generate snapshot/report.
- **Expected result:** Independent dates and missing/stale flags persist; only explicit review refreshes review time.
- **Status:** Planned — Not Executed.

### TC-073 — Sanitized health

- **Level / release:** Integration / MVP.
- **Requirements:** FR-045.
- **Setup and steps:** Admin inspects user/job/service/backup status with seeded private balances, filenames and prompts.
- **Expected result:** Only operational metadata appears; no financial contents or sensitive logs.
- **Status:** Planned — Not Executed.

## Verification and regressions

Run the prototype end-to-end/usable-layout subset first; full ownership/privacy and PostgreSQL scenarios follow their implementation tasks. Recheck affected exactness, movement/replay, source revision, snapshot immutability and export paths when their logic changes. Owner usability, Pi/proxy/volume and timed recovery checks require actual applicable environment evidence. No coverage percentage replaces financial/privacy invariants.

Document-only revisions use link/identifier/traceability/dependency/estimate/diff checks. They do not require launching the unchanged shell, installing Django/PostgreSQL/Docker/CasaOS, sending email, rendering unavailable diagrams or claiming application tests passed.
