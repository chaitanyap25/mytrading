import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPage
from pageObjects.Login_OpstraPage import Login_OpstraPage
from testCases.confest import setup
import time

class Test_001_Login:
    # url = "https://sso.definedge.com/auth/realms/definedge/protocol/openid-connect/auth?response_type=code&client_id=opstra&redirect_uri=https://opstra.definedge.com/ssologin&state=e2cf559f-356c-425a-87e3-032097f643d0&login=true&scope=openid"
    # username = "chaitanyapawar25@gmail.com"
    # password = "trading2023"
    url = "https://web.sensibull.com/option-chain?expiry=2023-03-29&tradingsymbol=NIFTY"
    # exp_date = "29-Mar-2023"
    stk_price = "17400"
    min = 1
    exp_date = "2023 - 03 - 29"

    def test_login(self, setup):
        # self.driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
        self.driver = setup
        # self.driver
        self.driver.get(self.url)
        self.lp = Login_OpstraPage(self.driver)

        # self.lp.selectexpiry(self.exp_date)
        # wait = WebDriverWait(self.driver, 10)
        for i in range(1, 5):
            self.lp.getoptiondata(self.stk_price)
            time.sleep(1*60)

        # self.lp.clickcon()
        # self.lp.clicklo()
        # self.lp.setusername(self.username)
        # wait = WebDriverWait(self.driver, 10)
        # self.lp.setpsw(self.password)
        # self.lp.clicklogin()
        # act_title = self.driver.title
        # print(act_title)
        # self.lp.clickpo()
        # wait = WebDriverWait(self.driver, 10)
        # self.lp.clickpaper()
        # if act_title == "Swag Labs":
        #     assert True
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
        #     assert False

        self.driver.close()

# pytest -s -v --html=Reports\report.html testCases/test_login_Optra.py