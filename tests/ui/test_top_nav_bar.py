import time

import pytest
from webdriver.web_driver import WebDriver
from pom.nav_bar import TopNavBar


class TestNavBar:
    webdriver = WebDriver()
    nav_bar = TopNavBar()

    @pytest.fixture(autouse=True, scope="function")
    def start_and_clean(self):
        self.webdriver.get_driver()
        self.webdriver.go_to_home_page()
        yield
        pass

    def test_company_navbar_link(self):
        # self.webdriver.get_driver()
        self.webdriver.go_to_home_page()
        time.sleep(1)
        company_link = self.nav_bar.link_company()
        company_link.click()
        assert "companies" in self.webdriver.current_url()
