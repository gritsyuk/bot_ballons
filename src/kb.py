from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.constant import PaymentTypes
from src.settings import config

buttons = [[InlineKeyboardButton(text=PaymentTypes.TRANSFER.value, callback_data=PaymentTypes.TRANSFER)],
           [InlineKeyboardButton(text=PaymentTypes.TERMINAL.value, callback_data=PaymentTypes.TERMINAL)],
           [InlineKeyboardButton(text=PaymentTypes.CASH.value, callback_data=PaymentTypes.CASH)],
           [InlineKeyboardButton(text=PaymentTypes.QR_CODE.value, callback_data=PaymentTypes.QR_CODE)],
           [InlineKeyboardButton(text=PaymentTypes.PAID.value, callback_data=PaymentTypes.PAID)]]
           
payment_types = InlineKeyboardMarkup(inline_keyboard=buttons)

def admin_keyboard_markup() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="👌", callback_data="OK")
        ]
    ]

    keyboard_markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard_markup

def thenks() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="Я посмотрел", 
                                 callback_data="look_calendar"
                                 )
        ]
    ]

    keyboard_markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard_markup

def button_calendar() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="📅 Открыть ", 
                                 url=config.GG_CALENDAR_URL
                                 )
        ]
    ]

    keyboard_markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard_markup