# Structured Bug Reports

## Bug Report – bug1.py
- **Summary**: Syntax error and incorrect modulo logic preventing script execution and failing to isolate even numbers.
- **Root Cause**: Missing colon `:` after the `for` statement and using single equals `=` instead of comparison `==` inside the `if` condition.
- **Resolution**: Added missing syntax colon and changed assignment to equality comparison `num % 2 == 0`. (Fix suggested by AI and verified manually).
- **Lesson Learned**: Always run dynamic syntax checks before validating logical loop conditions.

---

## Bug Report – bug2.js
- **Summary**: Loop out-of-bounds error and incorrect string concatenation when calculating average grades.
- **Root Cause**: Used `<= students.length` in loop comparison causing array index overflow, combined with string representation of numeric grades causing string concatenation instead of addition.
- **Resolution**: Updated loop boundary to `< students.length` and explicitly converted string scores using `Number()`. (Fix suggested by AI with manual string-to-number casting refinement).
- **Lesson Learned**: Strict type safety and proper array bounds validation prevent common runtime reference errors in JavaScript.

---

## Bug Report – bug3.py
- **Summary**: Unhandled `KeyError` runtime exception when querying non-existent user IDs.
- **Root Cause**: Direct dictionary access `users_db[user_id]` without checking if the key exists in the collection.
- **Resolution**: Replaced direct subscript access with `.get(user_id)` and added a fallback message `"Role not found"`. (AI-generated fix with added null check handling).
- **Lesson Learned**: Avoid direct dictionary index references for user input or dynamic lookup parameters.

---

## Bug Report – bug4.js
- **Summary**: Unexpected array mutation inside filter logic and unresolved asynchronous operations.
- **Root Cause**: Single `=` in `.filter()` mutated state to `true` for all elements, and `async` callbacks inside `.forEach()` did not wait for Promise resolution.
- **Resolution**: Corrected comparison operator to `===` and restructured async iteration using `Promise.all()` and `.map()`. (AI-generated architecture fix).
- **Lesson Learned**: `forEach` does not await promises; asynchronous array mapping must always be wrapped with `Promise.all()`.

---

## Bug Report – bug5.c
- **Summary**: Buffer overflow risk from missing null terminator memory allocation and wrong size calculation.
- **Root Cause**: `malloc` allocated exact combined string length without space for `\0`, and `sizeof(result)` evaluated pointer size instead of string length.
- **Resolution**: Added `+ 1` byte to `malloc` allocation and replaced `sizeof()` with `strlen()`. (Suggested by AI with added dynamic allocation error check).
- **Lesson Learned**: C string functions strictly rely on null terminators (`\0`); dynamic memory allocation must always account for terminator bytes.
