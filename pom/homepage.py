from selenium.webdriver.common.by import By
from webdriver.web_driver import WebDriver


class HomePage():
    webdriver = WebDriver()

    def top_nav_cig_logo(self):
        return self.webdriver.driver.find_element(By.XPATH, '//a[@aria-label="careersingear"]')

    def input_company(self):
        return self.webdriver.driver.find_element(By.ID, 'keywords')

    def input_location(self):
        return self.webdriver.driver.find_element(By.XPATH,
                                                  "//input[@title='Please make sure the state, city or zip is correct.']")

    def button_submit(self):
        return self.webdriver.driver.find_element(By.XPATH,
                                                  "//form[@id = 'navigation-search']//button[@class= 'btn orange darken-4']")

    def core_elements(self):
        return [self.input_company(), self.input_location(), self.button_submit()]