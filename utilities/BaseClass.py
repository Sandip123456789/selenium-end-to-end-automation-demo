from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import inspect
import logging


@pytest.mark.usefixtures("setup")
class BaseClass:
    #Creating logger
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler("../utilities/logfile.log")

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # fileHandler object

        logger.setLevel(logging.DEBUG)

        return logger

    # Creating custom utilities for Explicit wait
    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 8)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectDropdownByText(self, locator, text):
        # select class provide the methods to handle the options in dropdown (static)
        # dropdown = Select(self.drivers.find_element_by_id("exampleFormControlSelect1"))
        dropdown = Select(locator)
        # dropdown.select_by_index(1)
        dropdown.select_by_visible_text(text)