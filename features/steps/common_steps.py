from behave import given
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)


@given('The Home page is open')
def open_website(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(10)
    context.driver.get("http://automationpractice.com/index.php")
    context.driver.maximize_window()
    assert context.driver.title == "My Store"
