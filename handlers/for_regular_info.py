from aiogram import types
from create_bot import dp, bot
import time
import requests
import json



# Захародкоженный кусок для проверки работы оповещений о цене актива

users_list = ['SBER', 'GAZP', 'LKOH', 'TRNFP']
@dp.message_handler(commands=["start", "help"])
async def get_daily_info(message: types.Message):
    for i in range(2):    
        for ticker in users_list:
            time.sleep(1)
            data = requests.get(
            f"https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/{ticker}.json"
            ).text
            data = json.loads(data)
            share_current_price_index = data["marketdata"]["columns"].index("LCURRENTPRICE")
            data_list = data["marketdata"]["data"][0]
            share_current_price = data_list[share_current_price_index]
            await bot.send_message(message.from_user.id,
            f'Price of {ticker} is {share_current_price}'
            )