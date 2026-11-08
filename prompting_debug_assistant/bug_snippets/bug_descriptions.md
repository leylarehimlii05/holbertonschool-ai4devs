# Bug Descriptions

## Bug 1 – bug1.py
- **Intended Behavior**: Return the square of all even numbers in a given list.
- **Issue Type**: Syntax Error & Logical Error.
- **Notes**: Contains invalid syntax and incorrect modulo logic.

## Bug 2 – bug2.js
- **Intended Behavior**: Calculate the average grade from an array of student objects.
- **Issue Type**: Off-by-one / Loop logic & Type Coercion Error.
- **Notes**: Iterates beyond array bounds and concatenates strings instead of adding numbers.

## Bug 3 – bug3.py
- **Intended Behavior**: Safely fetch a user profile by ID from a dictionary database.
- **Issue Type**: Runtime Exception (KeyError & Unhandled NoneType).
- **Notes**: Throws an unhandled KeyError when a non-existent ID is passed.

## Bug 4 – bug4.js
- **Intended Behavior**: Filter out inactive users and update their last active timestamps asynchronously.
- **Issue Type**: Misuse of Data Types & Async/Promise handling issue.
- **Notes**: Fails to await async array mapping and mutates state unexpectedly.

## Bug 5 – bug5.c
- **Intended Behavior**: Concatenate two C-style strings safely and return the result length.
- **Issue Type**: Pointer / Memory Off-By-One & Missing Null Terminator.
- **Notes**: Out-of-bounds array access due to missing null terminator space allocation.
