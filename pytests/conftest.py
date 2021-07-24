from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--ignore-certificate-errors")

    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get('https://rahulshettyacademy.com/angularpractice/')

    request.cls.driver = driver

    yield
    driver.close()
    driver.quit()