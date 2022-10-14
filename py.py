from aiogram import Bot,executor,Dispatcher,types
from aiogram.dispatcher import FSMContext
import requests
from bs4 import BeautifulSoup
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '5557676933:AAFl9LpMWkhkrj1RQuRJ8bM21Cxq8zhqCcM'
bot = Bot(TOKEN)
class Botik(StatesGroup):
    pars = State()
    pars2 = State()
dp = Dispatcher(bot,storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def main(message: types.Message):
    await message.answer('Введите url')
    await Botik.pars.set()

@dp.message_handler(state=Botik.pars)
async def on(message: types.Message, state: FSMContext):
    text = message.text
    p = requests.get(text)
    t = BeautifulSoup(p.text)
    u = t.find('strong',class_='jsl10n localized-slogan')
    await message.answer(u.text)

#@dp.message_handler(state=Botik.pars2)
#async def off(message: types.Message, state: FSMContext):
if __name__ == '__main__':
    executor.start_polling(skip_updates=True,dispatcher=dp)