import pickle
import os.path
from os import path
import pandas as pd
from datetime import datetime, date, timedelta




if path.exists('transactions.pickle'):
    exists = True
    with open('transactions.pickle', 'rb') as f:
        transactions = pickle.load(f)
else:
    exists = False
    transactions = pd.DataFrame()


print(transactions.info())

if input("Did this transaction happen today(y/n)? ") == "y":
    dateTemp = datetime.now().date()
else:
    year = input("what year ")
    month = input("what month ")
    day = input("what day ")
    dateString = "{}-{}-{}".format(year, month, day)
    dateTemp = date.fromisoformat(dateString)

buysell = input("did you buy or sell?")
coin = input("which coin did you buy/sell?")
coin_val = input("coin value?")
coin_quantity = input("how many {} did you buy?".format(coin))
Originalusd = input("value usd?")


newRow = pd.DataFrame([[dateTemp, buysell, coin, coin_val, coin_quantity, Originalusd]], columns=['date', 'action', 'coin', 'coin_val', 'coin_quantity', 'usd'])


if exists:
    transactions = transactions.append(newRow, ignore_index = True)
else:
    transactions = newRow

#print(transactions.info())
print(transactions.head())
with open('transactions.pickle', 'wb') as f:
    pickle.dump(transactions, f)
