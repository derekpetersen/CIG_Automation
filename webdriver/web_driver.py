from selenium.webdriver.common.by import By
from selenium import webdriver

from singleton.singleton_decorator import singleton


@singleton
class WebDriver:
    def __init__(self):
        self.driver = None
        self.url = 'https://www.careersingear.com/'

    def get_driver(self):
        if self.driver is None:
            self.driver = webdriver.Chrome()
        return self.driver


    def go_to_home_page(self):
        self.driver.get(self.url)

    def go_to_url(self, url):
        self.driver.get(url)
        return self

    def maximize_window(self):
        self.driver.maximize_window()
        return self

    def narrow_window(self):
        self.driver.set_window_size(1100, 700)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return self

    def current_url(self):
        return self.driver.current_url

    def is_element_displayed(self, element):
       return element.is_displayed()

    def terminate_webdriver(self):
        return self.driver.quit()

