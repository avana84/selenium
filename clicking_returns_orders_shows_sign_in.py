from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/anavisekruna/Desktop/Automation_QA/python-selenium-automation/chromedriver')

driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()

expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
print(actual_result)
assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'