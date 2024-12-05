import pytest

from pages.cart_page import CartPage
from pages.computer_page import ComputerPage

def test_add_product_to_cart(driver):
    desktops_page = ComputerPage(driver)
    driver.get("https://demowebshop.tricentis.com/build-your-cheap-own-computer")
    desktops_page.add_to_cart()
    if desktops_page.get_successful_message():
        cart_page = CartPage(driver)
        driver.get("https://demowebshop.tricentis.com/cart")
        items = cart_page.get_item_by_name("Build your own chip computer")
        assert items , "Cart should not be empty after adding a product."

def test_negative_add_product_to_cart(driver):
    desktops_page = ComputerPage(driver)
    driver.get("https://demowebshop.tricentis.com/build-your-cheap-own-computer")
    desktops_page.set_qty(-1)
    desktops_page.add_to_cart()
    assert desktops_page.get_unsuccessful_message() == "Quantity should be positive"

def test_edit_cart_item_quantity(driver):
    desktops_page = ComputerPage(driver)
    driver.get("https://demowebshop.tricentis.com/build-your-cheap-own-computer")
    desktops_page.add_to_cart()
    item_name = "Build your own chip computer"
    new_qty = 5
    if desktops_page.get_successful_message():
        cart_page = CartPage(driver)
        driver.get("https://demowebshop.tricentis.com/cart")
        if cart_page.get_item_by_name(item_name):
            cart_page.change_item_qty(item_name, new_qty)
            real_new_qty = cart_page.check_item_qty(item_name)
            assert real_new_qty == new_qty, "unsuccessful_change qty"

