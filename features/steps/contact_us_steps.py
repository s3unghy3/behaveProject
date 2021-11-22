from behave import given, when, then, step, register_type
from selenium.webdriver.support.select import Select
import sys
import os
import parse


# To enable empty rows
@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text


register_type(NullableString=parse_nullable_string)

dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir_path)

from locators import locator


@given("The Contact Us link is clicked")
def click_contact_us_link(context):
    assert context.driver.find_element(*locator["contact_us"]).is_displayed()
    context.driver.find_element(*locator["contact_us"]).click()


@given('Subject is "{subject:NullableString}"')
def subject_heading(context, subject):
    if subject == "Webmaster":
        subject = 1
    elif subject == "Customer service":
        subject = 2
    else:
        subject = 0

    select = Select(context.driver.find_element(*locator['subject_heading']))
    select.select_by_value(str(subject))


@given('The email is "{email:NullableString}"')
def email_address(context, email):
    context.driver.find_element(*locator["contact_email"]).send_keys(email)


@given('The order reference is "{ref:NullableString}"')
def order_reference(context, ref):
    context.driver.find_element(*locator["order_ref"]).send_keys(str(ref))


@given('The {message:NullableString} is written in the Message')
def write_msg(context, message):
    context.driver.find_element(*locator["contact_message"]).send_keys(message)


@when('The send button is clicked')
def send_msg(context):
    context.driver.find_element(*locator["submit_message_contact"]).click()


@then('the "{succeeded}" message is shown')
def succeeded_msg(context, succeeded):
    success = context.driver.find_element(*locator["succ_contact_msg"]).text
    assert success == succeeded, f"{succeeded}"


@then('the "{failed}" alert is shown')
def failed_msg(context, failed):
    failure = context.driver.find_element(*locator["fail_contact_msg"]).text
    assert failure == failed, f"{failed}"
