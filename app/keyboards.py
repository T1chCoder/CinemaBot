from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Каталог")],
    [KeyboardButton(text="Корзина"), KeyboardButton(text="Контакты")]
], resize_keyboard=True, input_field_placeholder="Выберите пункт меню")

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Youtube", callback_data="btn_youtube")]
])