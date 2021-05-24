from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Input Table in search field')
def search_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Table')

@when('Click on Amazon search icon')
def click_search(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

@then('Verify search worked')
def verify_search_worked(context):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

    # print text of variable element for test purposes
    # print(f'Actual result: {actual_result}')

    # assign variable with expected result text
    expected_result = '"Table"'

    # compare expected result to actual result and return error message if this does not match
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'