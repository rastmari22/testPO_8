from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    cart_icon = (By.CSS_SELECTOR, ".cart-icon")
    add_to_cart_button = (By.CSS_SELECTOR, ".add-to-cart-button")
    cart_items = (By.CSS_SELECTOR, ".cart-item-row")
    cart_item_quantity = (By.CSS_SELECTOR, ".quantity")
    update_cart_button = (By.CSS_SELECTOR, ".update-cart-button")
    remove_cart_item_button = (By.CSS_SELECTOR, ".remove")
    total_price = (By.CSS_SELECTOR, ".total-price")
    qty_input = (By.CSS_SELECTOR, ".qty-input")

    items = (By.XPATH, "/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/table/tbody/tr[1]/td[3]/a")
    def add_product_to_cart(self):
        self.click(self.add_to_cart_button)

    def view_cart(self):
        self.click(self.cart_icon)

    def edit_cart_item_quantity(self, quantity):
        quantity_field = self.find(self.cart_item_quantity)
        quantity_field.clear()
        quantity_field.send_keys(quantity)
        self.click(self.update_cart_button)

    def remove_cart_item(self):
        self.click(self.remove_cart_item_button)

    def get_cart_items(self):
        return self.find_elements(self.cart_items)

    def get_total_price(self):
        total_price_text = self.find(self.total_price).text
        return float(total_price_text.replace('$', '').strip())
    def get_item_by_name(self, item_name):
        return self.find(self.items).text == item_name

    def change_item_qty(self,item_name, new_qty):
        items = self.find_elements(self.cart_items)
        for item in items:
            name_element = item.find_element(By.CSS_SELECTOR, ".product-name")
            if name_element.text == item_name:
                qty_element = item.find_element(self.qty_input)
                qty_element.clear()
                qty_element.send_keys(str(new_qty))
                self.click(self.update_cart_button)

    def check_item_qty(self, item_name):
        items = self.find_elements(self.cart_items)
        for item in items:
            name_element = item.find_element(By.CSS_SELECTOR, ".product-name")
            if name_element.text == item_name:
                qty_element = item.find_element(self.cart_item_quantity)
                return int(qty_element.get_attribute('value'))
        return 0