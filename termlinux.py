from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from subprocess import check_output


bot = Bot(token='Ваш токен')
dp = Dispatcher(bot)
user_id = 157191657

@dp.message_handler(content_types="text")
async def process_start_command(message: types.Message):
    if (user_id == message.chat.id):
        comand = message.text
        try:
         await  bot.send_message(message.chat.id, check_output(comand, shell=True))

        except:
         await  bot.send_message(message.chat.id, "Некорректная команда")



if __name__ == '__main__':

    executor.start_polling(dp)