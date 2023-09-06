from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from src.keyboards.main_page import main_kb

router: Router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f'''
😎 Привет, я бот фотографа <b>Елены Абрамовой!</b> 
<u>С моей помощью вы можете:</u>
<b>Кнопка 1.</b> Скачать гайд #1 по локациям <u>(free)</u>
<b>Кнопка 2.</b> Купить гайд #2 по локациям
<b>Кнопка 3.</b> Купить гайд по подготовке к фотосессиям
''',
        reply_markup=main_kb()
    )
