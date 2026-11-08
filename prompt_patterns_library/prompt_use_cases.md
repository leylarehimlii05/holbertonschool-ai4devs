# Prompt Use Cases

## Code Quality
- **Refactoring**
  - **Goal**: Improve readability and performance of existing code
  - **Input**: Source code function in [LANGUAGE]
  - **Output**: Optimized code block with a detailed explanation of changes

- **Style Enforcement**
  - **Goal**: Enforce consistent naming conventions and code formatting standards
  - **Input**: Raw or unformatted code snippet
  - **Output**: Rewritten code following specified style guide (e.g., PEP 8, Airbnb JS)

- **Code Smell Identification**
  - **Goal**: Detect anti-patterns, duplicated logic, or architectural flaws
  - **Input**: Source file or multi-function snippet
  - **Output**: Categorized list of code smells and actionable recommendations

## Debugging
- **Error Log Analysis**
  - **Goal**: Identify the root cause of an application crash or runtime error
  - **Input**: Stack trace, error message, and contextual code snippet
  - **Output**: Cause analysis and corrected code solution

- **Edge Case Identification**
  - **Goal**: Uncover hidden edge cases and boundary failures in business logic
  - **Input**: Function definition and expected requirements
  - **Output**: List of potential edge cases with sample failure inputs

- **Performance Bottleneck Resolution**
  - **Goal**: Resolve slow execution or memory leaks in algorithms
  - **Input**: Slow code block and execution context/data size
  - **Output**: Optimized algorithm with time/space complexity comparison

## Documentation
- **Docstring & API Comments**
  - **Goal**: Generate standardized docstrings and inline comments for public APIs
  - **Input**: Undocumented function or class block
  - **Output**: Fully documented code with parameter descriptions and return types

- **README Generation**
  - **Goal**: Draft a comprehensive README file for a project or module
  - **Input**: Project structure, installation steps, and tech stack details
  - **Output**: Structured Markdown file with setup guides and usage examples

## Testing
- **Unit Test Generation**
  - **Goal**: Generate high-coverage unit tests for a specific module
  - **Input**: Source code function and target testing framework (e.g., PyTest, Jest)
  - **Output**: Complete test suite including happy path and failure test cases

- **Test Data Mocking**
  - **Goal**: Produce realistic mock dataset fixtures for integration testing
  - **Input**: Database schema or JSON response structure
  - **Output**: Mock data objects in JSON or fixture format

- **Regression Test Scenario Design**
  - **Goal**: Formulate test scenario steps for newly introduced features
  - **Input**: Feature requirement description or user story
  - **Output**: Step-by-step test scenarios and expected system behaviors
