import logging
import yaml
from datetime import date
import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select


def parse_locators(filename: str):
    ids = dict()
    with open(filename) as f:
        locators = yaml.safe_load(f)
    if 'xpath' in locators.keys():
        for locator in locators['xpath'].keys():
            ids[locator] = (By.XPATH, locators['xpath'][locator])
    if 'css' in locators.keys():
        for locator in locators['css'].keys():
            ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])
    return ids


def fibofromtomorrow():
    tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).day

    def fibo(n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return fibo(n - 1) + fibo(n - 2)

    return fibo(tomorrow)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                          message=f'Cant find element by locator{locator}')
        except:
            logging.exception('Find element exсeptoin')
            element = None
        return element

    def go_to_site(self, url='https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'):
        try:
            start_browsing = self.driver.get(url)
        except:
            logging.exception('Exeption while open site')
            start_browsing = None
        return start_browsing

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f'Exception while button click')
            return False
        logging.debug(f'Clicked {element_name}')
        return True

    def select_value(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        select = self.find_element(locator)
        if not select:
            return False
        try:
            users = self.find_element(locator)
            user = Select(users)
            user.select_by_value('2')
        except:
            logging.exception(f'Exception while button click')
            return False
        logging.debug(f'Clicked {element_name}')
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator)
        if not field:
            logging.error(f' Element {locator} not found')
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get text from {element_name}')
            return None
        logging.info(f'Find text {text} in {field}')
        return text

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f' Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operation with {element_name}')
            return False
        return True
