from aiogram import ( Router, 
                      types,
                      F )
from src.constant import PaymentTypes
from src.kb import admin_keyboard_markup
from src.settings import config

router = Router()

@router.callback_query(F.data.in_({el.value for el in PaymentTypes}) )
async def callback_query_handler(callback_query: types.CallbackQuery):
    await callback_query.message.edit_reply_markup(reply_markup=None)
    text_msg = callback_query.message.text
    payment_type = callback_query.data.upper()
    await callback_query.bot.send_message(chat_id=config.TG_CHANEL_ADMINS_ID,
                                          text = f"{text_msg}\n\n<b>{payment_type}</b>",
                                          reply_markup=admin_keyboard_markup())
    await callback_query.answer("Спасибо!")
    
@router.callback_query(F.data.in_({'OK'}) )
async def callback_query_handler(callback_query: types.CallbackQuery):
    await callback_query.message.edit_reply_markup(reply_markup=None)
    await callback_query.answer("Спасибо!")