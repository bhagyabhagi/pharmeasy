import time

from Library.excel_lib import ReadExcel
from Library.config import Config


class PharmEasy:
    read_xl = ReadExcel()
    reg_locators = read_xl.read_locators()

    def __init__(self, driver):
        self.driver = driver

    def click_login_icon(self):
        locator = self.reg_locators["click_login_icon"]
        self.driver.find_element(*locator).click()

    def enter_mobile_number(self, mobile_number):
        if isinstance(mobile_number, float):
            mobile_number = int(mobile_number)
        locator = self.reg_locators["enter_mobile_number"]
        self.driver.find_element(*locator).send_keys(mobile_number)

    def click_send_OTP_button(self):
        locator = self.reg_locators["click_send_OTP_button"]
        self.driver.find_element(*locator).click()
        time.sleep(18)

    def click_continue_button(self):
        locator = self.reg_locators["click_continue_button"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def click_user_icon(self):
        locator = self.reg_locators["click_user_icon"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def click_logout_button(self):
        locator = self.reg_locators["click_logout_button"]
        self.driver.find_element(*locator).click()
        time.sleep(3)



