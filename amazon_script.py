from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:\_AQA\python-selenium-automation\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.amazon.com/')

# locate search field element
search_field = driver.find_element(By.ID, 'twotabsearchtextbox')

# input Table into search field
search_field.send_keys('Table')

# locate search button
search_icon = driver.find_element(By.ID, 'nav-search-submit-button')

# click search button
search_icon.click()

# assign variable to XPATH element specifically it's text
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

#print text of variable element for test purposes
#print(f'Actual result: {actual_result}')

# assign variable with expected result text
expected_result = '"Table"'

# compare expected result to actual result and return error message if this does not match
assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'

# close browser
driver.quit()


