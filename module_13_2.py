from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

API_TOKEN = '7787493433:AAGBdEiUhUvCcydfXXxFbbS_F_T_Ca5Tfbk'


bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer("Привет! Я бот помогающий твоему здоровью.")


@dp.message()
async def all_messages(message: Message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer("Введите команду /start, чтобы начать общение.")

async def main():
    print("Bot is running...")
    await bot.delete_webhook(drop_pending_updates=True)  
    await dp.start_polling(bot) 

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
