import pytest

from pages.filter_page import FilterPage

def test_successful_filter_by_price_under_1000(driver):

    desktops_page = FilterPage(driver)
    driver.get("https://demowebshop.tricentis.com/desktops")

    result_exist = desktops_page.filter_by_price_under_1000()

    assert result_exist,f"Product priceis not under 1000.00"

def test_successful_filter_by_price_1000_to_1200(driver):

    desktops_page = FilterPage(driver)
    driver.get("https://demowebshop.tricentis.com/desktops")

    result_exist = desktops_page.filter_by_price_1000_to_1200()

    assert result_exist,f"Product priceis not 1000.00 - 1200"

def test_successful_filter_by_price_over_1200(driver):

    desktops_page = FilterPage(driver)
    driver.get("https://demowebshop.tricentis.com/desktops")

    result_exist = desktops_page.filter_by_price_over_1200()

    assert result_exist,f"Product priceis not over 1200.00"