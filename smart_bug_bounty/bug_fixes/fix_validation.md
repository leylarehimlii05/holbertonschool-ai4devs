# Fix Validation Report

## bug1.py (`bug1_fixed.py`)
- **Original Issue**: Off-by-one negative index slicing (`items[-(n - 1):]`) omitted the first element and returned the whole list when `n == 1`.
- **Fix Applied**: Changed slicing expression to `items[-n:]` while preserving edge-case guards for `n <= 0` and `n >= len(items)`.
- **Test Results**: All 4 test cases passed (`n=3` -> `[30, 40, 50]`, `n=1` -> `[50]`, `n=10` -> full copy, `n=0` -> `[]`).

---

## bug2.js (`bug2_fixed.js`)
- **Original Issue**: `Array.prototype.forEach` ignored `async` callbacks, returning `0` prematurely, and floating-point totals were unrounded.
- **Fix Applied**: Replaced `forEach` with `await Promise.all(cartItems.map(...))` to resolve all asynchronous discount fetches before summing, and rounded the final subtotal with `Math.round(subtotal * 100) / 100`.
- **Test Results**: All 3 test cases passed (multi-item async discount calculation `19.99 * 0.9 + 5.50 * 0.8 = 22.39`, empty cart `0`, and zero-discount precision check).

---

## bug3.java (`bug3_fixed.java`)
- **Original Issue**: 32-bit `int` multiplication overflowed on large deposits/months, and `status.equals("ACTIVE")` threw `NullPointerException` when `status` was `null`.
- **Fix Applied**: Widened arithmetic operands and return type to `long` (`(long) monthlyDeposit * months + currentBalance`) and reversed the string comparison to `"ACTIVE".equals(status)`.
- **Test Results**: All 4 test cases passed (standard balance `4000L`, overflow boundary `3_000_000_100L`, `"ACTIVE"` -> `true`, `null` -> `false`).

---

## bug4.py (`bug4_fixed.py`)
- **Original Issue**: Mutable default list `assigned_roles=[]` leaked roles across separate user registrations, and `==` key comparison was vulnerable to timing attacks and `None` values.
- **Fix Applied**: Replaced mutable default with `assigned_roles=None` creating a fresh list per call, and switched API key validation to `hmac.compare_digest()` with strict `str` type checks.
- **Test Results**: All 4 test cases passed (isolated role lists for `"alice"` and `"bob"`, valid key match `True`, invalid/None key `False`).

---

## bug5.js (`bug5_fixed.js`)
- **Original Issue**: Shallow copy via `Object.assign` mutated `userProfile.permissions` in place, and `===` ID matching failed when `targetId` was a numeric string.
- **Fix Applied**: Cloned both the profile object and nested `permissions` array using spread syntax (`[...(userProfile.permissions || []), ...newPermissions]`), and normalized IDs with `String(user.id) === String(targetId)`.
- **Test Results**: All 3 test cases passed (original `permissions` array remained unmutated, numeric `42` and string `"42"` both resolved user object, `null` returned for missing ID).
