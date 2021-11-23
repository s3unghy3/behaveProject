from behave import given, when, then
import sys
import random
import os
from selenium.webdriver.support.select import Select

dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir_path)

from locators import locator


@given('The user types his/her email "{email}"')
def enter_email(context, email):
    context.driver.find_element(*locator["sign_up_email"]).send_keys(str(random.randint(0, 10000)) + email)


@when('The create an account button is clicked')
def click_create_account(context):
    context.driver.find_element(*locator["create_account_button"]).click()


@when('The user types his/her First name "{firstname}"')
def first_name(context, firstname):
    context.driver.find_element(*locator["firstname"]).send_keys(firstname)


@when('The user types his/her Last name "{lastname}"')
def last_name(context, lastname):
    context.driver.find_element(*locator["lastname"]).send_keys(lastname)


@when('The user set his/her Password "{password}"')
def set_password(context, password):
    context.driver.find_element(*locator["sign_up_password"]).send_keys(password)


@when('The user types his/her Address "{address}"')
def set_address(context, address):
    context.driver.find_element(*locator["sign_up_address"]).send_keys(address)


@when('The user types his/her City "{city}"')
def set_city(context, city):
    context.driver.find_element(*locator["city"]).send_keys(city)


@when('The user clicks his/her State "{state}"')
def set_state(context, state):

    select = Select(context.driver.find_element(*locator["state_dropdown"]))
    select.select_by_visible_text(state)


@when('The user types his/her Zip Code "{zipcode}"')
def set_zipcode(context, zipcode):
    context.driver.find_element(*locator["postcode"]).send_keys(zipcode)


@when('The user types his/her Mobile phone number "{mobile}"')
def set_mobile(context, mobile):
    context.driver.find_element(*locator["mobile"]).send_keys(mobile)


@when('The user clicks Register button')
def click_register_button(context):
    context.driver.find_element(*locator["register_button"]).click()


@then('The user created his/her account')
def account_created(context):
    assert context.driver.find_element(*locator["header_user_info"]).is_displayed()












