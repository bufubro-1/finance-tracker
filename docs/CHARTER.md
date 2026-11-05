# Project Charter
## Finance Tracker

**Project Name:** Finance Tracker
**Project Type:** Personal Software Development / Open Source  
**Project Status:** Planning  
**Development Approach:** Iterative and Incremental  
**Deployment:** Local Network (Self-Hosted)  
**Primary Language:** Python

---

## 1. Project Overview

Finance Tracker is a self-hosted personal finance management application designed to help individuals monitor their assets, track income and expenses, and manage financial savings goals.

The application will provide a centralized web dashboard accessible through a local network.

It will also integrate Google's Gemini API for AI-assisted financial insights and Telegram for notifications and periodic financial summaries.

The project will initially focus on single-user operation, simplicity, privacy, and maintainability rather than commercial deployment.

## 2. Problem Statement

Managing personal finances across different asset types, accounts, and financial goals can become complicated.

Individuals often rely on spreadsheets or multiple applications to track their savings, investments, and spending.

These approaches may lack centralized reporting, automated progress tracking, and personalized insights.

Personal Wealth Tracker aims to address these problems by combining financial records, goal monitoring, and AI-assisted analysis in one lightweight application.

## 3. Project Objectives

The primary objectives are:

1. **Centralized Asset Management:** Enable users to record and monitor their financial assets from a single dashboard.
2. **Income and Expense Tracking:** Provide a structured system for recording financial transactions and calculating savings.
3. **Financial Goal Management:** Allow users to create savings goals with target amounts and deadlines.
4. **AI-Assisted Insights:** Integrate Gemini to explain spending patterns, savings progress, and financial summaries.
5. **Telegram Integration:** Deliver configurable financial reports, reminders, and goal updates.
6. **Local-First Operation:** Store financial data locally and allow dashboard access within a trusted local network.
7. **Open-Source Development:** Maintain a documented and reproducible project on GitHub without exposing personal financial data.

## 4. Project Scope

### 4.1 In Scope

**Financial Dashboard**
- Total assets and estimated net worth
- Asset distribution charts
- Monthly income and expense summaries
- Historical financial trends
- Savings rate calculations

**Asset Management**
- Manual asset registration
- Support for cash, currencies, gold, stocks, and investment funds
- Recording asset quantities and transaction history
- Portfolio valuation using manually entered prices initially

**Financial Goals**
- Creating and editing multiple savings goals
- Defining target amounts and target dates
- Allocating existing savings to goals
- Calculating monthly required contributions
- Visualizing goal completion percentages
- Avoiding double-counting funds assigned to different goals

**AI Integration**
- Gemini API integration
- Spending pattern explanations
- Savings goal feasibility analysis
- Natural-language financial summaries
- User-initiated financial questions

**Telegram Integration**
- Connecting a personal Telegram account through a bot
- Weekly or monthly financial summaries
- Savings goal reminders
- Configurable notifications

**Data Management**
- Local SQLite database
- Basic backup and restore capabilities
- Data export to CSV
- Configuration through environment variables

### 4.2 Out of Scope

The following features are excluded from the initial project:

- Commercial financial services
- Multi-user account management
- Direct banking integrations
- Automated investment trading
- Portfolio rebalancing transactions
- Mobile application development
- Public cloud hosting
- Real-time market trading functionality
- Cryptocurrency wallet connections
- Personalized regulated investment advice

These features may be reconsidered in future versions but are not project commitments.

## 5. Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Web Interface | Streamlit |
| Database | SQLite |
| Data Processing | Pandas |
| Data Visualization | Plotly |
| AI Integration | Google Gemini API |
| Notifications | Telegram Bot API |
| Configuration | Python environment variables |
| Version Control | Git / GitHub |
| Deployment | Local machine / Local network |

The architecture should remain modular so individual integrations can be replaced without major changes to the core application.

## 6. Key Deliverables

**D1 — Working Web Dashboard**

A locally accessible Streamlit application displaying financial information and relevant visualizations.

**D2 — Financial Data Management Module**

A persistent database and interfaces for managing assets, income, expenses, and financial transactions.

**D3 — Financial Goal Tracking Module**

A goal management system with target calculations, savings allocations, and progress tracking.

**D4 — Gemini Integration**

An AI assistant capable of analyzing approved financial summaries and providing natural-language explanations.

**D5 — Telegram Integration**

A Telegram bot that sends scheduled reports and notifications.

**D6 — Project Documentation**

