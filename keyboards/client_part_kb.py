from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_additional_info(ticker, url):
    kb_addinfo_button = InlineKeyboardMarkup(row_width=1)
    additional_info_button = InlineKeyboardButton(text="Дополнительная информация",
                                                callback_data=f"get_add_info_about_{ticker}")
    link_button = InlineKeyboardButton(text="Перейти на страницу актива",
                                                callback_data=f"get_link_for_{ticker}",
                                                url = url)
    kb_addinfo_button.add(additional_info_button).add(link_button)
    return kb_addinfo_button

button_daily_info = KeyboardButton('/Допинфа')
kb_daily_info = ReplyKeyboardMarkup(resize_keyboard=True).add(button_daily_info)