from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Скачать гайд #1")
    kb.button(text="Купить гайд #2")
    kb.button(text="Купить гайд по подготовке к фотосессиям")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)