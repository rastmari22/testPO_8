from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    BOOKS_LINK = (By.LINK_TEXT, "Books")
    COMPUTERS_LINK = (By.LINK_TEXT, "Computers")
    ELECTRONICS_LINK = (By.LINK_TEXT, "Electronics")
    APPAREL_LINK = (By.LINK_TEXT, "Apparel & Shoes")
    DIGITAL_DOWNLOADS_LINK = (By.LINK_TEXT, "Digital downloads")
    JEWELRY_LINK = (By.LINK_TEXT, "Jewelry")
    GIFT_CARDS_LINK = (By.LINK_TEXT, "Gift Cards")

    def navigate_to_registration_page(self):
        self._driver.get("https://demowebshop.tricentis.com/register")

    def navigate_to_books(self):
        self.find(self.BOOKS_LINK).click()

    def navigate_to_computers(self):
        self.find(self.COMPUTERS_LINK).click()

    def navigate_to_electronics(self):
        self.find(self.ELECTRONICS_LINK).click()

    def navigate_to_apparel(self):
        self.find(self.APPAREL_LINK).click()

    def navigate_to_digital_downloads(self):
        self.find(self.DIGITAL_DOWNLOADS_LINK).click()

    def navigate_to_jewelry(self):
        self.find(self.JEWELRY_LINK).click()

    def navigate_to_gift_cards(self):
        self.find(self.GIFT_CARDS_LINK).click()

    def navigate_to_invalid_page(self):
        self._driver.get("https://demowebshop.tricentis.com/invalid-page")