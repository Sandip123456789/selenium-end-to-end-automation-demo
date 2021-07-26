import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        driver = self.driver

        #for logger
        log = self.getLogger()

        #Creating Objects of from Classes
        homePage = HomePage(driver)
        checkoutPage = CheckoutPage(driver)
        confirmPage = ConfirmPage(driver)

        #click shop, imported from HomePage
        homePage.getShopBtn()

        # to scroll down top to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        #click add item button, imported from CheckoutPage
        # Steps to Click on Add to cart button
        log.info("Getting all the product titles")
        products = checkoutPage.getCardTitle()
        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            print(productName)
            log.info(productName)
            if productName == "iphone X":
                # Add item into cart
                product.find_element_by_xpath("div[2]/button").click()

        # to scroll down bottom to top
        driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")

        # To click on checkout button, imported from CheckoutPage
        checkoutPage.getCheckoutList().click()

        # enter quantity no
        checkoutPage.getQuantity().clear()
        checkoutPage.getQuantity().send_keys("2")

        checkoutPage.getCheckOut().click()

        #enter country name
        confirmPage.getCountryName()

        #Click checkBox, imported from ConfirmPage
        checkbox = confirmPage.getCheckBox()
        checkbox.click()
        assert not checkbox.is_selected()

        #Click purchase button, imported from ConfirmPage
        confirmPage.getPurchaseBtn().click()

        #validating success message
        successText = driver.find_element_by_class_name("alert-success").text
        assert "Success!" in successText
        print(successText)
        log.info("Received success text is "+successText)

        # Taking screenshot
        # driver.get_screenshot_as_file("../Screenshots/successScreen.png")