
from webdriver.web_driver import WebDriver

webdriver = WebDriver()


def is_page_correct(element_list):
    for element in element_list:
        if not webdriver.is_element_displayed(element):
            is_page_correct(element_list)


