# Finance Tracker

Finance Tracker helps a small invited group track savings, current wealth, investment holdings and progress toward goals through simple manual updates.

The approved MVP includes balances/holdings, optional savings contributions and withdrawals, valuation/history, account-linked goals, an optional estimated income/expense profile and private monthly reports with generic reminder emails. Detailed expense/trade ledgers and cash reservations are deferred. Unsupported performance attribution is shown as unknown.

The accepted M-009 Django prototype is a local synthetic-data application with clear navigation, readable account cards and an intuitive account form. Its 16 hours are included in the approved 264-hour development planning baseline.

**Implemented and accepted:** TASK-001 supplies a minimal Streamlit runtime/configuration shell and focused tests. Its launcher remains unchanged.

**Implemented and accepted:** TASK-022A's separate Django shell and custom user-model foundation are integrated into local main at `18c1066`.

**Implemented and accepted:** TASK-025A's synthetic user provisioning, standard Django login/logout, sessions, CSRF and protected pages are integrated into local main at `d27f06b`. Its earlier review report records the pre-acceptance snapshot.

**M-009 completed and owner-accepted:** TASK-004A1 is integrated into local main at `6c937a6`, following accepted TASK-022A/025A. Owned synthetic USD openings, cards and Dashboard totals use disposable SQLite. Openings are starting positions, not contributions. See [closure evidence](docs/testing/M-009_CLOSURE.md) and [local setup](docs/SETUP.md). Keep the prototype synthetic and loopback-only; this is not production readiness.

The owner-requested interface revision uses Turkish pages, forms and errors, with an accessible **Koyu tema** switch on every page. Theme choice is stored in the browser; first use follows the system preference. The Turkish interface-language rule is recorded in [AGENTS.md](AGENTS.md).

**Target:** Django/PostgreSQL on Raspberry Pi 5 (8 GB), CasaOS, Docker Compose and Cloudflare Tunnel/HTTPS. Compatibility, infrastructure, CI and deployment remain later tasks. Invite-only accounts, User isolation, Admin MFA and recovery are mandatory before real users or sensitive data. Admin has no application access to private finances.

Start with the [documentation index](docs/README.md), [Charter](docs/CHARTER.md), [decisions](docs/DECISION_LOG.md) and [schedule](docs/planning/PROJECT_SCHEDULE.md). Gemini is a later consent-based explanation feature; Telegram is deferred. Documentation approval does not authorize application implementation or deployment.
