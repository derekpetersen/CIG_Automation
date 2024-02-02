from selenium.webdriver.common.by import By
from webdriver.web_driver import WebDriver
import random


def get_random_company():
    webdriver = WebDriver()
    search_results_page = SearchPage()
    webdriver.get_driver()
    webdriver.go_to_url(search_results_page.url)
    webdriver.maximize_window()
    list_of_companies = search_results_page.get_companies_as_string()
    number_of_companies = len(list_of_companies)
    return list_of_companies[random.randint(0, number_of_companies - 1)]


class SearchPage:
    web_driver = WebDriver()
    url = 'https://www.careersingear.com/search'

    def displayed_companies(self):
        return self.web_driver.driver.find_elements(By.XPATH, '//div[@class = "filter-chip"]')

    def displayed_location(self):
        return self.web_driver.driver.find_elements(By.XPATH, '//div[@class = "filter-chip"]')

    def get_companies_as_string(self):
        all_companies = self.web_driver.driver.find_elements(By.XPATH, '//form[@id = "search-filter"]//input[@type = "checkbox" and contains(@id, "company")]')
        return [company.get_attribute('value') for company in all_companies]
        # number_of_companies = len(list_of_companies)
        # return list_of_companies[random.randint(0, number_of_companies - 1)]

    def checkbox_company(self, company_value):
        return self.web_driver.driver.find_element(By.XPATH, f'//form[@id = "search-filter"]//label[@for= "company-{company_value}"]')

    def button_filter_results(self):
        return self.web_driver.driver.find_element(By.XPATH, '//button[@type = "submit" and contains(text(), "Filter Results")]')

    def input_location(self):
        return self.web_driver.driver.find_element(By.XPATH, '//form[@id = "search-filter"]//input[@name = "location"]')