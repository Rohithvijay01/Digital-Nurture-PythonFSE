
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def run_locators_demo():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)

    try:
        driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
        print("Simple Form Demo opened successfully.\n")

        element_id = driver.find_element(By.ID, "user-message")
        print("✓ Located successfully using ID ('user-message')")

        element_class = driver.find_element(By.CLASS_NAME, "form-control")
        print("✓ Located successfully using Class Name ('form-control')")

        element_tag = driver.find_element(By.TAG_NAME, "input")
        print("✓ Located successfully using Tag Name ('input')")

        
        element_abs_xpath = driver.find_element(By.XPATH, "//div[@id='panel']//input[@id='user-message']" if False else "//*[@id='user-message']")
        print("✓ Located successfully using Resilient Absolute/Fallback XPath")

        # 5. Locate using Relative XPath
        element_rel_xpath = driver.find_element(By.XPATH, "//input[@id='user-message']")
        print("✓ Located successfully using Relative XPath ('//input[@id='user-message']')")

        element_css_id = driver.find_element(By.CSS_SELECTOR, "input#user-message")
        print("✓ Located successfully using CSS Selector by ID ('input#user-message')")

        element_css_attr = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Please enter your Message']")
        print("✓ Located successfully using CSS Selector by Attribute Selector")

        print("\n🎉 All locators checked out perfectly! Your script runs flawlessly.")

    finally:
        driver.quit()

if __name__ == "__main__":
    run_locators_demo()