from asyncio import sleep
from src.kb import payment_types, thenks
from src.gs import message_tg_list
from aiogram import Bot
from src.settings import config
from src.text_msg import look_calendar

is_look_calendar = False

async def send_orders(bot: Bot ):
    for msg in message_tg_list:
        await bot.send_message(chat_id=config.TG_CHANEL_DELIVERIES_ID, 
                            text=msg,
                            reply_markup=payment_types)
        await sleep(2)

async def reminder_watch_calendar(bot: Bot ):
    await bot.send_message(chat_id=config.TG_CHANEL_DELIVERIES_ID, 
                        text=look_calendar,
                        reply_markup=thenks())
    await check_is_look_calendar(bot, 60)

async def check_is_look_calendar(bot: Bot, delay: int):
    await sleep(delay)
    global is_look_calendar
    if  not is_look_calendar:
        await bot.send_message(chat_id=config.TG_CHANEL_ADMINS_ID, 
                        text="ЛЖ не посмотрел календарь!\n\nБос, позвони ему, а то я готов уволить его уже 🤬"
                        )
    else:
        is_look_calendar = False