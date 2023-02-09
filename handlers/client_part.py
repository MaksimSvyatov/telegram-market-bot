from aiogram import types, Dispatcher
from create_bot import dp, bot

# from keyboards import client_part_kb
# from aiogram.types import ReplyKeyboardRemove
import keyboards.client_part_kb as nav
import asyncio

# import handlers.admin_part as states
import requests
import json


@dp.message_handler(commands=["start", "help"])
async def command_start(message: types.Message):
    try:
        await bot.send_message(
            message.from_user.id,
            "Привет. Я market-bot). Выберите о чём ты хотел бы получить данные"
            # , reply_markup=nav.main_menu_kb_client_part
        )
        
        # await message.delete()
    except:
        await message.reply(
            "Напишите боту в ЛС, напишите ему: \nhttps://t.me/Investment_FollowUp_bot"
        )

ticker = ''

# @dp.message_handler()
async def bot_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)
    # if message.text == "Акции":
    #     await bot.send_message(
    #         message.from_user.id,
    #         "Укажите тикер акции и нажмите кнопку"
    #         # ,
    #         # reply_markup=nav.share_current_price_menu_kb_client_part
    #     )
        # try:
    if len(message.text) == 4:
        
            # ticker = message.text
            data = requests.get(
            f"https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/{message.text}.json"
            ).text
            data = json.loads(data)
            share_current_price_index = data["marketdata"]["columns"].index("LCURRENTPRICE")
            data_list = data["marketdata"]["data"][0]
            share_current_price = data_list[share_current_price_index]
            await bot.send_message(
                message.from_user.id, f"Current share price is {share_current_price}",
                reply_markup=nav.main_menu_with_addinfo_button
            )
            print("From 4 length")
            


        # ticker = str(get())
        # ticker.close()
            
            
    
    # except:
    #     # if len(message.text) < 4 or len(message.text) > 4:
    #         await bot.send_message(message.from_user.id,
    #             'Ooops( Something goes wrong! Try another ticket, or go to "Облигации"')
    # await states.FSMClient.shares.set()
    # elif message.text == "Облигации":
    #     await bot.send_message(
    #         message.from_user.id,
    #         f"Укажите тикер облигации и нажмите кнопку",
    #         reply_markup=nav.bond_current_price_menu_kb_client_part,
    #     )
        # await states.FSMClient.bonds.set()
    elif message.text.startswith("SU"):
        data = requests.get(
            f"https://iss.moex.com/iss/engines/stock/markets/bonds/boards/TQOB/securities/{message.text}.json"
        ).text
        data = json.loads(data)
        ticker = message.text
        bond_current_price_index = data["marketdata"]["columns"].index("LCURRENTPRICE")
        data_list = data["marketdata"]["data"][0]
        bond_current_price = data_list[bond_current_price_index]
        await bot.send_message(
            message.from_user.id, f"Current bond price is {bond_current_price}",
            reply_markup=nav.main_menu_with_addinfo_button
        )
        print("From SU")
        
    elif message.text.startswith("RU"):
        data = requests.get(
            f"https://iss.moex.com/iss/engines/stock/markets/bonds/boards/TQCB/securities/{message.text}.json"
        ).text
        data = json.loads(data)
        ticker = message.text
        bond_current_price_index = data["marketdata"]["columns"].index("LCURRENTPRICE")
        data_list = data["marketdata"]["data"][0]
        bond_current_price = data_list[bond_current_price_index]
        await bot.send_message(
            message.from_user.id, f"Current bond price is {bond_current_price}",
            reply_markup=nav.main_menu_with_addinfo_button
        )
        print("From RU")
@dp.callback_query_handler(text='get_add_info')
async def get_add_info(callback : types.CallbackQuery):
                await callback.answer('Addinfo pressed')   

        # data = requests.get(
        #     f"https://iss.moex.com/iss/engines/stock/markets/bonds/boards/TQCB/securities/{message.text}.json"
        # ).text
        # data = json.loads(data)
        # bond_current_price_index = data["marketdata"]["columns"].index("LCURRENTPRICE")
        # data_list = data["marketdata"]["data"][0]
        # bond_current_price = data_list[bond_current_price_index]
        # await bot.send_message(
        #     message.from_user.id, f"Current bond price is {bond_current_price}",
        #     reply_markup=nav.main_menu_with_addinfo_button
        # )
    # if message.text == "Главное меню":
    #     await bot.send_message(
    #         message.from_user.id,
    #         "Выберите о чём бы Вы хотели получить данные",
    #         # input_field_placeholder = "Введите тикер инструмента",
    #         reply_markup=nav.main_menu_kb_client_part
    #     )


# @dp.message_handler(commands=['Акции'])
# async def command_shares(message : types.Message):
#     client_share_current_price = get_share_info_trough_ticker()
#     try:
#         # await bot.send_message(message.from_user.id, 'Укажи тикер акции заглавными буквами', reply_markup=kb_client_part)

#         # запрос определённого тикера

#         # client_share_current_price = get_share_info_trough_ticker()
#         await bot.send_message(message.from_user.id, f'Current price is {price}', reply_markup=kb_client_part)

#         # клавиатура останется на месте
#         await message.delete()
#     except:
#         await message.reply('Напишите боту в ЛС, напишите ему: \nhttps://t.me/Investment_FollowUp_bot')

# @dp.message_handler(commands=['Облигации'])
# async def command_bonds(message : types.Message):
#     try:
#         await bot.send_message(message.from_user.id, 'Укажи тикер облигации заглавными буквами')#, reply_markup=ReplyKeyboardRemove())
#         # клавиатура после срабатывания хэндлера удалится безвозвратно
#         await message.delete()
#     except:
#         await message.reply('Напишите боту в ЛС, напишите ему: \nhttps://t.me/Investment_FollowUp_bot')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start", "help"])
    dp.register_message_handler(bot_message)
    # dp.register_message_handler(command_shares, commands=['Акции'])
    # dp.register_message_handler(command_bonds, commands=['Облигации'])
