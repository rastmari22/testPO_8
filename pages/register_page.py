from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterPage(BasePage):
    FirstName = (By.ID, "FirstName")
    LastName = (By.ID, "LastName")
    Email = (By.ID, "Email")
    Password = (By.ID, "Password")
    ConfirmPassword = (By.ID, "ConfirmPassword")
    gender_male = (By.ID, "gender-male")
    gender_female = (By.ID, "gender-female")
    # gender
    # email
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='result']")
    REGISTER_BUTTON = (By.ID, "register-button")

    submit_button = (By.XPATH, "//*[@class='oxd-form']/div[3]/button")
    # error_message = (By.XPATH, "//*[@class='orangehrm-login-error']/div[1]/div[1]/p")
    error_message = (By.CSS_SELECTOR, ".field-validation-error[data-valmsg-for='Password'] span")
    def navigate_to_registration_page(self):
        self._driver.get("https://demowebshop.tricentis.com/register")
    def execute_login(self,
                      FirstName: str,
                      LastName: str,
                      Email: str,
                      Password: str,
                      gender: str):

        log = self.get_logger()

        log.info("Enter FirstName - " + FirstName)
        self.find(self.FirstName).send_keys(FirstName)
        log.info("Enter LastName - " + LastName)
        self.find(self.LastName).send_keys(LastName)
        log.info("Enter Email - " + Email)
        self.find(self.Email).send_keys(Email)
        log.info("Enter Password - " + Password)
        self.find(self.Password).send_keys(Password)
        self.find(self.ConfirmPassword).send_keys(Password)

        if gender.lower() == "male":
            self.find(self.gender_male).click()
        elif gender.lower() == "female":
            self.find(self.gender_female).click()


        self.find(self.REGISTER_BUTTON).click()

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