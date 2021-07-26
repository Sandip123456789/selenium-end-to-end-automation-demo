
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def getCardTitle(self):
        return self.driver.find_elements_by_xpath("//div[@class='card h-100']")

    def getCheckoutList(self):
        # To click on checkout button
        return self.driver.find_element_by_css_selector("a[class*='btn-primary']")

    def getQuantity(self):
        # enter quantity no
        return self.driver.find_element_by_id("exampleInputEmail1")

    def getCheckOut(self):
        #This is last checkout btn or success btn
        return self.driver.find_element_by_css_selector("button[class*='btn-success']")
