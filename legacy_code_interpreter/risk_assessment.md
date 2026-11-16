# Risk Assessment - LegacyIMS

This document identifies, categorizes, and prioritizes technical, security, and operational risks discovered in the Legacy Inventory & Order Management System (`LegacyIMS`).

## Prioritized Risk Table

| Risk | Severity | Notes |
| :--- | :--- | :--- |
| **SQL Injection Vulnerabilities** | High | Raw user inputs from `$_REQUEST` and `$_POST` are concatenated directly into `mysql_query()` strings across `process_order.php` and `includes/auth.php` without parameterization. |
| **Weak Authentication & Password Storage** | High | User passwords are hashed with unsalted `MD5`, and "remember me" tokens use predictable `md5($username . time())` values, exposing accounts to credential stuffing and rainbow-table attacks. |
| **Deprecated Runtime & API Usage (PHP 5.6 / `mysql_*`)** | High | Relies on End-of-Life PHP 5.6 and removed `mysql_*` extensions, blocking security patches and preventing upgrades to modern PHP 8.x environments. |
| **Hardcoded Credentials & Endpoints** | High | Database passwords and external SOAP ERP API keys are hardcoded directly inside `config.php` and `cron/erp_sync.php` in plaintext. |
| **Non-Transactional Batch Updates** | High | `sync_warehouse_stock()` executes autocommit `UPDATE` queries inside loops without `BEGIN`/`ROLLBACK` transactions, risking partial inventory corruption on failure. |
| **Missing Automated Unit & Integration Tests** | Medium | Zero automated test suite exists; any refactoring or bug fix in core billing (`calculate_final_invoice()`) risks silent regressions in production. |
| **Tight Coupling & Global State** | Medium | Business logic, SQL queries, and HTML output are mixed in 2,000+ LOC files relying on global variables (`$db_conn`, `$current_user`), making isolated changes difficult. |
| **Stored Cross-Site Scripting (XSS)** | Medium | Database fields are echoed directly into HTML tables in `reports/ledger.php` without `htmlspecialchars()` escaping, combined with outdated jQuery 1.8.3. |
| **Unbounded Memory Usage in Reporting** | Low | `generate_monthly_ledger()` loads entire query result sets into memory at once instead of streaming, causing occasional out-of-memory timeouts on large date ranges. |
| **Lack of Structured Application Logging** | Low | Errors and failed login attempts are either suppressed (`@mysql_query`) or echoed directly to users rather than written to structured audit logs, slowing incident debugging. |
