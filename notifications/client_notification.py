import schedule, time
import threading
from aiogram import types, Dispatcher
from create_bot import dp, bot
from socket import socket

def greeting():
#     # t = threading.Timer(10.0, greeting)
#     # t.start()
    print('Hello!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#     # await bot.send_message(
#     #     message.from_user.id,
#     #     "Привет. Я market-bot). Ведите тикер акции или облигации для получения информации"
#     #     )
# t = threading.Timer(10.0, greeting)
# t.start()
# t.cancel()
# print('Выполнено')


# def run_threated(job_func):
#     job_thread = threading.Thread(target=schedule)
#     job_thread.start()

# # def get_notification():
# schedule.every().day.at('14:03').do(run_threated, greeting)
        
# while True:
#     schedule.run_pending()
#     time.sleep(1)

import threading
import time 
import schedule

def run_continuously(interval=2): 
    """Continuously run, while executing pending jobs at each elapsed time interval.
    @return cease_continuous_run: threading. Event which can be set to cease continuous run. 
    Please note that it is *intended behavior that run_continuously() does not run missed jobs*. 
    For example, if you've registered a job that should run every minute and you 
    set a continuous run interval of one hour then your job won't be run 60 times at each interval but only once. """ 
    
    cease_continuous_run = threading.Event() 
    
    class ScheduleThread(threading.Thread): 
        @classmethod 
        def run(cls): 
            while not cease_continuous_run.is_set(): 
                schedule.run_pending() 
                time.sleep(interval)
                
    continuous_thread = ScheduleThread()
    continuous_thread.start() 
    return cease_continuous_run 

def background_job(): 
        print('Hello from the background thread')
         
schedule.every().day.at('14:05').do(background_job)
    
    # Start the background thread 
stop_run_continuously = run_continuously() 
    
    # Do some other things... 
time.sleep(10)
    
#     # Stop the background thread 
# stop_run_continuously.set()
