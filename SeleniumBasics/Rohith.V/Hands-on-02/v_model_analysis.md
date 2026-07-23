# Hands-On 2: SDLC vs TDLC — V-Model & Agile QA Integration

## Task 1: V-Model Mapping

### 1. The V-Model Diagram

```text
  SDLC (Verification / Design)              TDLC (Validation / Testing)
  ────────────────────────────              ───────────────────────────
  Requirements Analysis ──────────────────> Acceptance Testing
         │                                         ▲
         ▼                                         │
   System Design ─────────────────────────> System Testing
         │                                         ▲
         ▼                                         │
   Architecture Design ───────────────────> Integration Testing
         │                                         ▲
         ▼                                         │
    Module Design ────────────────────────> Unit Testing
         │                                         ▲
         ▼                                         │
      [Coding] ────────────────────────────────────┘



### 2. Mapped Phases & Test Artifacts

- **Requirements Analysis ──> Acceptance Testing**: The Acceptance Test Plan and user acceptance testing strategies are drafted during this phase based on the business requirements documentation.
- **System Design ──> System Testing**: The System Test Plan and complete end-to-end functional test cases are prepared here using the functional specifications layout.
- **Architecture Design ──> Integration Testing**: The Integration Test Plan along with technical API/interface verification test scripts are constructed from the subsystem interaction designs.
- **Module Design ──> Unit Testing**: The Unit Test Scenarios and basic logic input/output verification paths are mapped out alongside the low-level code module specifications.

### 3. Entry & Exit Criteria for the 4 Testing Levels

| Testing Level | Entry Criteria | Exit Criteria |
| :--- | :--- | :--- |
| **Unit Testing** | - Code module compilation succeeds.<br>- Developer code peer review is complete.<br>- Unit test scripts/stubs are written. | - 100% of planned unit tests pass.<br>- Code statement coverage goals are achieved (e.g., minimum 80%). |
| **Integration Testing** | - All targeted modules clear unit testing.<br>- Subsystem components are deployed to the integration stack.<br>- Test database connections are verified. | - All integration tests execute successfully.<br>- Component interface data transfers cleanly with zero corruption.<br>- Zero open Blocker or Critical severity integration defects. |
| **System Testing** | - Integration testing sign-off is completed.<br>- Stable software build is deployed to the QA environment.<br>- Test environments and data pools are prepared. | - 100% of the system test cases are executed.<br>- Planned test cases achieve a minimum 95% pass rate.<br>- Zero open Critical or High severity bugs remain active in the system tracker. |
| **Acceptance Testing** | - System testing phase achieves formal sign-off.<br>- UAT environment is verified to mirror production setup.<br>- Final business test data sets are loaded. | - Business stakeholders sign off on all completed user stories.<br>- Software aligns entirely with user requirements documents.<br>- User guides and support documents are validated. |

### 4. QA Engagement Points in the Course Management API Project

- **Point 1 (Requirements Phase Review)**: QA reviews user requirement specifications early on the left side of the V-Model. Catching logical gaps (e.g., confirming if a course code must be alpha-numeric or purely numbers) prevents building flawed logic.
- **Point 2 (API Schema Review)**: Reviewing the Swagger/OpenAPI models during the Architecture Design phase. Ensuring the dev and QA teams agree on technical exception handling patterns (like uniform error codes for missing fields) saves massive debugging time during integration.

## Task 2: Agile QA and Shift-Left Testing

### 5. Three Problems Caused by Traditional Waterfall Testing

- **Late Defect Discovery**: Testing happens at the absolute end. Discovering a fatal structural database flaw late in system testing requires rewriting massive portions of stable code.
- **Compressed Timelines**: Any development delays directly cut into the QA timeline. This forces testers to scramble and drop edge-case workflows to hit deployment deadlines.
- **High Fix Costs**: Repairing functional gaps or architectural misunderstandings late in the project lifecycle is significantly more expensive than addressing them during design reviews.

### 6. QA Roles in Agile Ceremonies

- **Sprint Planning**: QA updates user stories by defining clean, logical Acceptance Criteria and ensures tasks are realistic relative to the Definition of Done (DoD).
- **Daily Standup**: QA reports progress on testing tasks, tracks incoming hotfixes, and speaks up about blocked items (e.g., missing API endpoints or environmental drops).
- **Sprint Review**: QA joins the demo of functional increments to stakeholders and reports metrics on testing coverage execution.
- **Sprint Retrospective**: QA helps analyze quality leaks, examines the cause of any bugs escaping into production, and suggests adjustments to clean up future sprint steps.

### 7. Four Shift-Left Practices Applied to the Course Management API

- **(a) Reviewing Requirements for Testability**: QA clarifies vague phrases like "fast loading times" to "API response times under 200ms" before coders create the database operations.
- **(b) Writing Test Cases Before Code (TDD/BDD)**: QA defines validation scenarios first. Developers use these structured parameters as clear targets for code completion.
- **(c) Static Code Analysis**: Pushing backend code changes through automatic linters (e.g., Flake8 or SonarQube) checks for basic errors and security drops before integration testing begins.
- **(d) API Contract Testing Before Integration**: Running quick automated checks to ensure the API matches the Swagger blueprint allows component layers to be validated independently before full end-to-end setups are built.

### 8. Acceptance Criteria in Given-When-Then (Gherkin) Format

```gherkin
Feature: Course Creation Management

  Scenario: Create a new course successfully (Happy Path)
    Given the college admin is authenticated into the API system
    When they send a POST request to "/api/courses/" with name "DevOps Basics" and code "CS-102"
    Then the API should return an HTTP status code 201
    And the response body should contain a valid unique course ID
    And the course record should be successfully saved to the system database

  Scenario: Prevent creation of a duplicate course code
    Given the college admin is authenticated into the API system
    And a course with the code "CS-102" already exists in the system database
    When they send a POST request to "/api/courses/" with name "Advanced DevOps" and code "CS-102"
    Then the API should return an HTTP status code 400
    And the response error message should state "Course code already exists"

  Scenario: Prevent course creation when required fields are missing
    Given the college admin is authenticated into the API system
    When they send a POST request to "/api/courses/" with a blank name field and code "CS-105"
    Then the API should return an HTTP status code 400
    And the response error message should state "Course name field is required"
```