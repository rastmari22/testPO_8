from pages.autorize_page import AuthPage


def test_successful_login(driver):
    register_page = AuthPage(driver)
    register_page.navigate_to_registration_page()
    email = "admin@admin.ru"
    password = "admin$$"
    register_page.execute_login( email, password)
    assert register_page.is_registration_successful() == email, \
        "Registration was not successful, or success message does not match."

def test_unsuccessful_login(driver):
    register_page = AuthPage(driver)
    register_page.navigate_to_registration_page()
    email = "admin@admin.ru"
    password = "wrongpassword"
    register_page.execute_login(email, password)
    assert register_page.actual_error() == "Login was unsuccessful. Please correct the errors and try again.\nThe credentials provided are incorrect", \
        "Registration was not successful, or success message does not match."
