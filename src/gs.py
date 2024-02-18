import gspread
import logging
from src.utils import (
                  from_str_datatime, 
                  get_index_today, 
                  )
from model import OrderFromSheet
from typing import Iterator, Dict, List
from datetime import datetime

from settings import config

gc = gspread.service_account(
    filename=config.GOOGLE_CREDENTIALS_FILE
    )

def today_from_sheet() -> Iterator[List[OrderFromSheet]]:
    ss = gc.open_by_key(config.DB_SPREAD_SHEET_ID)
    sheet = ss.worksheet(config.DB_SHEET_NAME)
    deliveries_date_col = sheet.col_values(3)[1:]
    deliveries_date = list(map(from_str_datatime, deliveries_date_col))

    index_date = get_index_today(deliveries_date)

    data = sheet.get_all_records()
    selected_orders = [data[i] for i in index_date]

    return map(lambda el : 
                    OrderFromSheet.model_validate(el), 
                    selected_orders)

def job_msg_list(list_order) -> Iterator[Dict[datetime, str]]:
    for order in list_order:
        if not order.self_pickup:
            html = f"""Время: {order.deliver_at.strftime('%H:%M')}\nИмя: {order.client_name}\nТелефон: {order.client_phone}\nАдрес: <code>{order.adress}</code>\nИнфо: {order.comment}\nСумма: <b>{order.price_order} руб.</b>
            """
            yield dict(dt=order.deliver_at, html_msg=html)

def today_delivery_list(list_order) -> str:
    sorted_list = sorted(list_order, key=lambda r: r.deliver_at)
    res = '🔔 Доставки на сегодня:\n\n'
    for order in sorted_list:
        if not order.self_pickup:
            text = f"{order.deliver_at.strftime('%H:%M')} | <code>{order.adress}</code> | {order.comment}\n"
            res += text
    logging.info(res)
    return res