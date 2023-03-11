from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    # self.driver = webdriver.chrome()
    driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
    driver.maximize_window()
    return driver
