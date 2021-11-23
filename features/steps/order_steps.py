from behave import given, when, then, step, register_type
from selenium.webdriver.support.select import Select
import sys
import os
import parse

import time

dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir_path)

from locators import locator


@given("Another Checkout button is clicked")
def click_checkout(context):
    context.driver.find_element(*locator["checkout"]).click()
    time.sleep(5)


@given("Checkout in Address is clicked")
def click_address_checkout(context):
    context.driver.find_element(*locator["address_checkout"]).click()
    time.sleep(5)


@given('Sign in button is clicked')
def click_sign_in_button(context):
    context.driver.find_element(*locator["sign_in_button"]).click()


@given("Terms of service is checked")
def check_terms_of_service(context):
    context.driver.find_element(*locator["service"]).click()
    time.sleep(5)

@given("Checkout in Shipping is clicked")
def click_shipping_checkout(context):
    context.driver.find_element(*locator["shipping_checkout"]).click()
    time.sleep(5)

@given("The Payment button is clicked")
def click_payment_button(context):
    context.driver.find_element(*locator["payment"]).click()
    time.sleep(5)


@when("The Confirm order button is clicked")
def click_confirm_order_button(context):
    context.driver.find_element(*locator["confirm_order"]).click()
    time.sleep(5)


@then("Order confirmation is shown")
def confirm_order_info(context):
    assert context.driver.find_element(*locator["order-confirmation"]).is_displayed()

