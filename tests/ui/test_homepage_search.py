import time

import allure
import pytest
from pom.cookies_banner import CookiesBanner
from pom.homepage import HomePage
from pom.search_results_page import SearchPage, get_random_company
from pom.nginx_forbidden_page import ForbiddenPage
from webdriver.web_driver import WebDriver
from util.timeouts import Timeout


class TestHomePageSearch:
    home_page = HomePage()
    search_results_page = SearchPage()
    webdriver = WebDriver()
    cookies_button = CookiesBanner()
    forbidden_page = ForbiddenPage()

    @allure.step('Going to homepage')
    def go_to_homepage(self):
        self.webdriver.get_driver()
        self.webdriver.go_to_home_page()
        # time.sleep(Timeout.SMALL.value)

    @pytest.fixture(autouse=True, scope="function")
    def start_and_clean(self):
        self.go_to_homepage()
        yield
        pass

    @pytest.mark.ui
    @pytest.mark.homepage
    @pytest.mark.parametrize("company,location",
                             [("Penske", "Arizona"),
                              ("Covenant", "North Carolina"),
                              ("Crete Carrier", "Nevada")])
    def test_search_by_company_and_location_is_reflected_in_the_url(self, company, location):
        with allure.step('Filling input fields'):
            time.sleep(Timeout.SMALL.value)
            self.home_page.input_company().send_keys(company)
            self.home_page.input_location().send_keys(location)
        self.home_page.button_submit().click()
        time.sleep(Timeout.SMALL.value)
        expected_location = location.replace(" ", "+")
        expected_company = company.replace(" ", "+")
        assert expected_company in self.home_page.webdriver.driver.current_url
        assert expected_location in self.home_page.webdriver.driver.current_url

    @pytest.mark.ui
    @pytest.mark.homepage
    @pytest.mark.parametrize("company,location",
                             [("Penske", "Arizona"),
                              ("Covenant", "North Carolina"),
                              ("Crete", "Nevada")])
    def test_search_by_company_and_location_is_reflected_filter_chip(self, company, location):
        self.webdriver.maximize_window()
        time.sleep(Timeout.SMALL.value)
        self.home_page.input_company().send_keys(company)
        self.home_page.input_location().send_keys(location)
        self.home_page.button_submit().click()
        time.sleep(Timeout.SMALL.value)
        displayed_company = self.search_results_page.displayed_companies()
        displayed_location = self.search_results_page.displayed_location()
        displayed_company_text = [company_element.get_attribute('innerHTML') for company_element in displayed_company]
        displayed_location_text = [location_element.get_attribute('innerHTML') for location_element in
                                   displayed_location]
        assert company in displayed_company_text
        assert location in displayed_location_text

    @pytest.mark.parametrize("company,location",
                             [
                                 (0, ""),
                                 ("#", "@"),
                             ])
    def test_negative_inputs_in_main_search(self, company, location):
        time.sleep(Timeout.SMALL.value)
        self.home_page.input_company().send_keys(company)
        self.home_page.input_location().send_keys(location)
        self.home_page.button_submit().click()
        time.sleep(Timeout.SMALL.value)
        assert "https://www.careersingear.com/" == self.webdriver.current_url()

    @pytest.mark.parametrize("company,location",
                             [
                                 ("@", "SELECT * FROM information_schema.tables;"),
                                 ("SELECT * FROM information_schema.tables;", "1234")

                             ])
    def test_to_verify_sql_injection_fails_in_search(self, company, location):
        time.sleep(Timeout.SMALL.value)
        self.home_page.input_company().send_keys(company)
        self.home_page.input_location().send_keys(location)
        self.home_page.button_submit().click()
        time.sleep(Timeout.SMALL.value)
        self.forbidden_page.forbidden_403()
