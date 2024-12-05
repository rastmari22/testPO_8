from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AuthPage(BasePage):
    Email = (By.ID, "Email")
    Password = (By.ID, "Password")

    SUCCESS_MESSAGE = (By.XPATH, "/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a")
    REGISTER_BUTTON = (By.ID, "register-button")
    login_BUTTON = (By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]")

    submit_button = (By.XPATH, "//*[@class='oxd-form']/div[3]/button")
    error_message = (By.CSS_SELECTOR, "div.message-error > div")
    def execute_login(self,Email: str,Password: str):
        log = self.get_logger()
        log.info("Enter Email - " + Email)
        self.find(self.Email).send_keys(Email)
        log.info("Enter Password - " + Password)
        self.find(self.Password).send_keys(Password)
        self.find(self.login_BUTTON).click()
    def navigate_to_registration_page(self):
        self._driver.get("https://demowebshop.tricentis.com/login")
    def actual_error(self):
        log = self.get_logger()
        actual_errormessage = self.find(self.error_message).text
        log.info("Actual Error Message - " + actual_errormessage)
        return actual_errormessage

    def is_registration_successful(self):
        log = self.get_logger()

        actual_SUCCESS_MESSAGE = self.find(self.SUCCESS_MESSAGE).text
        log.info("Actual Success Message - " + actual_SUCCESS_MESSAGE)
        return actual_SUCCESS_MESSAGE