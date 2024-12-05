from pages.register_page import RegisterPage


def test_successful_registration(driver):
    register_page = RegisterPage(driver)

    register_page.navigate_to_registration_page()

    first_name = "admin"
    last_name = "admin"
    email = "new_admin@admin.ru"
    password = "admin$$"
    gender = "male"

    register_page.execute_login(first_name, last_name, email, password, gender)


    assert register_page.is_registration_successful() == "Your registration completed", \
        "Registration was not successful, or success message does not match."



def test_negative_registration(driver):
    register_page = RegisterPage(driver)

    register_page.navigate_to_registration_page()

    first_name = "admin"
    last_name = "admin"
    email = "admin@admin.ru"
    password = "12345"
    gender = "male"

    register_page.execute_login(first_name, last_name, email, password, gender)


    assert register_page.actual_error() == "The password should have at least 6 characters.", \
        "Registration was not successful, or success message does not match."