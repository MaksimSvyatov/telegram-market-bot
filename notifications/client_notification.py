from datetime import datetime
from create_bot import dp, bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from data_base import sqlite_db
import requests
import json
import asyncio

async def daily_job():
    data_base = await sqlite_db.sql_read()
    data_base_tuple = data_base[0]
    data_base_list = list(data_base_tuple)
    ticker_from_data_base = []
    quantity_from_data_base = []
    time_from_data_base = []

    for ticker in data_base_list[0]:
        ticker = data_base_list[0].split(', ')
        ticker_from_data_base.append(ticker)
    for quantity in data_base_list[1]:
        quantity = data_base_list[1].split(', ')
        quantity_from_data_base.append(quantity)
    time_from_data_base = data_base_list[2]
    print(time_from_data_base)
    ticker_from_data_base = ticker_from_data_base[0]
    quantity_from_data_base = quantity_from_data_base[0]

    for ticker in ticker_from_data_base:
        data = requests.get(
                f"https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/{ticker}.json"
        ).text
        data = json.loads(data)
        share_current_price_index = data["marketdata"]["columns"].index("LCURRENTPRICE")
        try:
            data_list = data["marketdata"]["data"][0]
            share_current_price = data_list[share_current_price_index]
            message = f"Current share price is {share_current_price} {datetime.now()}"
            await bot.send_message(chat_id=99117096, text=message)
        except:
            await bot.send_message(
                message.from_user.id,
                f"I don't now ticker {ticker} yet, but i'm still learn) Try another one.",
            )

scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
scheduler.add_job(daily_job, trigger='cron', day_of_week = '*', hour = '10', minute = '30')
scheduler.add_job(daily_job, trigger='cron', day_of_week = '*', hour = '17', minute = '45')

scheduler.start()