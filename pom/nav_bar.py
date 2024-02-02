from selenium.webdriver.common.by import By

from webdriver.web_driver import WebDriver
import time


class TopNavBar:
    webdriver = WebDriver()

    def link_cig_logo(self):
        return self.webdriver.driver.find_element(By.XPATH, '//a[@aria-label="careersingear"]')

    def link_company(self):
        return self.webdriver.driver.find_element(By.XPATH, '//a[contains(text(), "Company")]')

    def link_state(self):
        return self.webdriver.driver.find_element(By.XPATH, '//a[contains(text(), "State")]')

    def link_haul_type(self):
        return self.webdriver.driver.find_element(By.XPATH, '//a[contains(text(), "Haul Type")]')

    # Element not visible on the home page
    def link_magnify_glass_search(self):
        return self.webdriver.driver.find_element(By.XPATH, '//i[contains(@class, "nav-search-icon")]')

