from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.autorize_page import AuthPage
from pages.navigation_page import HomePage


def test_navigate_to_books(driver):
    home_page = HomePage(driver)
    home_page.navigate_to_books()
    assert "Books" in driver.title, "Should navigate to Books page."

def test_navigate_to_computers(driver):
    home_page = HomePage(driver)
    home_page.navigate_to_computers()
    assert "Computers" in driver.title, "Should navigate to Computers page."

def test_navigate_to_electronics(driver):
    home_page = HomePage(driver)
    home_page.navigate_to_electronics()
    assert "Electronics" in driver.title, "Should navigate to Electronics page."

def test_navigate_to_apparel(driver):
    home_page = HomePage(driver)
    home_page.navigate_to_apparel()
    assert "Apparel & Shoes" in driver.title, "Should navigate to Apparel & Shoes page."

def test_navigate_to_digital_downloads(driver):
    home_page = HomePage(driver)
    home_page.navigate_to_digital_downloads()
    assert "Digital downloads" in driver.title, "Should navigate to Digital downloads page."

def test_navigate_to_jewelry(driver):
    home_page = HomePage(driver)
    home_page.navigate_to_jewelry()
    assert "Jewelry" in driver.title, "Should navigate to Jewelry page."

def test_navigate_to_gift_cards(driver):
    home_page = HomePage(driver)
    home_page.navigate_to_gift_cards()
    assert "Gift Cards" in driver.title, "Should navigate to Gift Cards page."


def test_navigate_to_invalid_page(driver):
    home_page = HomePage(driver)
    home_page.navigate_to_invalid_page()
    try:
        error_message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Page not found')]"))
        )
        assert error_message_element.is_displayed(), "The 'Page not found' message should be displayed."

    except TimeoutException:
        assert False, "The error message 'Page not found' was not found."