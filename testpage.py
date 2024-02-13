from BaseApp import BasePage
from BaseApp import parse_locators
from BaseApp import fibofromtomorrow
from selenium.webdriver.common.by import By
import logging
import yaml

ids = parse_locators('locators.yaml')


class OperationsHelper(BasePage):

    def get_text_xyzbank(self):
        return self.get_text_from_element(ids['LOCATOR_XYZ_BANK_FIELD'], 'text_xyz_bank_error')

    def click_costomer_login_button(self):
        self.click_button(ids['LOCATOR_COSTOMER_LOGIN_BTN'], 'costomer_login_btn')

    def get_text_your_name(self):
        return self.get_text_from_element(ids['LOCATOR_YOUR_NAME_FIELD'], 'text_your_name_error')

    def select_harry_potter(self):
        self.select_value(ids['LOCATOR_SELECT_FIELD'], 'select_value_error')

    def click_submit_button(self):
        self.click_button(ids['LOCATOR_SUBMIT_BTN'], 'login_btn')

    def get_text_harry_potter(self):
        return self.get_text_from_element(ids['LOCATOR_HARRY_POTTER_FIELD'], 'text_harry_potter_error')

    def click_deposit_button(self):
        self.click_button(ids['LOCATOR_DEPOSIT_BTN'], 'deposit_btn')

    def get_text_deposited(self):
        return self.get_text_from_element(ids['LOCATOR_DEPOSIT_FIELD'], 'text_deposited_error')

    def enter_amount(self, word):
        self.enter_text_into_field(ids['LOCATOR_AMOUNT_INPUT'], word, 'amount_field')

    def get_text_operation_successful(self):
        return self.get_text_from_element(ids['LOCATOR_DEPOSIT_SUCCESSFUL_FIELD'], 'text_deposited_error')

    def click_withdrawn_button(self):
        self.click_button(ids['LOCATOR_WITHDRAWN_BTN'], 'withdrawn_btn')

    def get_text_withdrawn(self):
        return self.get_text_from_element(ids['LOCATOR_WITHDRAWN_FIELD'], 'text_deposited_error')

    def get_text_balance(self):
        return self.get_text_from_element(ids['LOCATOR_BALANCE_FIELD'], 'text_balance_error')

    def click_transactions_button(self):
        self.click_button(ids['LOCATOR_TRANSACTIONS_BTN'], 'transactions_btn')

    def get_text_credit(self):
        return self.get_text_from_element(ids['LOCATOR_CREDIT_FIELD'], 'text_credit_error')

    def get_text_debit(self):
        return self.get_text_from_element(ids['LOCATOR_DEBIT_FIELD'], 'text_debit_error')

    def get_credit_date_time(self):
        return self.get_text_from_element(ids['LOCATOR_CREDIT_DATE_TIME_FIELD'], 'text_debit_error')

    def get_credit_amount(self):
        return self.get_text_from_element(ids['LOCATOR_CREDIT_AMOUNT_FIELD'], 'text_debit_error')

    def get_debit_date_time(self):
        return self.get_text_from_element(ids['LOCATOR_DEBIT_DATE_TIME_FIELD'], 'text_debit_error')

    def get_debit_amount(self):
        return self.get_text_from_element(ids['LOCATOR_DEBIT_AMOUNT_FIELD'], 'text_debit_error')
