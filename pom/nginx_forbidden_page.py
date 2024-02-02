from selenium.webdriver.common.by import By
from webdriver.web_driver import WebDriver


class ForbiddenPage:
    webdriver = WebDriver()

    def forbidden_403(self):
        return self.webdriver.driver.find_element(By.XPATH, '//h1')

    def nginx_text(self):
        return self.webdriver.driver.find_element(By.XPATH, "//center")
