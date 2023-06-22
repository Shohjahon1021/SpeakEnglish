"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from aiogram import Bot, Dispatcher, executor, types

from googletrans import Translator

translator = Translator()


API_TOKEN = '6182386256:AAG5c10WsGR7w-0bzao6JD6S1P2tzhZaBNY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Speakinglish botga xush kelibsiz")
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Botni ishga tushurish uchun helpni bosing")



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    lang = translator.detect(message.text).lang
    dest = 'uz' if lang == 'en' else 'uz'
    await message.answer(translator.translate(message.text, dest).text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)