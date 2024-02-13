from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from datetime import date
import datetime
from time import sleep


service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# driver = webdriver.Chrome()
wait = WebDriverWait(driver, 90)
driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
#driver.maximize_window()


def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return fibo(n - 1) + fibo(n - 2)


try:
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "XYZ Bank"))  # Дождаться загрузки страницы
    print('XYZ Bank')
    sleep(2)

    if True:
        try:
            print("Проверяем кнопку")
            driver.find_element(By.XPATH, "//*[text()='Customer Login']")
            sleep(1)
            print("кнопка есть")
            driver.find_element(By.XPATH, '//button[contains(@ng-click,"customer()")]').click()
            sleep(1)
            print("Кликаем")
            print("ок")
        except:
            print("что-то пошло не так")
            sleep(0)

    if True:
        try:
            wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Your Name"))  # Дождаться загрузки страницы
            print('Your Name :')
            sleep(2)
            Select(driver.find_element(By.NAME, 'userSelect')).select_by_value('2')
            print('Your Name : Harry Potter')
            wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@type,"submit")]')))
            sleep(2)
            driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
            print('submit')
        except:
            print("что-то пошло не так")
            sleep(0)

    if True:
        try:
            wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Welcome"))
            wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Harry Potter"))
            print('Welcome: Harry Potter')
            sleep(2)
            driver.find_element(By.XPATH, '//button[contains(@ng-click,"deposit")]').click()
        except:
            print("что-то пошло не так")
            sleep(0)

    today = date.today()
    print("Current date =", today)
    tomorrowday = (datetime.datetime.now() + datetime.timedelta(days=1)).day
    print("Tomorrow date =", tomorrowday)

    deposit = fibo(tomorrowday)
    print("deposit =", deposit)

    if True:
        try:
            wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Amount to be Deposited :"))
            wait.until(EC.visibility_of_element_located((By.XPATH, '//input[contains(@type,"number")]')))
            print('Amount to be Deposited: ', deposit)
            sleep(2)
            driver.find_element(By.XPATH, '//input[contains(@type,"number")]').send_keys(deposit)
            sleep(2)
            driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
            print('replenished')
            wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Deposit Successful"))
            print('Deposit Successful')
            balance = driver.find_elements(By.XPATH, '//strong[contains(@class,"ng-binding")]')[1].text
            print(balance)
            assert int(balance) == int(deposit)
            print('ok')
        except:
            print("что-то пошло не так")
            sleep(0)

    if True:
        try:
            driver.find_element(By.XPATH, '//button[contains(@ng-click,"withdrawl")]').click()
            wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Amount to be Withdrawn :"))
            wait.until(EC.visibility_of_element_located((By.XPATH, '//input[contains(@type,"number")]')))
            print('Amount to be Withdrawn: ', deposit)
            sleep(2)
            driver.find_element(By.XPATH, '//input[contains(@type,"number")]').send_keys(deposit)
            sleep(2)
            driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
            print('Withdrawn')
            wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Transaction successful"))
            print('Transaction successful')
            newbalance = driver.find_elements(By.XPATH, '//strong[contains(@class,"ng-binding")]')[1].text
            print(newbalance)
            assert int(newbalance) == 0
        except:
            print("что-то пошло не так")
            sleep(0)


    if True:
        try:
            driver.find_element(By.XPATH, '//button[contains(@ng-click,"transactions")]').click()
            wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Transaction Type"))
            print("Transaction Type")
            credit = driver.find_element(By.CSS_SELECTOR, '#anchor0 > td:nth-child(3)').text
            print(credit)
            debit = driver.find_element(By.CSS_SELECTOR, '#anchor1 > td:nth-child(3)').text
            print(debit)
            assert ((str(credit) == "Credit") and (str(debit) == "Debit"))
        except:
            print("что-то пошло не так")
            sleep(0)



    print("Выход")
    sleep(2)

finally:
    print("Выполнено")
    sleep(2)
    driver.quit()
