from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*=shop]")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    radio = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    alert = (By.CLASS_NAME, "alert-success")
    success = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def shopitems(self):
        return self.driver.find_element(*Homepage.shop)

    def getname(self):
        return  self.driver.find_element(*Homepage.name)

    def getemail(self):
        return  self.driver.find_element(*Homepage.email)

    def getcheck(self):
        return self.driver.find_element(*Homepage.check)

    def getradio(self):
        return self.driver.find_element(*Homepage.radio)

    def getsubmit(self):
        return  self.driver.find_element(*Homepage.submit)

    def getalert(self):
        return self.driver.find_element(*Homepage.alert)

    def getsuccess(self):
        return  self.driver.find_element(*Homepage.success)
