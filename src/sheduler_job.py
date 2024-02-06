from asyncio import sleep
from src.kb import payment_types
from src.gs import message_tg_list
from aiogram import Bot
from src.settings import config


async def send_orders(bot: Bot ):
    for msg in message_tg_list:
        await bot.send_message(chat_id=config.TG_CHANEL_DELIVERIES_ID, 
                            text=msg,
                            reply_markup=payment_types)
        await sleep(1)