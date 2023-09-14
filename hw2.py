from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# # Amazon Logo
# driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
# # Email field
# driver.find_element(By.XPATH, "//input[@type='email']")
# # Continue button
# driver.find_element(By.XPATH, "//input[@id='continue']")
# # Conditions of use Link
# driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
# # Privacy Notice Link
# driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
# # Need help link
# driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
# # Forgot your password link
# driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")
# # Other issues with Sign-In link
# driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link]")
# # Create your Amazon account button
# driver.find_element(By.XPATH, "//a[@id='createAccountSubmit]")

# Click Orders
driver.find_element(By.XPATH, "//a[@id='nav-orders']").click()

# Verify Sign in page opened: Sign In header is visible, email input field is present

# expected result is always hard coded
expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

# compare two values to verify if they are the same
assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'
print('Test case passed')

expected_email_field = driver.find_element(By.XPATH, "//input[@type='email']")

# compare two values to verify if they are the same
assert expected_email_field, f'Expected {expected_email_field} is not found on screen'
print('Test case passed')

driver.quit()




