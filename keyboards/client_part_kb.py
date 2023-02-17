from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_additional_info(ticker):
    kb_addinfo_button = InlineKeyboardMarkup(row_width=1)
    additional_info_button = InlineKeyboardButton(text="Получить дополнительную информацию",
                                                callback_data=f"get_add_info_about_{ticker}")
    kb_addinfo_button.add(additional_info_button)
    return kb_addinfo_button