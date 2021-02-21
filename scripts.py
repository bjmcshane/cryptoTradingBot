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
        self.update_coin_data()
        self.name=name
        self.quantity=quantity
        #originalValueUSD
    
    def update_coin_data(self):
        today = datetime.now().strftime("%Y-%m-%d")
        self.data = yf.Ticker(self.coin).history(period='1d', start=self.delta_date, end=self.current_date)
        




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

    def __init__(self):
        self.load_config_data()
        self.get_crypto_data()


    def data_info(self):
        self.data.info()
        print(self.data.describe())


    def graph_smac(self):
        data = self.data
        
        plt.figure(figsize=(8,5))
        plt.plot(data['SMA1'], 'g--', label="SMA1")
        plt.plot(data['SMA2'], 'r--', label="SMA2")
        plt.plot(data['Close'], label="Close")
        plt.legend()
        plt.show()
    
    def graph_bands(self):
        data = self.data




    def load_config_data(self):
        self.coin = cfg.config["coin"]
        self.total_days = cfg.config["days"]
        self.current_date = datetime.now().strftime("%Y-%m-%d")
        self.delta_date = (datetime.now() - timedelta(self.total_days)).strftime("%Y-%m-%d")
        self.rsi_window = cfg.config["rsi_window"]
        self.small_window = cfg.config["smac_fast_period"]
        self.big_window = cfg.config["smac_slow_period"]

    def get_crypto_data(self):
        #somedata = yf.download(self.coin, self.delta_date, self.current_date)
        self.data = yf.Ticker(self.coin).history(period='1d', start=self.delta_date, end=self.current_date)
        self.data["Adj Close"] = somedata["Adj Close"]

        # SMAC
        self.data["SMA1"] = self.data['Close'].rolling(window=self.small_window).mean()
        self.data["SMA2"] = self.data['Close'].rolling(window=self.big_window).mean() 


        # Bolllinger Bands
        self.data['middle_band'] = self.data['Close'].rolling(window=20).mean()
        self.data['upper_band'] = self.data['Close'].rolling(window=20).mean() + self.data['Close'].rolling(window=20).std()*2
        self.data['lower_band'] = self.data['Close'].rolling(window=20).mean() - self.data['Close'].rolling(window=20).std()*2

    def buy_or_sell():
        print('this is where I test if I should buy or sell (currently based of SMAC')
 
    def pickle_coin_data(self):
        print("this is for saving data on my buys/sells")


    def load_pickled_data(self):
        if path.exists("state.pickle"):
            print("found saved state, loading")
            with open('state.pickle', 'rb') as f:
                self.transactions = pickle.load(f)

            with open('wallet.pickle', 'rb') as f:
                self.wallet = pickle.load(f)
    
    def pickle_data(self):
        with open('state.pickle', 'wb'):
            pickle.dump(self.state, f)
        
        with open('wallet.pickle', 'wb') as f:
            pickle.dump(self.wallet, f)

        print("this is for loading info of what coins/cash I have available")



    def add_transaction(self):
        print("this is where I'm going to save my buys/saves")
        buysell = input("did you buy or sell?")
        coin = input("which coin did you buy/sell?")
        coin_val = input("coin value?")
        usd = input("value usd?")

        newRow = [self.current_date, buysell, coin, coin_val, usd]


    def SMAC(self):
        

        fast_nums = self.data["Close"][self.total_days-fast_period:self.total_days]
        slow_nums = self.data["Close"][self.total_days-slow_period:self.total_days]

        fast_avg = sum(fast_nums)/len(fast_nums)
        slow_avg = sum(slow_nums)/len(slow_nums)
        
        # so when this number is crosses over 1, we know we need to buy or sell depending on direction
        return fast_avg/slow_avg

    
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
            
    def sentimentAnalysis(self):
        print("the is where I do sentiment analyis")
    
def main():
    m = cryptoBot()
    #m.data_info()
    #m.graph_smac()



__name__ = "main"
if (__name__ == "main"):
    main()