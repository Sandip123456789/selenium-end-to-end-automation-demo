from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass


class ConfirmPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def getCountryName(self):
        #for logger
        log = self.getLogger()

        log.info("Entering country name as Ge")
        self.driver.find_element_by_id("country").send_keys("Ge")

        # Explicit wait from custom utilities, imported from BaseClass
        self.verifyLinkPresence("Germany")
        self.driver.find_element_by_link_text("Germany").click()

    def getCheckBox(self):
        return self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']")
        # checkBox = self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']")
        # checkBox.click()
        # assert not checkBox.is_selected()

    def getPurchaseBtn(self):
        return self.driver.find_element_by_css_selector("input[type='submit']")