from behave import then
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)


@then('Navigate to the "{page}" page')
def nav_page(context, page):
    if page == "contact-us":
        context.driver.find_element_by_xpath("//*[@id='contact-link']/a").click()
        assert context.driver.title == "Contact us - My Store"
    if page == "sign-in":
        context.driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
        assert context.driver.title == "Login - My Store"
    if page == "cart":
        context.driver.find_element_by_xpath('//*[@id="header"]/div[3]/div/div/div[3]/div/a').click()
        assert context.driver.title == "Order - My Store"
    if page == "our stores":
        context.driver.find_element_by_xpath('//*[@id="block_various_links_footer"]/ul/li[4]/a').click()
        assert context.driver.title == "Stores - My Store"


@then('Check if the Banner exists')
def check_banner(context):
    assert context.driver.find_element_by_xpath('//*[@id="header"]/div[1]').is_displayed()
