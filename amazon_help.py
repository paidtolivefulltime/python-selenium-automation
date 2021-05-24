from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path='C:\_AQA\python-selenium-automation\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

# locate search field element
search_field = driver.find_element(By.ID, 'helpsearch')

#clear search field element
search_field.clear()

# input Table into search field
search_field.send_keys('Cancel order')

#sends enter key command for search field
search_field.send_keys(Keys.RETURN)

# locate search button
#search_icon = driver.find_element(By.ID, 'nav-search-submit-button')

# click search button
#search_icon.click()

# assign variable to XPATH element specifically it's text
# actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
actual_result = driver.find_element(By.XPATH, "//h1[text()='Cancel Items or Orders']").text
# /html/body/div[2]/div[2]/div[1]/div/div[3]/div/div[1]/h2/a


#print text of variable element for test purposes
print(f'Actual result: {actual_result}')

# assign variable with expected result text
expected_result = 'Cancel Items or Orders'

# compare expected result to actual result and return error message if this does not match
assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'

# close browser
driver.quit()


