# Selenium Locators and Waits Demo

A hands-on project that demonstrates different Selenium WebDriver locator strategies and waiting mechanisms using the LambdaTest Selenium Playground.

## Objective

The goal is to understand how to locate web elements using various Selenium locator strategies and learn the difference between explicit waits, implicit waits, time.sleep, and fluent waits for handling dynamic web elements.

## Concepts Covered

- Selenium locator strategies (ID, Class Name, Tag Name, XPath, CSS Selector)
- Absolute XPath vs Relative XPath
- CSS Selector by ID and attribute
- Implicit waits
- Explicit waits with WebDriverWait and expected conditions
- Fluent waits with custom polling frequency
- Time comparison between explicit wait and time.sleep
- Element clickability verification using EC.element_to_be_clickable
- Headless browser mode
- WebDriver exception handling (network errors)

## Technologies Used

- Python
- Selenium WebDriver
- Chrome Browser
- Selenium Manager (built-in driver management)

## Project Structure

```
Hands-on-05/
├── locators.py        # Demonstrates 7 different locator strategies
├── wait_demo.py       # Demonstrates explicit, fluent, and sleep-based waits
└── README.md          # This file
```

### File Descriptions

**locators.py** - A standalone script that opens the LambdaTest Simple Form Demo page and locates the message input field using seven different locator strategies: ID, Class Name, Tag Name, XPath (fallback), Relative XPath, CSS Selector by ID, and CSS Selector by attribute. Prints a success message for each strategy.

**wait_demo.py** - A standalone script that runs three demonstrations:

- Compares the speed of explicit waits versus time.sleep when waiting for an alert message to appear after clicking a button.
- Verifies that an element is clickable using EC.element_to_be_clickable before interacting with it.
- Demonstrates fluent wait by polling a dynamic data table every 0.5 seconds until the first row is visible.

Both scripts run independently using `python filename.py` and do not require Pytest.

## Setup Instructions

1. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Install dependencies:**

   These scripts only need the selenium package. Selenium Manager (bundled with Selenium 4+) handles ChromeDriver automatically.

   ```bash
   pip install selenium
   ```

   No requirements.txt file is needed for this project.

## Running the Scripts

Run the locators demo:

```bash
python locators.py
```

Run the waits demo:

```bash
python wait_demo.py
```

## Expected Output

**locators.py** - Prints a confirmation for each of the 7 locator strategies when it successfully finds the message input element on the Simple Form Demo page. Ends with a success message confirming all locators worked.

**wait_demo.py** - Performs three tasks:

- Clicks a "Normal Success" button on the Bootstrap Alert Messages Demo page and times how quickly the explicit wait catches the alert (typically under 1 second). Then compares it to the same action using time.sleep(3), showing that explicit wait is faster by approximately 2 seconds.
- Verifies the button is clickable before clicking it, confirming secure element interaction.
- Opens the Table Data Download Demo page and uses a fluent wait with 0.5 second polling to locate the first row of a dynamic table.

## Framework Design

This project does not use any test framework or design pattern. Both scripts are standalone demonstrations that run directly from the command line. No Pytest, no Page Object Model, no fixtures. The scripts are meant to be educational examples of individual Selenium features.

## Notes

- The scripts run against the **LambdaTest Selenium Playground**, which is a third-party website. The page structure and element attributes may change over time, which could cause locators to fail.
- `wait_demo.py` uses headless mode by default. Remove `options.add_argument('--headless')` to see the browser actions visually.
- The locator script uses `webdriver-manager` imported but switched to Selenium Manager for driver resolution. If you encounter driver issues, install webdriver-manager with `pip install webdriver-manager` and update the driver setup.
- A stable internet connection is required to access the LambdaTest playground pages.
- This is a learning project. The scripts are not designed for CI/CD or production use.

## Learning Outcome

After completing this hands-on, you will be able to:

- Use different Selenium locator strategies to find web elements
- Choose between ID, Class Name, Tag Name, XPath, and CSS Selector based on the element structure
- Understand why explicit waits are more efficient than hard-coded time.sleep calls
- Implement fluent waits with custom polling intervals for dynamic content
- Verify element states like clickability before performing actions
- Handle network errors gracefully in Selenium scripts
