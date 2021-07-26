import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    #creating tuples
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    radioBtn = (By.ID, "inlineRadio1")
    dob = (By.NAME, "bday")
    submit = (By.XPATH, "//input[@type='submit']")

    def getShopBtn(self):
        # Clicking without using selenium .click() method
        shop = self.driver.find_element_by_link_text("Shop")
        # shop.click()
        self.driver.execute_script("arguments[0].click();", shop)

    def getName(self):
        return self.driver.find_element(*HomePage.name)  # put * to say it is tuple
        # self.driver.find_element_by_name('name').send_keys("Killerbee")

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        #select class provide the methods to handle the options in dropdown (static)
        return self.driver.find_element(*HomePage.gender)

    def getRadioBtnStudent(self):
        return self.driver.find_element(*HomePage.radioBtn)

    def getDOB(self):
        return self.driver.find_element(*HomePage.dob)

    def getSubmitBtn(self):
        return self.driver.find_element(*HomePage.submit)

