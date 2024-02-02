import pytest
from webdriver.web_driver import WebDriver


@pytest.fixture(autouse=True, scope="session")
def initialize_test():
    base_page = WebDriver()
    base_page.get_driver()
    yield
    base_page.get_driver().close()
