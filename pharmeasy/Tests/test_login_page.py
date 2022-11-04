import datetime
import pytest

from Library.excel_lib import ReadExcel
from Library.config import Config
from POM.login_page import PharmEasy


class TestPharmEasy:
    read_xl = ReadExcel()
    data = read_xl.read_testdata()

    @pytest.mark.parametrize("mobile_number", data)
    def test_valid_credentials(self, init_driver, mobile_number):
        driver = init_driver
        pe = PharmEasy(init_driver)

        try:
            pe.click_login_icon()
            pe.enter_mobile_number(mobile_number)
            pe.click_send_OTP_button()
            pe.click_continue_button()
            pe.click_user_icon()
            pe.click_logout_button()

        except BaseException as err_msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}{td.minute}{td.second}.png"
            #path = r"C:\Users\91779\PycharmProjects\pythonProject1\screenshot\\"
            driver.save_screenshot(Config.SCREENSHOTS_PATH+name)
            raise err_msg








