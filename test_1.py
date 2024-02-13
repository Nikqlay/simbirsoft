import datetime
import time
from testpage import *
import csv
from confest import *

with open('config.yaml') as f:
    config = yaml.safe_load(f)


def test_step1(browser, check_xyz_bank):
    logging.info('test_1 running')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    assert testpage.get_text_xyzbank() == check_xyz_bank


def test_step2(browser, check_your_name):
    logging.info('test_2 running')
    testpage = OperationsHelper(browser)
    testpage.click_costomer_login_button()
    assert testpage.get_text_your_name() == check_your_name


def test_step3(browser, check_harry_potter):
    logging.info('test_3 running')
    testpage = OperationsHelper(browser)
    testpage.select_harry_potter()
    testpage.click_submit_button()
    time.sleep(1)
    assert testpage.get_text_harry_potter() == check_harry_potter


def test_step4(browser, check_deposit):
    logging.info('test_4 running')
    testpage = OperationsHelper(browser)
    testpage.click_deposit_button()
    time.sleep(1)
    assert testpage.get_text_deposited() == check_deposit


def test_step5(browser, check_deposit_successful):
    logging.info('test_5 running')
    testpage = OperationsHelper(browser)
    testpage.enter_amount(fibofromtomorrow())
    time.sleep(1)
    testpage.click_submit_button()
    time.sleep(1)
    assert testpage.get_text_operation_successful() == check_deposit_successful


def test_step6(browser, check_withdrawn):
    logging.info('test_6 running')
    testpage = OperationsHelper(browser)
    testpage.click_withdrawn_button()
    time.sleep(1)
    assert testpage.get_text_withdrawn() == check_withdrawn


def test_step7(browser, check_withdrawn_successful, check_balance):
    logging.info('test_7 running')
    testpage = OperationsHelper(browser)
    testpage.enter_amount(fibofromtomorrow())
    time.sleep(1)
    testpage.click_submit_button()
    time.sleep(1)
    assert ((testpage.get_text_operation_successful() == check_withdrawn_successful) and
            (testpage.get_text_balance() == check_balance))


def test_step8(browser, check_transaction_credit, check_transaction_debit):
    logging.info('test_8 running')
    testpage = OperationsHelper(browser)
    testpage.click_transactions_button()
    time.sleep(1)
    assert ((testpage.get_text_credit() == check_transaction_credit) and
            (testpage.get_text_debit() == check_transaction_debit))


def test_step9(browser):
    logging.info('test_9 running')
    testpage = OperationsHelper(browser)
    date_time_credit = datetime.datetime.strptime(testpage.get_credit_date_time(), '%b %d, %Y %I:%M:%S %p')\
        .strftime("%d %m %Y %I:%M:%S")
    date_time_debit = datetime.datetime.strptime(testpage.get_debit_date_time(), '%b %d, %Y %I:%M:%S %p')\
        .strftime("%d %m %Y %I:%M:%S")

    with open("transactions.csv", mode="w", encoding='utf-8') as f:
        file_writer = csv.writer(f, delimiter=',', lineterminator='\r')
        file_writer.writerow(['Дата-времяТранзакции', ' Сумма', 'ТипТранзакции'])
        file_writer.writerow([date_time_credit, testpage.get_credit_amount(), testpage.get_text_credit()])
        file_writer.writerow([date_time_debit, testpage.get_debit_amount(), testpage.get_text_debit()])
