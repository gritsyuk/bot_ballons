import logging
from src.settings import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from asyncio import sleep
from src.bot.kb import payment_types, thenks
from src.bot import text_msg
from aiogram import Bot
from src.gs import google_client


async def send_list_delivery(bot: Bot):
    list_delivery = await google_client.get_today_orders()
    logging.info(list_delivery)
    msg = text_msg.today_delivery_list(list_delivery)
    logging.info(msg)
    await bot.send_message(chat_id=config.TG_CHANEL_DELIVERIES_ID,
                           text=msg,
                           reply_markup=None)


async def send_delivery(bot: Bot, html_msg):
    await bot.send_message(chat_id=config.TG_CHANEL_DELIVERIES_ID,
                           text=html_msg,
                           reply_markup=payment_types)


async def reminder_watch_calendar(bot: Bot):
    await bot.send_message(chat_id=config.TG_CHANEL_DELIVERIES_ID,
                           text=text_msg.look_calendar,
                           reply_markup=thenks())
    await check_is_look_calendar(bot, config.MINUTES_TO_CHEK_COURIER)


async def check_is_look_calendar(bot: Bot, delay: int):
    await sleep(delay * 60)
    if config.IS_LOOK_CALENDAR:
        config.IS_LOOK_CALENDAR = False
    else:
        await bot.send_message(chat_id=config.TG_CHANEL_ADMINS_ID,
                               text=text_msg.did_not_look
                               )


async def set_jobs(bot: Bot, scheduler: AsyncIOScheduler, row: str = None):
    if row is None:
        list_delivery = await google_client.get_today_orders()
    else:
        list_delivery = await google_client.get_order_by_row(row)
    logging.info(f"set_jobs->list_delivery-{list_delivery}")
    jobs_msg = text_msg.job_msg_list(list_delivery)
    logging.info(f"jobs_msg-{jobs_msg}")
    for job in jobs_msg:
        try:
            scheduler.add_job(
                func=send_delivery,
                trigger='date',
                run_date=job.get("dt"),
                args=[bot, job.get("html_msg")],
                replace_existing=False)
        except Exception as e:
            await bot.send_message(chat_id=config.TG_CHANEL_ADMINS_ID,
                                   text=str(e))
