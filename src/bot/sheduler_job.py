from asyncio import sleep
from src.bot.kb import payment_types, thenks
from src.gs import (
                    today_from_sheet,
                    today_delivery_list, 
                    job_msg_list)
from aiogram import Bot
from src.settings import config
from src.bot import text_msg
from apscheduler.schedulers.asyncio import AsyncIOScheduler


async def send_list_delivery(bot: Bot):
    list_delivery = today_from_sheet()
    await bot.send_message(chat_id=config.TG_CHANEL_DELIVERIES_ID, 
                        text=today_delivery_list(list_delivery),
                        reply_markup=None)

async def send_delivery(bot: Bot, html_msg):
    await bot.send_message(chat_id=config.TG_CHANEL_DELIVERIES_ID, 
                        text=html_msg,
                        reply_markup=payment_types)

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

async def set_jobs(bot: Bot, scheduler: AsyncIOScheduler):
    list_delivery = today_from_sheet()
    jobs_msg = job_msg_list(list_delivery)
    for job in jobs_msg:
        scheduler.add_job(
                        func=send_delivery,
                        trigger='date',
                        run_date=job.get("dt"), 
                        args=[bot, job.get("html_msg")],
                        replace_existing=True)