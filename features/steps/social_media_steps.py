from behave import given, when, then
import sys
import os
import time

dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir_path)

from locators import locator


@when('The Product Blouse is clicked')
def click_blouse(context):
    context.driver.find_element(*locator["blouse"]).click()
    time.sleep(5)


@then('Twitter is shown')
def twitter_is_shown(context):
    context.driver.find_element(*locator["twitter"]).is_displayed()


@then('Facebook is shown')
def facebook_is_shown(context):
    context.driver.find_element(*locator["facebook"]).is_displayed()


@then('Googleplus is shown')
def google_is_shown(context):
    context.driver.find_element(*locator["googleplus"]).is_displayed()


@then('Pinterest in shown')
def pinterest_is_shown(context):
    context.driver.find_element(*locator["pinterest"]).is_displayed()