# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return the last `n` elements of a list in their original order when `n` is a positive integer.
- **Current Issue**: Off-by-one slicing error (`items[-(n - 1):]` instead of `items[-n:]`), which omits the first element of the expected slice and fails completely when `n == 1` (`items[0:]` returns the entire list).

## bug2.js
- **Intended Behavior**: Asynchronously fetch category discount rates for each cart item, compute the discounted line totals, and return the final rounded cart total.
- **Current Issue**: `Array.prototype.forEach` does not await `async` callbacks, causing `calculateCartTotal` to return `0` before any discount fetches resolve. Additionally, floating-point arithmetic is not rounded to two decimal places.

## bug3.java
- **Intended Behavior**: Safely compute a future account balance over a given number of months and check whether an account status string equals `"ACTIVE"`.
- **Current Issue**: Multiplying `monthlyDeposit * months` as 32-bit `int` values silently overflows on large inputs, and `status.equals("ACTIVE")` throws a `NullPointerException` if `status` is `null`.

## bug4.py
- **Intended Behavior**: Assign a role to a user without leaking state across separate calls, and safely validate API keys against timing attacks or `None` values.
- **Current Issue**: Using a mutable default argument (`assigned_roles=[]`) causes roles assigned to one user to persist into subsequent calls for unrelated users. Also, `==` comparison on API keys is vulnerable to timing side-channel attacks.

## bug5.js
- **Intended Behavior**: Return a new user profile object with added permissions without mutating the original profile, and locate a user by ID regardless of whether `targetId` is passed as a number or numeric string.
- **Current Issue**: `Object.assign({}, userProfile)` only performs a shallow copy, so `updatedProfile.permissions.push(...)` mutates `userProfile.permissions` in place. Furthermore, `user.id === targetId` returns `null` when `targetId` is a stringified number (e.g., `"42"` vs `42`).
