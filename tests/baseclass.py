import inspect

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import setup


@pytest.mark.usefixtures("setup")
class Baseclass:

    def test_getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler('logfile.log')
        formater = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formater)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def getwaitpresence(self, text):
        wait = WebDriverWait(self.driver, 6)
        wait.until(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT, text)))

    def selectoptionbytext(self,locator,text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)
