import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# ⚠️ ИЗМЕНИТЬ ТОКЕН
bot = Bot(token="")
dp = Dispatcher()


# Хэндлер на команду /start ---------------------------------------------------
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    text = "Привет, бот работает!"
    await message.answer(text, parse_mode='HTML')


# Здесь прописывается, то какую мы команду хотим сделать
@dp.message(Command("hi"))
async def cmd_start(message: types.Message):
    text = "Вау"  # то что отвечает нам бот
    await message.answer(text, parse_mode='HTML')


# Здесь прописывается, то какую мы команду хотим сделать
@dp.message(Command("while"))
async def cmd_start(message: types.Message):
    i = 0
    while i < 5:
        i += 1
        text = str(i)  # то что отвечает нам бот
        await message.answer(text, parse_mode='HTML')


# Запуск процесса поллинга новых апдейтов
async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
