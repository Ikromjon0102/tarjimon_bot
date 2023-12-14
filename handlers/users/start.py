from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

from googletrans import Translator
tarj = Translator()

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    await message.answer(f"Salom, {message.from_user.full_name}!")


@dp.message_handler()
async def tarjimon(message: types.Message):
    xabar = message.text
    tarj_matn = tarj.translate(xabar, dest='en').text

    await message.answer(tarj_matn)

