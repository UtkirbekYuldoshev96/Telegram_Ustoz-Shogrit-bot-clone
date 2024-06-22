import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN
from aiogram import F
from buttons import menu_buttons

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
async def command_start_handler(message: Message) -> None:
    fullName = message.from_user.full_name
    text = f"Assalom alaykum {fullName}\n\nUstozShogird kanalining rasmiy botiga xush kelibsiz!\n\n/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!"
    await message.answer(
        text=text,
        reply_markup=menu_buttons,
        )
    pass


@dp.message(Command(commands='help'))
async def help_command(message:Message):
    await message.reply(HELP_COMMANDS, parse_mode='HTML')

    

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())