from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class OptionChainPage:


    # exp_date = "29-Mar-2023"
    # strick_price = "17400"

    def __init__(self, driver):
        self.driver = driver

    def selectexpiry(self, exp_date):
        # expiry = "//*[@id='expirySelect']/option[@value='"+exp_date+"']"
        expiry = "// *[ @ id = 'menu-'] / div[3] / ul / li[ @ data - value = '"+exp_date+"']"
        print(expiry)
        self.driver.find_element(By.ID, self.expiry).click()

    def getoptiondata(self, strick_price):

        total_row = "//*[@id='oc-table-body']/div"
        cnt = len(total_row)
        print("Total Rows: "+cnt)

        for i in cnt:
            print("Row: "+i)
            nifty = self.driver.find_element(By.ID, "//*[@id='oc-table-body']/div["+i+"]/div/div[4]").text
            print("Nifty : " + nifty)
            if nifty == strick_price:
                print("pass")
        # self.driver.find_element(By.ID, self.psw).send_keys(password)
        # EC.presence_of_element_located(By.ID, self.psw)

    def clicklogin(self):
        self.driver.find_element(By.ID, self.login).click()

    def clickcon(self):
        self.driver.find_element(By.XPATH, self.con).click()

    def clicklo(self):
        self.driver.find_element(By.XPATH, self.lo).click()

    def clickpo(self):
        self.driver.find_element(By.XPATH, self.po).click()

    def clickpaper(self):
        try:
            WebDriverWait(self.driver, 3)
            var = self.driver.find_element(By.XPATH, self.expand)
            print("count button :" + len(var))
            print("verify button :"+var.is_displayed())
            self.driver.find_element(By.XPATH, self.expand).click()
        finally:
            print("no element")

