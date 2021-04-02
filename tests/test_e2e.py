from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from testobjects.Checkoutpage import Checkoutpage
from testobjects.Confirmpage import Confirmpage
from testobjects.Homepage import Homepage
from tests.baseclass import Baseclass


class Testdemo(Baseclass):

    def test_e2e(self):
        homepage = Homepage(self.driver)
        homepage.shopitems().click()
        checkoutpage = Checkoutpage(self.driver)
        products = checkoutpage.getproducttitle()

        i = -1
        for product in products:
            i = i+1
            productname = product.text
            if productname == "Blackberry":
                checkoutpage.getproductbtn()[i].click()

        checkoutpage.clickcheckoutbtn().click()
        confirmpage = checkoutpage.getconfirm()
        #confirmpage = Confirmpage(self.driver)
        confirmpage.getsearchcountry().send_keys("ind")
        self.getwaitpresence("India")                # base class method inherited
        confirmpage.country().click()
        confirmpage.clickcheckbox().click()
        confirmpage.clickpurchasrbtn().click()
        print(confirmpage.getsuccesstext().text)
        self.driver.get_screenshot_as_file("screenshot.png")