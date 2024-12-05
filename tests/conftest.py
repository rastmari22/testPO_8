import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options)
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
