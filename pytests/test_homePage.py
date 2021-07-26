import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):
    def test_homePage(self, getData):
        driver = self.driver
        #for logger
        log = self.getLogger()

        driver.implicitly_wait(10)

        #object of class HomePage
        homePage = HomePage(driver)

        log.info("Entered name is "+getData["Name"]+" and Email is "+getData["Email"])
        homePage.getName().send_keys(getData["Name"])
        homePage.getEmail().send_keys(getData["Email"])
        homePage.getPassword().send_keys(getData["Password"])
        homePage.getCheckbox().click()

        # homePage.getGender()  #imported from HomePage
        # imported from BaseClass, for reusable purpose
        self.selectDropdownByText(homePage.getGender(), getData["Gender"])

        homePage.getRadioBtnStudent().click()
        homePage.getDOB().send_keys(getData["DOB"])
        homePage.getSubmitBtn().click()

        # validating and printing success message
        message = driver.find_element_by_class_name('alert-success').text
        print(message)
        log.info(message)

        assert "Success!" in message
        #refresh before second test inputs
        self.driver.refresh()

    #Using another file to store data, imported from TestData.HomePageData
    @pytest.fixture(params=HomePageData.test_homePage_data)
    def getData(self, request):
        return request.param

    # we can also use dictionary inside list of params
    # @pytest.fixture(params=[("Killerbee", "killer@gmail.com", "killer99", "04/11/2000"),
    #                         ("Rusty", "rustyboi@gmail.com", "rusty99", "05/12/2001")
    #                         ])
    # def getData(self, request):
    #     return request.param