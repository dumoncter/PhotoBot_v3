from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def guide_location_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Купить гайд #2")
    kb.button(text="На главную")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)