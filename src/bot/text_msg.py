import logging
from typing import Iterator, Dict
from datetime import datetime

look_calendar = "🔔 <b>Напоминание</b>\n\nПроверить по календарю доставки на сегодня и завтра"

did_not_look = ("⚠️ <b>Уведомление</b>\n\nКурьер <b>Не посмотрел</b> по календарю доставки на Сегодня и Завтра или не "
                "отжал кнопку |Я посмотрел|")


def did_look_calendar(user: str = None):
    return f"🔔 <b>Уведомление</b>\n\nПользователь @{user} подтвердил, что посмотрел календарь заказов на доставку."


def today_delivery_list(list_order) -> str:
    sorted_list = sorted(list_order, key=lambda r: r.deliver_at)
    logging.info(f"Sorted_list: {sorted_list}")
    res = '🔔 Доставки на сегодня:\n\n'
    for order in sorted_list:
        if not order.self_pickup:
            text = f"{order.deliver_at.strftime('%H:%M')} | <code>{order.adress}</code> | {order.comment}\n"
            res += text
    logging.info(res)

    return res


def job_msg_list(list_order) -> Iterator[Dict[datetime, str]]:
    for order in list_order:
        if not order.self_pickup:
            html = f"""Время: {order.deliver_at.strftime('%H:%M')}\nИмя: {order.client_name}\nТелефон: {order.client_phone}\nАдрес: <code>{order.adress}</code>\nИнфо: {order.comment}\nСумма: <b>{order.price_order} руб.</b>
            """
            yield dict(dt=order.deliver_at, html_msg=html)
