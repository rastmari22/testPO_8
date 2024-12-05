import pytest
from pages.search_page import SearchPage

def test_successful_search(driver):
    search_page = SearchPage(driver)

    search_page.enter_search_query("book")
    search_page.click_search()

    results = search_page.get_search_results()
    assert len(results) > 0, "No products found for the search query."


def test_unsuccessful_search(driver):
    search_page = SearchPage(driver)

    search_page.enter_search_query("ab")
    search_page.click_search()

    error_message = search_page.get_error_message()
    assert error_message == "Search term minimum length is 3 characters", "Expected error message was not displayed."

