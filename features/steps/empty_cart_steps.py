from behave import given, when, then, step, register_type
from selenium.webdriver.support.select import Select
import sys
import os
import parse

import time


dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir_path)

from locators import locator


@given("The Women button is clicked")
def click_women_button(context):
    context.driver.find_element(*locator["women_button"]).click()


@given("The Product name is clicked")
def click_product_name(context):
    context.driver.find_element(*locator["product_name"]).click()


@given("The Add to Cart button is clicked")
def click_add_to_cart_button(context):
    context.driver.find_element(*locator["add_to_cart"]).click()


@given("The Proceed to checkout button is clicked")
def click_checkout_button(context):
    context.driver.find_element(*locator["proceed_to_checkout"]).click()
    time.sleep(5)


@given("The Before button is clicked")
def click_before_button(context):
    context.driver.find_element(*locator["before_button"]).click()


@when("The Delete icon is clicked")
def click_delete_icon(context):
    context.driver.find_element(*locator["delete_icon"]).click()
    time.sleep(5)


@when("The Subtract icon is clicked")
def click_subtract_icon(context):
    context.driver.find_element(*locator["subtract"]).click()
    time.sleep(5)


