# Fix Validation Report

## Bug 1 – bug1_fixed.py
- **Input**: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
- **Expected Output**: `[4, 16, 36, 64, 100]`
- **Actual Output**: `[4, 16, 36, 64, 100]` ✅
- **Validation Notes**: Syntax error fixed by adding missing colon and comparison operator changed to `==`. Output matches expected behavior.

---

## Bug 2 – bug2_fixed.js
- **Input**: `[{ name: "Alice", score: "85" }, { name: "Bob", score: "90" }, { name: "Charlie", score: "78" }]`
- **Expected Output**: `84.33333333333333`
- **Actual Output**: `84.33333333333333` ✅
- **Validation Notes**: Off-by-one error fixed by changing loop condition to `<`. Numeric string score converted properly using `Number()`.

---

## Bug 3 – bug3_fixed.py
- **Input**: `user_id = 103` (Non-existent key in dictionary)
- **Expected Output**: `"Role not found"` (Graceful default handling)
- **Actual Output**: `"Role not found"` ✅
- **Validation Notes**: Replaced direct index access with `users_db.get(user_id, {})` and fallback default, eliminating the `KeyError`.

---

## Bug 4 – bug4_fixed.js
- **Input**: Array with 2 users (1 active, 1 inactive)
- **Expected Output**: Only 1 active user returned with updated ISO timestamp. Inactive user remains unchanged.
- **Actual Output**: Active user updated and returned correctly ✅
- **Validation Notes**: Replaced mutation assignment `=` with strict equality `===` in filter, and handled async mapping via `Promise.all()`.

---

## Bug 5 – bug5_fixed.c
- **Input**: `str1 = "Hello"`, `str2 = "World"`
- **Expected Output**: Concatenated string `"HelloWorld"` and accurate string length `10`
- **Actual Output**: `Result: HelloWorld`, `Length: 10` ✅
- **Validation Notes**: Memory allocation increased by 1 byte for null terminator `\0`, and `strlen()` used instead of `sizeof()` pointer evaluation.
