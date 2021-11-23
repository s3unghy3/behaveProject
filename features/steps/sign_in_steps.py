from behave import given, when, then
import sys

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir_path)

from locators import locator


@given('The Sign In link is clicked')
def click_signin_link(context):
    context.driver.find_element(*locator["sign_in_link"]).click()


@given('Enter email "{email}" and password "{pwd}"')
def enter_info(context, email, pwd):
    context.driver.find_element(*locator["sign_in_email"]).send_keys(email)
    context.driver.find_element(*locator["sign_in_pass"]).send_keys(pwd)


@when('Sign in button is clicked')
def click_signin_button(context):
    context.driver.find_element(*locator["sign_in_button"]).click()


@then('User logged in successfully')
def access_granted(context):
    context.driver.find_element(*locator["my_account"]).text


@given('Enter email "" and password ""')
def step_impl(context):
    context.driver.find_element(*locator["sign_in_email"]).send_keys("")
    context.driver.find_element(*locator["sign_in_pass"]).send_keys("")


@given('Enter email "" and password "debrecen"')
def step_impl(context):
    context.driver.find_element(*locator["sign_in_email"]).send_keys("")
    context.driver.find_element(*locator["sign_in_pass"]).send_keys("")


@given('Enter email "valid@email.com" and password ""')
def step_impl(context):
    context.driver.find_element(*locator["sign_in_email"]).send_keys("valid@email.com")
    context.driver.find_element(*locator["sign_in_pass"]).send_keys("")


@then("The {msg} error message is shown")
def error_msg(context, msg):
    if context.driver.find_elements(*locator["error_msg"]):
        print("Element exists")
    else:
        print("Element doesn't exist")

