from aiogram import Router, F
from aiogram.types import Message
from src.keyboards.guide_locations import guide_location_kb
from pathlib import Path

path = Path("src", "img", "abramova.png")

router: Router = Router()


@router.message(F.text == "Скачать гайд #1")
async def guide_free(message: Message):
    await message.reply("Отличный выбор!")


@router.message(F.text == "Купить гайд #2")
async def guide_location(message: Message):
    await message.reply("Отличный выбор! 2")


@router.message(F.text == "Купить гайд по подготовке к фотосессиям")
async def guide_photo_session(message: Message):
    await message.reply(f'''
🦋 <b>Поборка самых красивых мест для фотосессии.</b>
Приобретя этого гида, вы узнаете самые интересные, красивые, яркие места которые подойдут для фотосесси.
Места проверенные временем и результат на фотографии не остал никого неравнодушным.
Вы посмотрите примеры из моего портфолио, узнате советы к подготовке, описанием и адреса места.
🔥 <b>И еще вы меня так поддержите, вдохновляя меня еще больше к моей любимой работе!</b>
''',
                        reply_markup=guide_location_kb()
                        )
