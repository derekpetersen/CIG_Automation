from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class Footer:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://www.careersingear.com/'

    def nav_to_home_page(self):
        self.driver.get(self.url)

    def link_about_cig(self):
        return self.driver.find_element(By.XPATH, '//a[contains(text(), "About CIG")]')

    def link_advertise(self):
        return self.driver.find_element(By.XPATH, '//a[contains(text(), "About CIG")]')

