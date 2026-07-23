from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground")

driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

time.sleep(2)

assert "simple-form-demo" in driver.current_url
print("URL assertion passed.")

# Navigate back
driver.back()

time.sleep(2)

driver.execute_script('window.open("https://www.google.com");')

time.sleep(2)

tabs = driver.window_handles
print("Open Tabs:", tabs)

# Switch to Google tab
driver.switch_to.window(tabs[1])

print("Google Tab Title:", driver.title)

driver.switch_to.window(tabs[0])

# Take screenshot
screenshot_name = "playground_screenshot.png"
driver.save_screenshot(screenshot_name)

if os.path.exists(screenshot_name):
    print("Screenshot saved successfully.")
else:
    print("Screenshot not found.")

print("Current Window Size:", driver.get_window_size())

driver.set_window_size(1280, 800)



print("Updated Window Size:", driver.get_window_size())

# Wait before closing
time.sleep(3)

# Close browser
driver.quit()