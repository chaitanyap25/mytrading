import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPage
from pageObjects.Login_OpstraPage import Login_OpstraPage
from pageObjects.Option_ChainPage import OptionChainPage
from testCases.confest import setup


class Option_Chain:
    url = "https://www.nseindia.com/option-chain"
    exp_date = "29-Mar-2023"
    stk_price = "17400"

    def __init__(self):
        self.lp = OptionChainPage(self.driver)
        self.driver = setup

    def test_login(self, setup):
        # self.driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
        # self.driver
        self.driver.get(self.url)

        self.lp.selectexpiry(self.exp_date)
        wait = WebDriverWait(self.driver, 10)
        self.lp.getoptiondata(self.stk_price)

        self.driver.close()

# pytest -s -v --html=Reports\report.html testCases/option_chain.py