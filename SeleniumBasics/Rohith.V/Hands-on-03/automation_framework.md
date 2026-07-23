# Hands-On 3: Test Automation Process, Lifecycle & Framework Types

## Task 2: Compare Automation Framework Types

### 21. Comparison of Automation Framework Types

### 1. Linear Framework

#### Description
The Linear Framework is the simplest type of automation framework where all test steps are written in a single script from start to finish. There is no separation of code, test data, or reusable components. It is mainly used for small projects or learning Selenium because it is easy to understand and implement.

**Advantage**
- Easy to create and suitable for beginners.

**Disadvantage**
- Code duplication is high, making maintenance difficult as the project grows.

**Example**
For the Course Management System, the Linear Framework can be used to automate a single "Create Course" functionality where all steps such as opening the browser, logging in, creating a course, and closing the browser are written in one script.

---

### 2. Modular Framework

#### Description
The Modular Framework divides the application into multiple independent modules such as Login, Courses, Students, and Faculty. Each module contains reusable functions that can be called from different test cases. This reduces code duplication and improves maintainability.

**Advantage**
- Promotes code reuse and easier maintenance.

**Disadvantage**
- Initial design and planning require more effort.

**Example**
In the Course Management System, the Login module can be reused by all test cases instead of writing the login steps repeatedly.

---

### 3. Data-Driven Framework

#### Description
In a Data-Driven Framework, test logic and test data are separated. Test data is stored in external files such as CSV, Excel, or JSON. The same automation script executes multiple times using different input values, reducing duplicate scripts.

**Advantage**
- Supports testing with multiple datasets using a single test script.

**Disadvantage**
- Managing external data files increases complexity.

**Example**
The login feature of the Course Management System can be tested using 50 different username and password combinations stored in an Excel file.

---

### 4. Keyword-Driven Framework

#### Description
The Keyword-Driven Framework allows test cases to be written using predefined keywords instead of programming code. Keywords such as Click, EnterText, OpenBrowser, and Verify are stored in an Excel sheet or another external file. The automation engine reads these keywords and performs the corresponding actions.

**Advantage**
- Non-technical team members can create and understand test cases.

**Disadvantage**
- Framework development is complex and requires additional maintenance.

**Example**
A manual tester can create login test cases using keywords without writing Selenium code.

---

### 5. Hybrid Framework

#### Description
The Hybrid Framework combines the strengths of multiple frameworks, including Modular, Data-Driven, and Keyword-Driven approaches. It is the most widely used framework in real-world Selenium projects because it provides flexibility, code reuse, scalability, and easier maintenance.

**Advantage**
- Highly scalable, reusable, and suitable for enterprise-level automation projects.

**Disadvantage**
- Initial setup takes more time and requires experienced team members.

**Example**
The Course Management System can use reusable login modules, external Excel files for test data, and Page Object Model classes to create a maintainable automation framework.

---

## Comparison Table

| Framework | Best Used For | Main Advantage | Main Disadvantage |
|------------|--------------|----------------|-------------------|
| Linear | Small projects | Easy to develop | Poor maintenance |
| Modular | Medium-sized projects | Code reuse | Requires planning |
| Data-Driven | Multiple input combinations | Reusable test data | Data management complexity |
| Keyword-Driven | Non-technical users | Less coding | Complex framework design |
| Hybrid | Enterprise projects | Flexible and scalable | Longer initial setup |

---

## 22. Recommended Framework for the Given Scenario

### Scenario

The Selenium automation team needs to:

- Test login using 50 different username and password combinations.
- Reuse login functionality across 20 different test cases.
- Allow both technical and non-technical team members to contribute to automation.

### Recommendation

The most suitable choice is a **Hybrid Framework** that combines the **Modular**, **Data-Driven**, and **Keyword-Driven** frameworks.

### Justification

**Modular Framework**
- Creates a reusable Login module that can be used by all test cases, reducing duplicate code.

**Data-Driven Framework**
- Stores login credentials in an Excel or CSV file, allowing one test script to execute with multiple datasets.

**Keyword-Driven Framework**
- Enables manual testers and business analysts to create or modify test cases using keywords without writing Python code.

### Final Conclusion

A Hybrid Framework is the best solution because it combines code reusability, multiple test data support, and ease of use for both technical and non-technical team members. It is also the most commonly used automation framework in enterprise Selenium projects.

---

## 23. Hybrid Framework Folder Structure

```text
CourseManagementAutomation/
│
├── config/
│   ├── config.py
│   └── settings.json
│
├── test_data/
│   ├── login_data.csv
│   ├── course_data.csv
│   └── users.xlsx
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── course_page.py
│   ├── student_page.py
│   └── faculty_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_create_course.py
│   ├── test_update_course.py
│   ├── test_delete_course.py
│   └── test_student.py
│
├── utilities/
│   ├── driver_factory.py
│   ├── excel_reader.py
│   ├── logger.py
│   ├── screenshot.py
│   └── wait_utils.py
│
├── reports/
│
├── screenshots/
│
├── requirements.txt
├── conftest.py
└── README.md
```

### Folder Description

- **config/** – Stores application URL, browser settings, and environment configuration.
- **test_data/** – Contains Excel, CSV, or JSON files used for Data-Driven Testing.
- **pages/** – Implements the Page Object Model (POM), where each page contains its locators and methods.
- **tests/** – Contains all Selenium test scripts.
- **utilities/** – Includes reusable helper classes such as WebDriver setup, logging, screenshots, waits, and Excel readers.
- **reports/** – Stores generated HTML or test execution reports.
- **screenshots/** – Stores screenshots captured during test failures.
- **requirements.txt** – Lists all required Python packages.
- **conftest.py** – Contains shared pytest fixtures for browser setup and teardown.
- **README.md** – Explains the project structure and execution steps.

---

## Conclusion

Among all automation framework types, the **Hybrid Framework** is the most suitable for large Selenium projects because it combines the strengths of the Modular, Data-Driven, and Keyword-Driven frameworks. It improves code reusability, simplifies maintenance, supports multiple test datasets, and enables collaboration between technical and non-technical team members. This makes it the preferred framework for enterprise-level automation projects such as the Course Management System.