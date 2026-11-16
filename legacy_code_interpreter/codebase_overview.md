# Codebase Overview - Legacy Inventory & Order Management System (LegacyIMS)

## Age
- **First Release:** 2008 (v1.0)
- **Last Major Update:** 2016 (v2.4)
- **Active Maintenance Status:** Deprecated / Maintenance-only mode for over 10 years, still running core warehouse and billing workflows in production.

## Size
- **Total Lines of Code (LOC):** ~48,500 LOC
- **Language Breakdown:**
  - PHP 5.6 (procedural scripts & legacy classes): ~34,000 LOC (70%)
  - Raw SQL / Stored Procedures: ~8,500 LOC (18%)
  - Vanilla JavaScript / jQuery 1.8: ~6,000 LOC (12%)
- **File Count:** 215 source files across flat, unorganized directories (`/includes`, `/admin`, `/reports`).

## Dependencies
- **Runtime:** PHP 5.6 (End-of-Life since December 2018; incompatible with PHP 8.x without major refactoring).
- **Database:** MySQL 5.5 / 5.6 using deprecated `mysql_*` procedural extension instead of PDO or MySQLi.
- **Frontend:** jQuery 1.8.3 and Bootstrap 2.3 (known XSS vulnerabilities, unmaintained).
- **Authentication & Security:** Custom session-based auth relying on unsalted `MD5` password hashing and `register_globals`-style superglobal access (`$_REQUEST`).
- **External Integrations:** Hardcoded SOAP XML endpoints for legacy ERP sync and local file-system CSV exports.

## Issues
- **Zero Automated Test Coverage:** No unit, integration, or end-to-end tests exist; all verification is performed manually in production or staging.
- **Mixed Procedural and OOP Styles:** Business logic, database queries, and HTML presentation are tightly coupled inside single monolithic files (e.g., `process_order.php` exceeds 2,400 LOC).
- **Critical Security Vulnerabilities:** Widespread string concatenation in SQL queries (SQL injection risks), lack of CSRF tokens on state-changing forms, and outdated `MD5` password storage.
- **High Coupling & Global State:** Heavy reliance on global variables (`$db_conn`, `$current_user`) and direct `include` chains makes isolated refactoring high-risk.
- **Undocumented Business Rules:** Tax calculations, discount tiers, and inventory locking logic are buried inside nested conditional blocks with no inline comments or architectural documentation.
