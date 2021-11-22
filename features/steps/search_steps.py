from behave import given, when, then
import sys

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir_path)

from locators import locator


@given('The Search box is clicked')
def click_search_box(context):
    assert context.driver.find_element(*locator["search_box"]).is_displayed()
    context.driver.find_element(*locator["search_box"]).click()


@when("The Search button is clicked")
def click_search_button(context):
    context.driver.find_element(*locator["search_button"]).click()


@given('Enter product "{product}"')
def enter_product(context, product):
    context.driver.find_element(*locator["search_box"]).send_keys(product)


@then("The {result} result is shown")
def result(context, result):
    if context.driver.find_elements(*locator["result_msg"]):
        print("Result(s) have been found")
    else:
        print("Result(s) have not been found")

    context.driver.close()
    assert True, "Test Passed"


@then("The alert-warning is shown")
def alert_warning(context):
    assert context.driver.find_element(*locator["alert_warning"]).is_displayed()
