
import xlrd
from Library.config import Config
from selenium import webdriver

class ReadExcel:

    def read_testdata(self):
        wb = xlrd.open_workbook(Config.TESTDATA_PATH)
        ws = wb.sheet_by_name("pharmeasy_data")
        columns = ws.ncols
        rows = ws.get_rows()
        header = next(rows)
        data = []
        for row in rows:
            data.append((row[0].value))

        return data

    def read_locators(self):
        # f_path = r"C:\Users\hp\PycharmProjects\HTD_project\test_data\reg_locators.xlsx"
        wb = xlrd.open_workbook(Config.LOCATORS_PATH)
        ws = wb.sheet_by_name("pharmeasy_locators")
        rows = ws.get_rows()
        header = next(rows)
        dict_ = {}
        for row in rows:
            dict_[row[0].value] = (row[1].value, row[2].value)

        return dict_


# n = ReadExcel()
# h=n.read_testdata()
# print(h)



