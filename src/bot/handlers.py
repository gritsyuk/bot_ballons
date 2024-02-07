from aiogram import ( Router, 
                      types,
                      F )
from src.constant import PaymentTypes
from src.kb import admin_keyboard_markup, thenks, button_calendar
from src.settings import config
from src.text_msg import did_look_calendar

router = Router()

@router.callback_query( F.data.in_({el.value for el in PaymentTypes}) )
async def payment_types_handler(clbk_query: types.CallbackQuery):
    await clbk_query.message.edit_reply_markup(reply_markup=None)
    text_msg = clbk_query.message.text
    payment_type = clbk_query.data.upper()
    await clbk_query.bot.send_message(chat_id=config.TG_CHANEL_ADMINS_ID,
                                          text = f"{text_msg}\n\n<b>{payment_type}</b>",
                                          reply_markup=admin_keyboard_markup())
    await clbk_query.answer("Спасибо!")
    
@router.callback_query( F.data.in_({'OK'}) )
async def ok_handler(clbk_query: types.CallbackQuery):
    await clbk_query.message.edit_reply_markup(reply_markup=None)
    await clbk_query.answer("Спасибо!")

@router.callback_query( F.data == "look_calendar" )
async def look_calendar_handler(clbk_query: types.CallbackQuery):
    await clbk_query.message.edit_reply_markup(reply_markup=button_calendar())
    username = clbk_query.from_user.username
    await clbk_query.bot.send_message(chat_id=config.TG_CHANEL_ADMINS_ID,
                                      text = did_look_calendar(username))