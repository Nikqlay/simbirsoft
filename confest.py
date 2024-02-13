import requests
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

with open('config.yaml') as f:
    config = yaml.safe_load(f)

browser = config['browser']
site = config['address']



@pytest.fixture(scope='session')
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def check_xyz_bank():
    return "XYZ Bank"


@pytest.fixture()
def check_your_name():
    return "Your Name :"


@pytest.fixture()
def check_harry_potter():
    return 'Harry Potter'


@pytest.fixture()
def check_deposit():
    return 'Amount to be Deposited :'


@pytest.fixture()
def check_deposit_successful():
    return 'Deposit Successful'


@pytest.fixture()
def check_withdrawn():
    return 'Amount to be Withdrawn :'


@pytest.fixture()
def check_withdrawn_successful():
    return 'Transaction successful'


@pytest.fixture()
def check_balance():
    return '0'


@pytest.fixture()
def check_transaction_credit():
    return 'Credit'


@pytest.fixture()
def check_transaction_debit():
    return 'Debit'



