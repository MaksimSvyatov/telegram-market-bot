from aiogram import types
from create_bot import dp, bot
import time
import requests
import json
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from create_bot import dp, bot
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text


tickers_list = []

class FSMAdmin(StatesGroup):
    tickers_names = State()
    periodicity = State()
    time = State()
    
# Начало диалога загрузки нового, например, пункта меню
@dp.message_handler(commands='dailyinfo', state=None)
async def make_changes_command(message : types.Message):
    global ID
    ID = message.from_user.id
    await FSMAdmin.tickers_names.set()
    await message.reply('If you want to get daily info about prices, enter tickers with ,')

# Ловим первый ответ
@dp.message_handler(state = FSMAdmin.tickers_names)
async def load_tickers_names(message : types.Message, state: FSMContext):
        print(message.text, 'message.text')
        async with state.proxy() as data:
            data['tickers_names'] = message.text
        await FSMAdmin.next()
        await message.reply('Сколько раз в день?')# если дальше есть какие-то пунткы.
        #Этой строкой переводим бота в ожидание ответ на на следующее состояние 
        # идёт по порядку class FSMAdmin(StatesGroup), ждёт следующее состояние


# Ловим второй ответ
@dp.message_handler(state = FSMAdmin.periodicity)
async def load_tickers_names(message : types.Message, state: FSMContext):
        print(message.text, 'message.text')
        async with state.proxy() as data:
            data['periodicity'] = message.text
        await FSMAdmin.next()
        await message.reply('В какое время?')# если дальше есть какие-то пунткы.
        #Этой строкой переводим бота в ожидание ответна на следующее состояние 
        # идёт по порядку class FSMAdmin(StatesGroup), ждёт следующее состояние

# Ловим второй ответ
@dp.message_handler(state = FSMAdmin.time)
async def load_tickers_names(message : types.Message, state: FSMContext):
        print(message.text, 'message.text')
        async with state.proxy() as data:
            data['time'] = message.text
        await state.finish()

# Ловим первый ответ админа
# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message : types.Message, state : FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await state.finish() # эта строка для последнего состояния, бот выходит из машины состояний и всё очищается
    
# Выход из машины состояний
# @dp.message_handler(state='*', commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
# async def cancel_handler(message : types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#     await state.finish()
#     await message.reply('Ok')
    

async def get_daily_info(message: types.Message):
    for i in range(2):    
        for ticker in tickers_list:
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
    
    # Регистрация хэндлерова
def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(make_changes_command, commands=['dailyinfo'])
    dp.register_message_handler(load_tickers_names, state=None)
    # dp.register_message_handler(load_name, commands=['Введи название'], state=FSMAdmin.photo)
    dp.register_message_handler(load_photo, commands=['Загрузить фото'], state=None)
    # dp.register_message_handler(cancel_handler, state='*', commands='отмена')
    # dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*') 
