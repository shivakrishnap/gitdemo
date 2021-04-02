#self.driver.find_element_by_id("country")
#self.driver.find_element_by_link_text("India")
#self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']")
#self.driver.find_element_by_xpath("//input[@value='Purchase']")
#self.driver.find_element_by_css_selector(".alert-success")
from selenium.webdriver.common.by import By


class Confirmpage:

    def __init__(self, driver):
        self.driver = driver

    searchcountry = (By.ID, "country")
    getcountry = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchasebtn = (By.XPATH, "//input[@value='Purchase']")
    successtext = (By.CSS_SELECTOR, ".alert-success")

    def getsearchcountry(self):
        return self.driver.find_element(*Confirmpage.searchcountry)
    def country(self):
        return self.driver.find_element(*Confirmpage.getcountry)
    def clickcheckbox(self):
        return self.driver.find_element(*Confirmpage.checkbox)
    def clickpurchasrbtn(self):
        return self.driver.find_element(*Confirmpage.purchasebtn)
    def getsuccesstext(self):
        return self.driver.find_element(*Confirmpage.successtext)