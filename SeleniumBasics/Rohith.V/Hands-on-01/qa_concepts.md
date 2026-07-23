# Handson 01: QA Concepts and Defect Management

## 1. Testing Levels

Testing is usually divided into four main levels depending on what we want to validate.

### 1. Unit Testing

- Focus: Smallest independent part of the code
- Purpose: Check whether a single function or logic unit works correctly
- Example: Testing a helper function such as validate_course_duration(duration) with values like -5 or 500

### 2. Integration Testing

- Focus: Interaction between modules or components
- Purpose: Verify that different parts of the system work together correctly
- Example: Checking whether the repository layer saves course data correctly into the database

### 3. System Testing

- Focus: Complete application behavior
- Purpose: Validate the full workflow from input to output
- Example: Sending a real request to POST /api/courses/ and confirming that the course is created successfully

### 4. User Acceptance Testing (UAT)

- Focus: Real user/business scenario
- Purpose: Confirm that the software meets business requirements
- Example: An administrator creates a course from the UI and confirms it appears in the student portal

---

## 2. Functional vs. Non-Functional Testing

### Functional Testing

- Checks whether the system does what it is supposed to do
- Examples: login, course creation, form validation, API response

### Non-Functional Testing

- Checks how well the system performs under different conditions
- Examples: performance, reliability, security, usability

### Example

A non-functional test could be:

- Send 1,000 requests to GET /api/courses/ within 2 seconds
- Verify that response time stays within the expected limit and the system remains stable

---

## 3. Black-Box vs. White-Box Testing

| Type              | Meaning                                                                       | Who Usually Performs It |
| ----------------- | ----------------------------------------------------------------------------- | ----------------------- |
| Black-Box Testing | Testing the system through inputs and outputs without examining internal code | QA Engineers / Testers  |
| White-Box Testing | Testing with knowledge of internal logic, code structure, and decision paths  | Developers              |

### Simple Difference

- Black-box testing asks: “Does the product work?”
- White-box testing asks: “Why does it work or fail?”

---

## 4. Sample Test Cases for POST /api/courses/

| Test Case ID | Scenario                                        | Preconditions                              | Expected Result                                                               |
| ------------ | ----------------------------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------- |
| TC_API_001   | Create a course with valid data                 | User is logged in with a valid admin token | API returns 201 Created and stores the course successfully                    |
| TC_API_002   | Reject course creation when the name is missing | User is logged in with a valid admin token | API returns 400 Bad Request with a message like “name is required”            |
| TC_API_003   | Block creation when duration is negative        | User is logged in with a valid admin token | API returns 400 Bad Request with a message like “duration cannot be negative” |

---

## 5. Defect Lifecycle

A defect usually moves through the following stages:

New → Assigned → Open → Fixed → Retest → Verified → Closed

### Common Statuses

- New: The defect is identified and logged
- Assigned: The issue is assigned to the responsible developer
- Open: The developer is investigating the root cause
- Fixed: The code change is completed
- Retest: QA verifies the fix again
- Verified: The defect is confirmed as resolved
- Closed: The issue is officially completed

### Other Possible Outcomes

- Rejected: The issue is not considered a real defect
- Deferred: The issue is valid but postponed for a later release

---

## 6. Bug Classification Examples

### Example A

- Defect: POST /api/courses/ returns 500 Internal Server Error for all requests
- Severity: Critical
- Priority: P1
- Reason: The core feature is completely blocked, affecting all users

### Example B

- Defect: Course names longer than 150 characters are silently truncated
- Severity: Medium
- Priority: P2
- Reason: Data integrity is affected, even though the system still runs

### Example C

- Defect: The Swagger documentation page contains a typo
- Severity: Low
- Priority: P4
- Reason: It is a cosmetic issue and does not affect system functionality

### Example D

- Defect: Login sometimes returns 401 on the first attempt
- Severity: High
- Priority: P1
- Reason: It creates a serious user experience and authentication problem

---

## 7. Sample Defect Report

**Defect ID:** BUG-DN5-001  
**Title:** API returns 500 error when creating a course  
**Environment:** QA-Staging-Cluster 02  
**Build Version:** Release v5.0-alpha-3  
**Severity:** Critical  
**Priority:** P1

### Steps to Reproduce

1. Log in to the QA environment with a valid admin account
2. Open Postman or Insomnia
3. Send a POST request to /api/courses/
4. Use the payload: {"name": "QA Basics Class", "duration": 12}
5. Click Send

### Expected Result

The API should return 201 Created and save the course successfully.

### Actual Result

The API returns 500 Internal Server Error.

### Attachment

Screenshot of the error response and server logs

---

## 8. Severity vs. Priority

### Severity

- Describes how serious the defect is from a technical point of view
- Focus: Impact on the system

### Priority

- Describes how quickly the defect should be fixed
- Focus: Business urgency

### Example

A defect may be high severity but low priority if it affects a rarely used legacy process and does not impact current users.

---

## Quick Summary

QA work is about ensuring that software is correct, reliable, and useful for real users. Good testing helps find defects early, improve quality, and build trust in the product.
