look_calendar = "🔔 <b>Напоминание</b>\n\nПроверить по календарю доставки на сегодня и завтра"

did_not_look = "⚠️ <b>Уведомление</b>\n\nКурьер <b>Не посмотрел</b> по календарю доставки на Сегодня и Завтра или не отжал кнопку |Я посмотрел|"

def did_look_calendar(user: str = None): 
    return f"⚠️ <b>Уведомление</b>\n\nПользователь @{user} подтвердил, что посмотрел календарь заказов на доставку."