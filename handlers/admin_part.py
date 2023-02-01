# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram import types
# from create_bot import dp, bot
# from aiogram.dispatcher import Dispatcher
# from aiogram.dispatcher.filters import Text

# ID = None

# class FSMAdmin(StatesGroup):
#     name = State()
#     photo = State()
    
# # @dp.message_handler(commands=['moderator'], is_chat_admin=True)
# async def make_changes_command(message : types.Message):
#     global ID
#     ID = message.from_user.id
#     await bot.send_message(message.from_user.id, 'Что, хозяин, нужно???')
#     await message.delete() 
    
# # Начало диалога загрузки нового, например, пункта меню
# @dp.message_handler(commands='Загрузить', state=None)
# async def cm_start(message : types.Message):
#     await FSMAdmin.name.set()
#     await message.reply('Введи название')

# # Ловим второй ответ админа
# # @dp.message_handler(content_types=['name'], state=FSMAdmin.name)
# async def load_name(message : types.Message, state : FSMContext):
#     if message.from_user.id == ID:
#         async with state.proxy() as data:
#             data['name'] = message.text
#         await FSMAdmin.next()
#         await message.reply('Загрузи фото')# если дальше есть какие-то пунткы.
#         #Этой строкой переводим бота в ожидание ответна на следующее состояние 
#         # идёт по порядку class FSMAdmin(StatesGroup), ждёт следующее состояние

# # Ловим первый ответ админа
# # @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
# async def load_photo(message : types.Message, state : FSMContext):
#     if message.from_user.id == ID:
#         async with state.proxy() as data:
#             data['photo'] = message.photo[0].file_id
#         await FSMAdmin.next()
#         # await message.reply('Теперь введи название')

#         # await message.reply('Теперь введи название')
#         await state.finish() # эта строка для последнего состояния, бот выходит из машины состояний и всё очищается
    
# # Выход из машины состояний
# # @dp.message_handler(state='*', commands='отмена')
# # @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
# async def cancel_handler(message : types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#     await state.finish()
#     await message.reply('Ok')
    
#     # Регистрация хэндлерова
# def register_handlers_admin(dp : Dispatcher):
#     dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
#     dp.register_message_handler(load_name, commands=['Введи название'], state=FSMAdmin.photo)
#     dp.register_message_handler(load_photo, commands=['Загрузить фото'], state=None)
#     dp.register_message_handler(cancel_handler, state='*', commands='отмена')
#     dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*') 
