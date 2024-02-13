from datetime import date
import datetime
import csv
import time
#
#
# def fibofromtomorrow():
#     tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).day
#
#     def fibo(n):
#         if n == 1:
#             return 1
#         elif n == 2:
#             return 2
#         return fibo(n - 1) + fibo(n - 2)
#
#     return fibo(tomorrow)
#
# print(fibofromtomorrow())


date_time_str = 'Feb 13, 2024 6:04:17 PM'
date_time_obj = datetime.datetime.strptime(date_time_str, '%b %d, %Y %I:%M:%S %p').strftime("%d %m %Y %I:%M:%S")
print(date_time_obj)
amount = 610
transaction = 'debit'
full = [date_time_obj].extend(str(amount))
print(full)
# full = [amount].append(',')

import csv
with open("transactions.csv", mode="w", encoding='utf-8') as f:
    file_writer = csv.writer(f, delimiter = ',', lineterminator='\r')
    file_writer.writerow(['Дата-времяТранзакции', ' Сумма', 'ТипТранзакции'])
    file_writer.writerow([date_time_obj, amount, transaction])
    file_writer.writerow(['Маша', '11', '18'])
