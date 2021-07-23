from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

driver.get('https://rahulshettyacademy.com/angularpractice/')

#Clicking without using selenium .click() method
shopBtn = driver.find_element_by_link_text("Shop")
driver.execute_script("arguments[0].click();",shopBtn)

#to scroll down top to bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

#Steps to Click on Add to cart button
# driver.find_element_by_xpath("//body/app-root[1]/app-shop[1]/div[1]/div[1]/div[2]/app-card-list[1]/app-card[1]/div[1]/div[2]/button[1]").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
# //div[@class='card h-100']/div/h4/a
# //div[@class='card h-100']/div[2]/button
# //div[@class='card h-100']/div/button
for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    print(productName)
    if productName == "iphone X":
        #Add item into cart
        product.find_element_by_xpath("div[2]/button").click()

#to scroll down bottom to top
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")

#To click on checkout button
driver.find_element_by_css_selector("a[class*='btn-primary']").click()
#enter quantity no
driver.find_element_by_id("exampleInputEmail1").clear()
driver.find_element_by_id("exampleInputEmail1").send_keys("2")

driver.find_element_by_css_selector("button[class*='btn-success']").click()

driver.find_element_by_id("country").send_keys("Ge")
#Explicit wait
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Germany")))
# wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='suggestions']/ul/li/a")))

driver.find_element_by_link_text("Germany").click()
checkBox = driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']")
checkBox.click()
assert not checkBox.is_selected()

driver.find_element_by_css_selector("input[type='submit']").click()
successText = driver.find_element_by_class_name("alert-success").text
assert "Success!" in successText
print(successText)

#Taking screenshot
driver.get_screenshot_as_file("../Screenshots/successScreen.png")

time.sleep(4)

driver.close()
driver.quit()