import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from Testdata.Hompagedata import Hompagedata
from testobjects.Homepage import Homepage
from tests.baseclass import Baseclass


class Testhomepage(Baseclass):

    def test_formsubmission(self, getdata):
        log = self.test_getlogger()
        homepage = Homepage(self.driver)
        log.info("first name is "+getdata["firstname"])
        homepage.getname().send_keys(getdata["firstname"])
        log.info("first name is " + getdata["email"])
        homepage.getemail().send_keys(getdata["email"])
        homepage.getcheck().click()
        self.selectoptionbytext(homepage.getradio(),getdata["gender"])
        homepage.getsubmit().click()
        print(homepage.getalert().text)
        print(homepage.getsuccess().text)
        self.driver.refresh()

    @pytest.fixture(params=Hompagedata.getstdata("Testcase2"))
    def getdata(self, request):
        return request.param