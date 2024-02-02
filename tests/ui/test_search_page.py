import time

import pytest

from pom.cookies_banner import CookiesBanner
from pom.search_results_page import SearchPage, get_random_company
from webdriver.web_driver import WebDriver


class TestSearchPage:
    webdriver = WebDriver()
    cookies_banner = CookiesBanner()
    search_results_page = SearchPage()
    are_cookies_accepted = 0

    @pytest.fixture(autouse=True, scope="function")
    def start_and_clean(self):
        self.webdriver.get_driver()
        self.webdriver.go_to_url(self.search_results_page.url)
        self.webdriver.maximize_window()
        time.sleep(2)
        if self.are_cookies_accepted == 0:
            self.cookies_banner.accept_cookies_button_if_present()
        yield
        pass

    @pytest.mark.searchpage
    @pytest.mark.parametrize("location",
                             ["Arizona",
                              "North Carolina",
                              "Florida",
                              ])
    @pytest.mark.parametrize("company",
                             [get_random_company() for x in range(3)])
    def test_filters_are_applied_with_company_checkboxes(self, location, company):
        company_box = self.search_results_page.checkbox_company(company)
        self.search_results_page.input_location().send_keys(location)
        time.sleep(2)
        company_box.click()
        self.webdriver.scroll_to_element(company_box)
        self.search_results_page.button_filter_results().click()
        time.sleep(1)
