from selenium import webdriver
from selenium.webdriver.common.by import By
# git Psw: Git@2023

class LoginPage:
    username = 'user-name'
    psw = 'password'
    login = "login-button"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, name):
        self.driver.find_element(By.ID, self.username).send_keys(name)

    def setpsw(self, password):
        self.driver.find_element(By.ID, self.psw).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.ID, self.login).click()
