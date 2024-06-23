import asyncio
from email import message
import logging
import sys
from socketserver import DatagramRequestHandler
from metods import Ustoz
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext


from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN
from aiogram import F
from aiogram.utils.formatting import (Bold, as_list, as_marked_section, as_key_value, HashTag)


# oflain metods
from buttons import menu_buttons
from metods import sendMessage
dp = Dispatcher()


HELP_COMMANDS = """
UzGeeks faollari tomonidan tuzilgan Ustoz-Shogird kanali va tomonidan clone versiyasi yozib chiqilidi @Yuldoshev08

Bu yerda Programmalash bo`yicha
#Ustoz,  
#Shogird,
#UquvKursi,
#Sherik,  
#Xodim va #IshJoyi 
topishingiz mumkin. 

E'lon berish: @UserNmabot 
Admin @Yuldoshev08
"""


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:

    fullName = message.from_user.full_name
    user_id = message.from_user.id
    
    text = f"Assalom alaykum {fullName}\n\nUstozShogird kanalining rasmiy botiga xush kelibsiz!\n\n/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!\n
    {user_id}"
    await message.answer(
        text=text,
        reply_markup=menu_buttons,
        )
    pass

@dp.message(Command(commands='help'))
async def help_command(message:Message):
    await message.reply(HELP_COMMANDS, parse_mode='HTML')

    

# sherik kerak
@dp.message(F.text == "Sherik kerak")
async def sherk_handler(message: Message):
    await message.answer("Ism, Familiyangizni kiriting? ", reply_markup=ReplyKeyboardRemove())
    await Ustoz.name.set()
    pass

@dp.message(state=Ustoz.name)
async def name(message: type.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'name': name}
    )
    await message.answer("📚 Texnologiya:\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating. Masalan,\n\nJava, C++, C#")



# ish joyi kerak

# Hodim kerak

# Ustoz kerak

# Shogird kerak

# Uquv markaz





async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())