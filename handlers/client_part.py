from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import client_part_kb
from aiogram.types import ReplyKeyboardRemove
import keyboards.client_part_kb as nav
import requests
import json

@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет. Я market-bot). Выбери о чём ты хотел бы получить данные')
            # input_field_placeholder = "Введите тикер инструмента")
            #   reply_markup = nav.main_menu_kb_client_part)
        # await message.delete()
    except:
        await message.reply('Напишите боту в ЛС, напишите ему: \nhttps://t.me/Investment_FollowUp_bot')
        
@dp.message_handler()
async def bot_message(message : types.Message):
    #await bot.send_message(message.from_user.id, message.text)
    # if message.text == 'Акции':
    #     await bot.send_message(message.from_user.id, f'Укажите тикер акции и нажмите кнопку',
    #            reply_markup = nav.share_current_price_menu_kb_client_part)
    # elif message.text == 'Облигации':
    #     await bot.send_message(message.from_user.id, f'Укажите тикер облигации и нажмите кнопку')
    # else:
        if len(message.text) == 4:
            data = requests.get(f'https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/{message.text}.json').text
            data = json.loads(data)
            share_current_price_index = data['marketdata']['columns'].index('LCURRENTPRICE')
            data_list = data['marketdata']['data'][0]
            share_current_price = data_list[share_current_price_index]
            await bot.send_message(message.from_user.id,f'Current share price is {share_current_price}')
        else:
            data = requests.get(f'https://iss.moex.com/iss/engines/stock/markets/bonds/boards/TQOB/securities/{message.text}.json').text
            data = json.loads(data)
            bond_current_price_index = data['marketdata']['columns'].index('LCURRENTPRICE')
            data_list = data['marketdata']['data'][0]
            bond_current_price = data_list[bond_current_price_index]
            await bot.send_message(message.from_user.id,f'Current bond price is {bond_current_price}')

       
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
        
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    # dp.register_message_handler(command_shares, commands=['Акции'])
    # dp.register_message_handler(command_bonds, commands=['Облигации'])