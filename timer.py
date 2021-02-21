#from schedule import *
import schedule
import time
import scripts
#print(schedule.__file__)
#print(schedule.__doc__)
#print(dir(schedule))
def job():
    m = cryptoBot()
'''
schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)
'''
schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
