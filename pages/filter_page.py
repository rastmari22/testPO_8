
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FilterPage(BasePage):
    filter_hp = (By.XPATH, "//input[@value='HP']")
    filter_dell = (By.XPATH, "//input[@value='Dell']")
    filter_show_products = (By.XPATH, "//button[contains(text(), 'Show products')]")
    product_items = (By.CSS_SELECTOR, '.item-box')

    filter_under_1000 = (By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/ul/li[1]/a")
    filter_1000_to_1200 = (By.XPATH,
                           "/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/ul/li[2]/a")
    filter_over_1200 = (By.XPATH,
                        "/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/ul/li[3]/a")

    product_price = (By.CSS_SELECTOR, '.actual-price')

    def filter_by_price_under_1000(self):
        self.find(self.filter_under_1000).click()
        log = self.get_logger()
        price_text = self.find_elements(self.product_price)
        for price in price_text:
            log.info("price_text - " + price.text)
            if float(price.text) >= 1000:
                return False
        return True

    def filter_by_price_1000_to_1200(self):
        self.find(self.filter_1000_to_1200).click()
        log = self.get_logger()
        price_text = self.find_elements(self.product_price)
        for price in price_text:
            log.info("price_text - " + price.text)
            if float(price.text) < 1000 or float(price.text) > 1200:
                return False
        return True

    def filter_by_price_over_1200(self):
        self.find(self.filter_over_1200).click()
        log = self.get_logger()
        price_text = self.find_elements(self.product_price)
        for price in price_text:
            log.info("price_text - " + price.text)
            if float(price.text) < 1200:
                return False
        return True

    def get_product_items(self):
        return self.find_elements(self.product_items)

    def get_product_names(self):
        return [item.text for item in self.get_product_items()]

    def get_product_prices(self):
        log = self.get_logger()
        price_text = self.find_elements(self.product_price)
        for price in price_text:
            log.info("price_text - " + price.text)
            if int(price.text) >= 1000:
                return False

        return price_text
