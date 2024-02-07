from asyncio import sleep
from src.kb import payment_types, thenks
from src.gs import message_tg_list
from aiogram import Bot
from src.settings import config
from src.text_msg import look_calendar


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
        