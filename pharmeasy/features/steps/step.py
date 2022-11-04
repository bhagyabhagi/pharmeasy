import time

from behave import *
from selenium import webdriver

@given(u'Lunch the opera browser')
def opera_browser(context):
    path = r"C:\Users\hp\PycharmProjects\pharmeasy\drivers\operadriver.exe"
    context.driver = webdriver.Opera(executable_path=path)
    context.driver.get("https://pharmeasy.in/")
    context.driver.maximize_window()
    context.driver.implicitly_wait(30)

@when(u'Open PharmEasy click on login')
def login(context):
    context.driver.find_element("xpath", '(//a[@class="c-iWbDBM c-iWbDBM-idhzjXW-css"])[1]').click()
    time.sleep(5)

@when(u'user enter the valid phone number"{phone_number}"')
def valid_phone_number(context, phone_number):
    context.driver.find_element("xpath", '//input[@placeholder="Enter your phone number"]').send_keys(phone_number)
    time.sleep(5)


@when(u'User is able to click on the send OTP button')
def otp_button(context):
    context.driver.find_element("xpath", '//button[@type="submit"]').click()
    time.sleep(20)

@when(u'User is able to click on continue')
def continue_button(context):
    context.driver.find_element("xpath", '//button[@type="submit"]').click()
    time.sleep(5)


@then(u'user is able to click on user icon')
def user_icon(context):
    context.driver.find_element("xpath", '(//a[@class="c-iWbDBM c-iWbDBM-idhzjXW-css"])[1]').click()
    time.sleep(5)


@when(u'user is able to click on logout button')
def logout_button(context):
    context.driver.find_element("xpath", '//span[text()="Logout"]').click()