A GitHub repository containing installation instructions, configuration examples, application architecture, and usage documentation.

## 7. Project Milestones

| Phase | Milestone | Expected Outcome |
|---|---|---|
| Phase 1 | Project Foundation | Repository, project structure, database |
| Phase 2 | Financial Tracking | Asset and transaction management |
| Phase 3 | Dashboard | Charts, summaries, net worth tracking |
| Phase 4 | Goal Management | Savings targets and progress calculations |
| Phase 5 | AI Integration | Gemini financial insights |
| Phase 6 | Telegram Integration | Notifications and periodic reports |
| Phase 7 | Testing & Documentation | Stable, documented local release |

Milestone dates will be determined based on development progress and available time.

## 8. Stakeholders

| Stakeholder | Responsibility |
|---|---|
| Project Owner | Defines requirements, priorities, and success criteria |
| Developer | Designs, implements, tests, and maintains the application |
| End User | Uses the application and evaluates its functionality |
| External API Providers | Provide optional AI and messaging capabilities |

Initially, the project owner, developer, and primary end user may be the same individual.

## 9. Assumptions and Constraints

### Assumptions
- The application will initially serve one user.
- Financial data will primarily be entered manually.
- Users will supply their own API credentials.
- Internet access will be available when external integrations are required.
- The application will run on a personal computer or local server.

### Constraints
- The project should minimize operating costs.
- Core financial features must work without Gemini or Telegram.
- Sensitive financial information must not be committed to GitHub.
- Third-party API usage may be subject to rate limits, costs, and availability.
- The dashboard is intended for trusted local-network access, not public internet exposure.
- Development complexity should remain proportional to personal usage requirements.

## 10. Risks and Mitigation Strategies

| Risk | Mitigation |
|---|---|
| Financial data loss | Database backups and export functionality |
| Incorrect financial calculations | Unit tests and deterministic calculation functions |
| Gemini produces inaccurate advice | Use validated calculations and restrict AI to explanatory assistance |
| API downtime | Keep core features independent of external services |
| Unauthorized network access | Limit access to trusted devices and networks; use firewall restrictions |
| Sensitive data exposure | Git exclusions, environment variables, and data minimization |
| Project scope expansion | Maintain a prioritized backlog and explicit out-of-scope list |
| Incorrect portfolio valuation | Display valuation timestamps and identify missing or outdated prices |

## 11. Security and Privacy Requirements

Since the application handles sensitive financial information, privacy and security are essential.

The system must:

- Store user financial records locally by default.
- Avoid committing database files, API keys, or personal records to GitHub.
- Keep Gemini and Telegram integrations optional.
- Send only necessary financial context to external AI services.
- Restrict Telegram commands to explicitly authorized users.
- Avoid logging credentials or sensitive prompts.
- Protect access to the dashboard on the local network.
- Provide backup and recovery procedures.

Local hosting alone does not guarantee privacy or security. Devices on the network must be considered when configuring access.

## 12. Success Criteria

The project will be considered successful when:

- [ ] The user can launch the application locally using documented instructions.
- [ ] Assets and transactions can be created, edited, and deleted.
- [ ] Financial records persist after restarting the application.
- [ ] The dashboard correctly calculates total assets and net worth.
- [ ] Income, expenses, and savings are reported accurately.
- [ ] The user can define and track multiple financial goals.
- [ ] Funds allocated to different goals are not double-counted.
- [ ] Gemini can explain financial summaries without performing unauthorized financial operations.
- [ ] Telegram can deliver configured reports to the authorized user.
- [ ] Core application features remain operational when external APIs are unavailable.
- [ ] Sensitive configuration and financial data are excluded from the public repository.
- [ ] Essential financial calculations and data operations are covered by automated tests.

## 13. Future Enhancement Opportunities

Potential enhancements include:

- Automated market price updates
- Multi-currency financial analysis
- Inflation-adjusted performance tracking
- Advanced portfolio analytics
- Automated recurring transaction entry
- AI-assisted budget categorization
- Financial forecasting and scenario simulations
- Improved responsive dashboard layouts

These enhancements are optional and will be evaluated only after the core application is functional.

## 14. Project Authorization

The Project Charter defines the initial objectives, scope, constraints, deliverables, and success criteria of Personal Wealth Tracker.

Development may begin with Phase 1: Project Foundation.

Any major changes to project scope should be documented before implementation.

**Project Owner:** Solo Developer  
**Approval Status:** Proposed — Pending Owner Approval
