from aiogram import types, Dispatcher
from create_bot import dp, bot
import keyboards.client_part_kb as nav
from aiogram.types import ReplyKeyboardRemove
import requests
import json
from data_base import sqlite_db
from datetime import datetime

# @dp.message_handler(commands=["start", "help"])
async def command_start(message: types.Message):
    try:
        await bot.send_message(
            message.from_user.id,
            "Привет. Я market-bot). Ведите тикер акции или облигации для получения информации",
            reply_markup = ReplyKeyboardRemove()
        )

    except:
        await message.reply(
            "Напишите боту в ЛС, напишите ему: \nhttps://t.me/Investment_FollowUp_bot"
        )
    
# @dp.message_handler()
async def bot_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)

    if len(message.text) <= 6:
        ticker = message.text
        date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        data = requests.get(
            f"https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/{ticker}.json"
        ).text
        url = f'https://www.moex.com/en/issue.aspx?board=TQBR&code={ticker}'
        data = json.loads(data)
        share_current_price_index = data["marketdata"]["columns"].index("LCURRENTPRICE")
        try:
            data_list = data["marketdata"]["data"][0]
            share_current_price = data_list[share_current_price_index]
            
            await bot.send_message(
                message.from_user.id,
                f"Current share price is {share_current_price}",
                reply_markup=nav.get_additional_info(ticker,url)
            )
        except:
            await bot.send_message(
                message.from_user.id,
                f"I don't now this ticker yet, but i'm still learn) Try another one.",
            )
        
        @dp.callback_query_handler(text=f"get_add_info_about_{ticker}")
        async def get_add_info(callback: types.CallbackQuery):
            user_id = message.chat.id
            additional_share_data = requests.get(
            f"https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/{ticker}.json"
        ).text
            data = json.loads(additional_share_data)
            share_name_index = data["securities"]["columns"].index("SECNAME")
            data_list = data["securities"]["data"][0]
            share_name = data_list[share_name_index]
            share_min_price_index = data["marketdata"]["columns"].index("LOW")
            data_list = data["marketdata"]["data"][0]
            share_min_price = data_list[share_min_price_index]
            share_max_price_index = data["marketdata"]["columns"].index("HIGH")
            data_list = data["marketdata"]["data"][0]
            share_max_price = data_list[share_max_price_index]
            print(user_id)
            await bot.send_message(
                chat_id=user_id, text = f"Share name: {share_name}, Min price: {share_min_price}, Max price: {share_max_price}"
            )
            await callback.answer()

        @dp.callback_query_handler(text=f"get_link_for_{ticker}")
        async def get_add_info(callback: types.CallbackQuery):
            await callback.answer()
            
    elif message.text.startswith("SU"):
        ticker = message.text
        data = requests.get(
            f"https://iss.moex.com/iss/engines/stock/markets/bonds/boards/TQOB/securities/{ticker}.json"
        ).text
        url = f'https://www.moex.com/ru/issue.aspx?code={ticker}'
        data = json.loads(data)
        bond_current_price_index = data["marketdata"]["columns"].index("LCURRENTPRICE")
        try:
            data_list = data["marketdata"]["data"][0]
            bond_current_price = data_list[bond_current_price_index]
            await bot.send_message(
                message.from_user.id,
                f"Current bond price is {bond_current_price}",
                reply_markup=nav.get_additional_info(ticker,url)
            )
        except:
            await bot.send_message(
                message.from_user.id,
                f"I don't now this ticker yet, but i'm still learn) Try another one.",
            )

        @dp.callback_query_handler(text=f"get_add_info_about_{ticker}")
        async def get_add_info(callback: types.CallbackQuery):
            additional_bondSU_data = requests.get(
                f"https://iss.moex.com/iss/engines/stock/markets/bonds/boards/TQOB/securities/{ticker}.json"
            ).text
            
            data = json.loads(additional_bondSU_data)
            bond_name_index = data["securities"]["columns"].index("SECNAME")
            data_list = data["securities"]["data"][0]
            bond_name = data_list[bond_name_index]
            bond_min_price_index = data["marketdata"]["columns"].index("LOW")
            data_list = data["marketdata"]["data"][0]
            bond_min_price = data_list[bond_min_price_index]
            bond_max_price_index = data["marketdata"]["columns"].index("HIGH")
            data_list = data["marketdata"]["data"][0]
            bond_max_price = data_list[bond_max_price_index]
            await bot.send_message(
                message.from_user.id,
                f"Bond name: {bond_name}, Min price: {bond_min_price}, Max price: {bond_max_price}",
            )
            await callback.answer()

        @dp.callback_query_handler(text=f"get_link_for_{ticker}")
        async def get_add_info(callback: types.CallbackQuery):
            await callback.answer()

    elif message.text.startswith("RU"):
        ticker = message.text
        data = requests.get(
            f"https://iss.moex.com/iss/engines/stock/markets/bonds/boards/TQCB/securities/{ticker}.json"
        ).text
        url = f'https://www.moex.com/ru/issue.aspx?code={ticker}&board=TQCB'
        data = json.loads(data)
        ticker = message.text
        bond_current_price_index = data["marketdata"]["columns"].index("LCURRENTPRICE")
        try:
            data_list = data["marketdata"]["data"][0]
            bond_current_price = data_list[bond_current_price_index]
            await bot.send_message(
                message.from_user.id,
                f"Current bond price is {bond_current_price}",
                reply_markup=nav.get_additional_info(ticker,url)
            )
        except:
            await bot.send_message(
                message.from_user.id,
                f"I don't now this ticker yet, but i'm still learn) Try another one.",
            )


        @dp.callback_query_handler(text=f"get_add_info_about_{ticker}")
        async def get_add_info(callback: types.CallbackQuery):
            additional_bondRU_data = requests.get(
                f"https://iss.moex.com/iss/engines/stock/markets/bonds/boards/TQCB/securities/{ticker}.json"
            ).text
            data = json.loads(additional_bondRU_data)
            bond_name_index = data["securities"]["columns"].index("SECNAME")
            data_list = data["securities"]["data"][0]
            bond_name = data_list[bond_name_index]
            bond_min_price_index = data["marketdata"]["columns"].index("LOW")
            data_list = data["marketdata"]["data"][0]
            bond_min_price = data_list[bond_min_price_index]
            bond_max_price_index = data["marketdata"]["columns"].index("HIGH")
            data_list = data["marketdata"]["data"][0]
            bond_max_price = data_list[bond_max_price_index]
            await bot.send_message(
                message.from_user.id,
                f"Bond name: {bond_name}, Min price: {bond_min_price}, Max price: {bond_max_price}",
            )
            await callback.answer()
            
        @dp.callback_query_handler(text=f"get_link_for_{ticker}")
        async def get_add_info(callback: types.CallbackQuery):
            await callback.answer()

        
@dp.message_handler(commands=['Get stat from data base'])
async def get_stat_from_data_base(message : types.Message):
    await sqlite_db.sql_read(message)
    
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start", "help"])
    dp.register_message_handler(bot_message)
    dp.register_message_handler(get_stat_from_data_base, commands=['Get stat from data base'])
