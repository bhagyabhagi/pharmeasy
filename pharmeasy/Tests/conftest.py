import pytest
from Library.config import Config
from selenium import webdriver


@pytest.fixture(params=["edge", "opera", "firefox"])
def init_driver(request):
    browser = request.param

    if browser.lower() == "edge":

        driver = webdriver.Edge(executable_path=Config.MSEDGE_PATH)

    elif browser.lower() == "opera":

        driver = webdriver.Opera(executable_path=Config.OPERA_PATH)

    else:

        driver = webdriver.Firefox(executable_path=Config.FIREFOX_PATH)

    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    driver.close()





