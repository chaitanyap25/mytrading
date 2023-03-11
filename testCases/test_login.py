import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from testCases.confest import setup


class Test_001_Login:
    url = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    def test_login(self, setup):
        # self.driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
        self.driver = setup
        self.driver.get(self.url)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpsw(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        print(act_title)
        if act_title == "Swag Labs":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            assert False

        self.driver.close()
