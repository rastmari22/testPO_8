from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    search_field = (By.ID, 'small-searchterms')
    search_button = (By.XPATH, '//input[@value="Search"]')
    search_results = (By.CSS_SELECTOR, '.product-item')
    no_results_message = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[3]/strong')
    error_message = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[3]/strong')

    def enter_search_query(self, query: str):
        self.get_logger().info(f"Enter search query - {query}")
        self.enter_text(self.search_field, query)

    def click_search(self):
        self.get_logger().info("Clicking search button")
        self.click(self.search_button)

    def get_search_results(self):
        return self.find_elements(self.search_results)

    def get_error_message(self):
        log = self.get_logger()
        try:
            actual_message = self.find(self.error_message).text
            log.info("Actual Error Message - " + actual_message)
            return actual_message
        except TimeoutException:
            log.warning("Error message element not found.")
            return "Error message not found."
    def get_no_results_message(self):
        log = self.get_logger()
        try:
            actual_message = self.find(self.no_results_message).text
            log.info("Actual No Results Message - " + actual_message)
            return actual_message
        except TimeoutException:
            log.warning("No results message element not found.")
            return "No results message not found."
