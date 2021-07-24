import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
# from utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class TestOne:
    def test_e2e(self):
        driver = self.driver

        #Creating Objects of from Classes
        homePage = HomePage(driver)
        checkoutPage = CheckoutPage(driver)
        confirmPage = ConfirmPage(driver)

        #click shop, imported from HomePage
        homePage.click_shopBtn()

        # to scroll down top to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        #click add item button, imported from CheckoutPage
        checkoutPage.click_addItem()

        # to scroll down bottom to top
        driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")

        # To click on checkout button, imported from CheckoutPage
        checkoutPage.click_checkoutList()

        # enter quantity no
        checkoutPage.enter_quantity()

        checkoutPage.click_checkOut()

        #enter country name
        confirmPage.enter_countryName()

        #Click checkBox, imported from ConfirmPage
        confirmPage.click_checkBox()

        #Click purchase button, imported from ConfirmPage
        confirmPage.click_purchaseBtn()

        #validating success message
        successText = driver.find_element_by_class_name("alert-success").text
        assert "Success!" in successText
        print(successText)

        # Taking screenshot
        driver.get_screenshot_as_file("../Screenshots/successScreen.png")