import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
#from fastquant import get_crypto_dataget_yahoo_data, get_bt_news_sentiment
import pickle
import os.path
from os import path
import yfinance as yf
from datetime import datetime, timedelta
import config as cfg


class coin:
    name=""
    quantity=0
    originalValueUSD=0
    currentValueUSD=0
    dateBought=""
    percentIncrease=0

    def __init__(self, name, quantity):
        #self.update_coin_data()
        self.name=name
        self.quantity=quantity
        today = datetime.now().strftime("%Y-%m-%d")
        delta_date = (datetime.now() - timedelta(30))
        data = yf.Ticker("ETH-USD").history(period='1d', start=delta_date, end=today)
        closing_data = data["Close"]
        self.currentValueUSD = closing_data[30]*quantity
        self.originalValueUSD = closing_data[30]*quantity
        self.percentIncrease = 0 

    
    def update_coin_data(self):
        today = datetime.now().strftime("%Y-%m-%d")
        delta_date = (datetime.now() - timedelta(30))
        data = yf.Ticker("ETH-USD").history(period='1d', start=delta_date, end=today)
        closing_data = data["Close"]
        self.currentValueUSD = closing_data[30]*self.quantity
        self.percentIncrease = (self.currentValueUSD - self.originalValueUSD)/self.originalValueUSD
        self.print_coin_info()


    def print_coin_info(self):
        print("coin: ", self.name)
        print("quantity: ", self.quantity)
        print("original value in USD: ", self.originalValueUSD)
        print('current value in USD', self.currentValueUSD)
        print('percent increase/decrease: ', self.percentIncrease)
        print("=================================")
    
    def yftomfoolery(self):
        eth = yf.Ticker("ETH-USD")
        #print(eth.info)
        print(eth.actions)
        print('=================================')
        print(eth.financials)
        print('=================================')
        print(eth.major_holders)
        print('=================================')
        print(eth.balance_sheet)
        print('=================================')
        print(eth.earnings)
        print('=================================')
        print(eth.calendar)
        print('=================================')
        print(eth.recommendations)





class cryptoBot:
    coin_data = pd.DataFrame()
    transactions = pd.DataFrame()
    current_wallet = pd.DataFrame()
    total_days=0
    coin = ""
    current_date=""
    delta_date=""
    rsi_window=0
    transactions = ""
    bearish = False
    bullish = False
    buy = False
    sell = False
    holdings = []

    def __init__(self):
        self.load_config_data()
        self.get_crypto_data()

    # this is just my method for describing the pandas dataframe that stores my coin information
    def data_info(self):
        self.data.info()
        print(self.data.describe())

    # graphs simple moving average crossover algorithm
    def graph_smac(self):
        data = self.data
        sma1label = "SMA1 (", self.small_window, ")"
        sma2label = "SMA2 (", self.big_window, ")"

        plt.figure(figsize=(8,5))
        plt.plot(data['SMA1'], 'g--', label=sma1label)
        plt.plot(data['SMA2'], 'r--', label=sma2label)
        plt.plot(data['Close'], label="Close")
        plt.legend()
        plt.show()
    
    # is going to graph the bollinger bands algorithm
    def graph_bands(self):
        data = self.data



    # loads the config.py file and all the settings I have in it
    # coin name, moving average window size, total days of coin info to fetch, etc.
    def load_config_data(self):
        self.coin = cfg.config["coin"]
        self.total_days = cfg.config["days"]
        self.current_date = datetime.now().strftime("%Y-%m-%d")
        self.delta_date = (datetime.now() - timedelta(self.total_days)).strftime("%Y-%m-%d")
        self.rsi_window = cfg.config["rsi_window"]
        self.small_window = cfg.config["smac_fast_period"]
        self.big_window = cfg.config["smac_slow_period"]

    # uses yahoo finance to collect information on coin given in config.py
    # also computes numbers for several strategies and attaches them to self.data
    def get_crypto_data(self):
        somedata = yf.download(self.coin, self.delta_date, self.current_date)
        self.data = yf.Ticker(self.coin).history(period='1d', start=self.delta_date, end=self.current_date)
        self.data["Adj Close"] = somedata["Adj Close"]

        # SMAC
        self.data["SMA1"] = self.data['Close'].rolling(window=self.small_window).mean()
        self.data["SMA2"] = self.data['Close'].rolling(window=self.big_window).mean() 

        fasterma = self.data["SMA1"][len(self.data["SMA1"]-1)]
        slowerma = self.data["SMA2"][len(self.data["SMAw"]-1)]

        if self.bearish and fasterma > slowerma:
            self.bearish = False
            self.bullish = True

        # Bolllinger Bands
        self.data['middle_band'] = self.data['Close'].rolling(window=20).mean()
        self.data['upper_band'] = self.data['Close'].rolling(window=20).mean() + self.data['Close'].rolling(window=20).std()*2
        self.data['lower_band'] = self.data['Close'].rolling(window=20).mean() - self.data['Close'].rolling(window=20).std()*2



    # will tell me to buy or sell the given coin depending on if the market is bearish or bullish
    def buy_or_sell():
        print('this is where I test if I should buy or sell (currently based of SMAC')
 


    # loads data on my holdings and transactions
    def load_pickled_data(self):
        if path.exists("state.pickle"):
            print("found saved state, loading")
            with open('state.pickle', 'rb') as f:
                self.transactions = pickle.load(f)

            with open('wallet.pickle', 'rb') as f:
                self.wallet = pickle.load(f)
    
    # saves data on my holdings and transactions (hopefully will end up being able to plug these numbers into a ML model)
    def pickle_data(self):
        with open('state.pickle', 'wb'):
            pickle.dump(self.state, f)
        
        with open('wallet.pickle', 'wb') as f:
            pickle.dump(self.wallet, f)

        print("this is for loading info of what coins/cash I have available")


    # based off the results of buy_or_sell() will add transaction/holding information to current state
    def add_transaction(self):
        print("this is where I'm going to save my buys/saves")
        buysell = input("did you buy or sell?")
        coin = input("which coin did you buy/sell?")
        coin_val = input("coin value?")
        usd = input("value usd?")

        newRow = [self.current_date, buysell, coin, coin_val, usd]

    # I've currently moved algorithm computation to the get_coin_data() method, hopefully find a use for this code later on 
    def RSI(self):
        nums = self.data["Close"][self.total_days-self.rsi_window:self.total_days]
        i=0
        upPrices=[]
        downPrices=[]

        while(i<len(nums)-1):
            first = nums[i]
            second = nums[i+1]
            diff = abs(first-second)
            if(diff==0):
                i+=1
                continue
            
            upPrices.append(diff) if second > first else downPrices.append(diff)
            i+=1
        
        avgGain = sum(upPrices)/len(upPrices)
        avgLoss = sum(downPrices)/len(downPrices)
        #return 100 - 100/(1/(1+ratio))#there's a step after this I think?
    
    # will eventually add sentiment analysis to my computations
    def sentimentAnalysis(self):
        print("the is where I do sentiment analyis")
    
def main():
    m = cryptoBot()
    #m.data_info()
    #m.graph_smac()
    c = coin("bananas", 12341)
    #c.yftomfoolery()
    c.update_coin_data()


__name__ = "main"
if (__name__ == "main"):
   main()