import datetime
import pytest
from POM.login_page import PharmEasy
from Library.excel_lib import ReadExcel
from Library.config import Config

class TestPharmEasy():

    read_xl = ReadExcel()
    data = read_xl.read_testdata("Sheet1")

    @pytest.mark.parametrize("phoneno","otp",data)
    def test_valid_credentials(self,phoneno,otp,init_driver):
        driver = init_driver
        dw = PharmEasy(driver)
                                    #dw=demo web shop registerpage(init_driver)
        driver = init_driver
        try:
            dw.click_register()
            dw.click_maleradio_button()
            dw.enter_firstname(f_name)
            dw.enter_lastname(l_name)
            dw.enter_email(email)
            actual = dw.enter_password(pwd)
            dw.enter_confirmpassword(c_pwd,actual)

        except BaseException as err_msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}{td.minute}{td.second}.png"
            #path = r"C:\Users\91779\PycharmProjects\pythonProject1\screenshot\\"
            driver.save_screenshot(Config.SCREENSHOTS_PATH+name)
            raise err_msg