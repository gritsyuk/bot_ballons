from asyncio import sleep
from src.bot.kb import payment_types, thenks
from src.gs import message_tg_list
from aiogram import Bot
from src.settings import config
from src.bot import text_msg


async def send_orders(bot: Bot ):
    for msg in message_tg_list:
        await bot.send_message(chat_id=config.TG_CHANEL_DELIVERIES_ID, 
                            text=msg,
                            reply_markup=payment_types)
        await sleep(2)

async def reminder_watch_calendar(bot: Bot ):
    await bot.send_message(chat_id=config.TG_CHANEL_DELIVERIES_ID, 
                        text=text_msg.look_calendar,
                        reply_markup=thenks())
    await check_is_look_calendar(bot, config.MINUTES_TO_CHEK_COURIER)

async def check_is_look_calendar(bot: Bot, delay: int):
    await sleep(delay * 60)
    if  config.IS_LOOK_CALENDAR:
        config.IS_LOOK_CALENDAR = False
    else:
        await bot.send_message(chat_id=config.TG_CHANEL_ADMINS_ID, 
                text=text_msg.did_not_look
                )