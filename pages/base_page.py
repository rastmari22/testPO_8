import inspect
import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)
        self._action = ActionChains(self._driver)

    def find(self, locator):
        return self._wait.until(ec.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self._wait.until(ec.visibility_of_all_elements_located(locator))

    def click(self, locator):
        element = self.find(locator)
        element.click()
        self.get_logger().info(f"Clicked on element: {locator}")

    def enter_text(self, locator, text):
        element = self.find(locator)
        element.clear()  # Очистка перед вводом
        element.send_keys(text)
        self.get_logger().info(f"Entered text '{text}' into element: {locator}")

    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler('logfile1.log')

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        logger.setLevel(logging.INFO)
        return logger