look_calendar = "<b>Напоминание</b>\n\nПроверить по календарю доставки на сегодня и завтра"

def did_look_calendar(user: str = None): 
    return f"<b>Уведомление</b>\n\nПользователь @{user} нажал кнопку что посмотрит заказы в календаре."