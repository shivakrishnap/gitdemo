#self.driver.find_elements_by_xpath("//div[@class='card h-100']")
#driver.find_element_by_xpath("div/button")
#self.driver.find_element_by_css_selector("a.btn-primary")
#self.driver.find_element_by_xpath("//button[@class='btn btn-success']")
from selenium.webdriver.common.by import By

from testobjects.Confirmpage import Confirmpage  # page object optimisation


class Checkoutpage:

    def __init__(self, driver):
        self.driver = driver

    producttitle = (By.XPATH, "//div[@class='card h-100']")
    productbtn = (By.XPATH, "div/button")
    checkoutbtn = (By.CSS_SELECTOR, "a.btn-primary")
    confirmbtn = (By.XPATH, "//button[@class='btn btn-success']")

    def getproducttitle(self):
        return self.driver.find_elements(*Checkoutpage.producttitle)

    def getproductbtn(self):
        return self.driver.find_element(*Checkoutpage.productbtn)

    def clickcheckoutbtn(self):
        return self.driver.find_element(*Checkoutpage.checkoutbtn)

    def getconfirm(self):
        self.driver.find_element(*Checkoutpage.confirmbtn).click()
        confirmpage = Confirmpage(self.driver)
        return confirmpage
