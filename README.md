# Finance Tracker

Finance Tracker helps a small invited group track savings, current wealth, investment holdings and progress toward goals through simple manual updates.

The approved MVP includes balances/holdings, optional savings contributions and withdrawals, valuation/history, account-linked goals, an optional estimated income/expense profile and private monthly reports with generic reminder emails. Detailed expense/trade ledgers and cash reservations are deferred. Unsupported performance attribution is shown as unknown.

The first planned Django prototype is a local synthetic-data application with clear navigation, readable account cards and an intuitive account form. Its 16 hours are included in the 264-hour remaining development planning baseline.

**Implemented today:** accepted TASK-001 supplies a minimal Streamlit runtime/configuration shell and focused tests. Financial tracking and Django are not implemented yet. Follow [existing runtime setup](docs/SETUP.md) for that shell.

**Target:** Django/PostgreSQL on Raspberry Pi 5 (8 GB), CasaOS, Docker Compose and Cloudflare Tunnel/HTTPS. Compatibility, infrastructure, CI and deployment remain later tasks. Invite-only accounts, User isolation, Admin MFA and recovery are mandatory before real users or sensitive data. Admin has no application access to private finances.

Start with the [documentation index](docs/README.md), [Charter](docs/CHARTER.md), [decisions](docs/DECISION_LOG.md) and [schedule](docs/planning/PROJECT_SCHEDULE.md). Gemini is a later consent-based explanation feature; Telegram is deferred. Documentation approval does not authorize application implementation or deployment.
