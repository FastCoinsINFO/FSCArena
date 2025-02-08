import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.utils import executor

TOKEN = 7857745838:AAGBO9i_UEG27uogJYmuMFtiWKi-sN2WRhM

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Кнопка для запуска игры
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("🎮 Играть", web_app=WebAppInfo(url=https://github.com/FastCoinsINFO/FSCArena/blob/main/game.html)))

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("🔥 Добро пожаловать в FSC Token Arena! 🔥\nВыберите 'Играть', чтобы начать сражение!", reply_markup=keyboard)

if name == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)