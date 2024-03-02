import logging

from aiogram import (Router,
                     types,
                     F)
from src.bot.constant import PaymentTypes
from src.bot.kb import (admin_keyboard_markup,
                        button_calendar)
from src.bot.text_msg import did_look_calendar
from src.settings import config
import re
from src.sheduler.sheduler_job import set_jobs
from apscheduler.schedulers.asyncio import AsyncIOScheduler

router = Router()


@router.callback_query(F.data.in_({el.value for el in PaymentTypes}))
async def payment_types_handler(clbk_query: types.CallbackQuery):
    await clbk_query.message.edit_reply_markup(reply_markup=None)
    text_msg = clbk_query.message.text
    payment_type = clbk_query.data.upper()
    await clbk_query.bot.send_message(chat_id=config.TG_CHANEL_ADMINS_ID,
                                      text=f"{text_msg}\n\n<b>{payment_type}</b>",
                                      reply_markup=admin_keyboard_markup())
    await clbk_query.answer("Спасибо!")


@router.callback_query(F.data.in_({'OK'}))
async def ok_handler(clbk_query: types.CallbackQuery):
    await clbk_query.message.edit_reply_markup(reply_markup=None)
    await clbk_query.answer("Спасибо!")


@router.callback_query(F.data == "look_calendar")
async def look_calendar_handler(clbk_query: types.CallbackQuery):
    await clbk_query.message.edit_reply_markup(reply_markup=button_calendar())
    config.IS_LOOK_CALENDAR = True
    username = clbk_query.from_user.username
    await clbk_query.bot.send_message(chat_id=config.TG_CHANEL_ADMINS_ID,
                                      text=did_look_calendar(username))


@router.channel_post(F.text.contains("НОВАЯ ДОСТАВКА"))
async def new_delivery_handler(message: types.Message, scheduler: AsyncIOScheduler):
    string = message.text.split('\n')[0]
    match = re.search(r'(\d+)', string)
    if match:
        row = match.group(1)
        await set_jobs(message.bot, scheduler, row)
