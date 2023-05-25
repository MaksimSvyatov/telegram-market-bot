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
from data_base import sqlite_db
import keyboards.client_part_kb as nav

tickers_list = []

class FSMAdmin(StatesGroup):
    tickers_names = State()
    periodicity = State()
    time = State()
 
# Начало диалога загрузки нового, например, пункта меню
@dp.message_handler(commands=['dailyinfo'])
async def make_changes_command(message : types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'What do you want?', reply_markup=nav.kb_daily_info)
    
# Начало диалога
@dp.message_handler(commands='Допинфа', state=None)
async def cm_start(message : types.Message):
    await FSMAdmin.tickers_names.set()
    await message.reply('Write tickers with ,')

# Ловим первый ответ
@dp.message_handler(state = FSMAdmin.tickers_names)
async def load_tickers_names(message : types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['tickers_names'] = message.text
        await FSMAdmin.next()
        await message.reply('Сколько раз в день?')# если дальше есть какие-то пунткы.
        #Этой строкой переводим бота в ожидание ответ на на следующее состояние 
        # идёт по порядку class FSMAdmin(StatesGroup), ждёт следующее состояние

# Ловим второй ответ
@dp.message_handler(state = FSMAdmin.periodicity)
async def load_tickers_names(message : types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['periodicity'] = message.text
        await FSMAdmin.next()
        await message.reply('В какое время?')# если дальше есть какие-то пунткы.
        #Этой строкой переводим бота в ожидание ответна на следующее состояние 
        # идёт по порядку class FSMAdmin(StatesGroup), ждёт следующее состояние

# Ловим второй ответ
@dp.message_handler(state = FSMAdmin.time)
async def load_tickers_names(message : types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['time'] = message.text
            data['id'] = message.from_user.id

        await sqlite_db.sql_add_command(state)
        await message.reply('Всё успешно записано)')
        await state.finish()

    # Регистрация хэндлерова
def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(make_changes_command, commands=['dailyinfo'])
    dp.register_message_handler(cm_start, commands=['Допинфа'], state=None)
    dp.register_message_handler(load_tickers_names, state=None)