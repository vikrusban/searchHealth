from os import getenv
from async_collect_data import collect_data
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    start_buttons = ['Белорецк', 'Магнитогорск', 'Челябинск']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Выбери город, в котором будем искать Эутирокс и его аналоги', reply_markup=keyboard)


@dp.message_handler(Text(equals='Белорецк'))
async def beloreck_city(message: types.Message):
    await message.answer('Поиск...')
    chat_id = message.chat.id
    await send_data(city='beloreck', chat_id=chat_id)

@dp.message_handler(Text(equals='Магнитогорск'))
async def beloreck_city(message: types.Message):
    await message.answer('Поиск...')
    chat_id = message.chat.id
    await send_data(city='magnitogorsk', chat_id=chat_id)

@dp.message_handler(Text(equals='Челябинск'))
async def beloreck_city(message: types.Message):
    await message.answer('Поиск...')
    chat_id = message.chat.id
    await send_data(city='chelyabinsk', chat_id=chat_id)

async def send_data(city='', chat_id=''):
    url = await collect_data(city=city)
    data = '''💊 Нашел свопадения, по ссылке ниже
'''+str(url)+'''     
'''
    await bot.send_message(chat_id=chat_id, text=data)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)