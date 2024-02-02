from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from webdriver.web_driver import WebDriver


class CookiesBanner:
    web_driver = WebDriver()
    are_cookies_accepted = 0

    def cookies_button(self):
        return self.web_driver.driver.find_element(By.XPATH, '//button[@id = "onetrust-accept-btn-handler"]')

    def accept_cookies_button_if_present(self):
        try:
            self.cookies_button().click()
            self.are_cookies_accepted = 1
        except (NoSuchElementException, TimeoutException) as e:
            pass
