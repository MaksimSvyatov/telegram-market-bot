from datetime import datetime
from create_bot import dp, bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import requests
import json

async def daily_job():
    # message = "Job is working"
    data = requests.get(
            f"https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/GAZP.json"
    ).text
        # url = f'https://www.moex.com/en/issue.aspx?board=TQBR&code={ticker}'
    data = json.loads(data)
    share_current_price_index = data["marketdata"]["columns"].index("LCURRENTPRICE")
        # try:
    data_list = data["marketdata"]["data"][0]
    share_current_price = data_list[share_current_price_index]
    message = f"11-00 Current share price is {share_current_price} {datetime.now()}"
    await bot.send_message(chat_id=99117096, text=message)

scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
scheduler.add_job(daily_job, trigger='cron', day_of_week = '*', hour = '10', minute = '00')

scheduler.start()






















# from aiogram import types, Dispatcher
# from create_bot import dp, bot
# from datetime import datetime
# import requests
# import json
# import threading
# import time
# import schedule
# import asyncio
# import aioschedule

# async def noon_print():
#     print("It's noon!")

# async def scheduler():
#     aioschedule.every().day.at("12:00").do(noon_print)
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)

# async def on_startup(_):
#     asyncio.create_task(scheduler())

# def run_continuously(interval=2): 
#     """Continuously run, while executing pending jobs at each elapsed time interval.
#     @return cease_continuous_run: threading. Event which can be set to cease continuous run. 
#     Please note that it is *intended behavior that run_continuously() does not run missed jobs*. 
#     For example, if you've registered a job that should run every minute and you 
#     set a continuous run interval of one hour then your job won't be run 60 times at each interval but only once. """ 
    
#     cease_continuous_run = threading.Event() 
    
#     class ScheduleThread(threading.Thread): 
#         @classmethod 
#         def run(cls): 
#             while not cease_continuous_run.is_set(): 
#                 schedule.run_pending() 
#                 time.sleep(interval)
                
#     continuous_thread = ScheduleThread()
#     continuous_thread.start() 
#     return cease_continuous_run 

# # def background_job(): 
#         # print('Hello from the background thread')
# def bot_message():
#     # await bot.send_message(chat_id=99117096, text=message)
#         # messag÷e = 'SBER'
#     # if len(message.text) <= 6:
#         # ticker = 'SBER'
#         # date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    # data = requests.get(
    #         f"https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/SBER.json"
    # ).text
    #     # url = f'https://www.moex.com/en/issue.aspx?board=TQBR&code={ticker}'
    # data = json.loads(data)
    # share_current_price_index = data["marketdata"]["columns"].index("LCURRENTPRICE")
    #     # try:
    # data_list = data["marketdata"]["data"][0]
    # share_current_price = data_list[share_current_price_index]
    # message = f"Current share price is {share_current_price}"
#     # await bot.send_message(chat_id=99117096, text=message)

#             # bot.send_message(
#             #     message.from_user.id,
#     print(f"Current share price is {share_current_price}")
#                 # , 
#                 # reply_markup=nav.get_additional_info(ticker,url)
#             # )
#         # except:
#         # bot.send_message(
#         #     message.from_user.id,
#         #     f"I don't now this ticker yet, but i'm still learn) Try another one.",
#         #     )
         
# # schedule.every(2).seconds.do(bot_message)
# schedule.every().day.at('16:52').do(bot_message)
    
#     # Start the background thread 
# stop_run_continuously = run_continuously() 
    
#     # Do some other things... 
# time.sleep(10)
    
# #     # Stop the background thread 
# # stop_run_continuously.set()
