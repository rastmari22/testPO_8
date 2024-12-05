from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ComputerPage(BasePage):
    add_button = (By.XPATH, "//input[@value='Add to cart']")
    product_items = (By.CSS_SELECTOR, '.item-box')
    qty_input = (By.CSS_SELECTOR, ".qty-input")


    product_price = (By.CSS_SELECTOR, '.actual-price')
    content_msg = (By.CSS_SELECTOR, '.content')

    bad_msg = (By.ID, "bar-notification")


    def set_qty(self, quantity):
        quantity_field = self.find(self.qty_input)
        quantity_field.clear()
        quantity_field.send_keys(quantity)
    def add_to_cart(self):
        self.find(self.add_button).click()

    def get_successful_message(self):
          return self.find(self.add_button).text

    def get_unsuccessful_message(self):
          return self.find(self.content_msg).text
