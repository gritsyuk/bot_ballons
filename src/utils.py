from datetime import datetime, timedelta
import pytz
from time import time
from typing import Iterator, Dict, List
import logging


def parse_date(x):
    try:
        return datetime.strptime(x, "%d.%m.%Y %H:%M:%S")
    except ValueError:
        return None


def from_str_datatime(el: str):
    """Faster then strptime"""
    try:
        date_time = el.split(' ')
        day_s, mon_s, year_s = date_time[0].split('.')
        h, m, s = date_time[1].split(':')
        return datetime(int(year_s),
                        int(mon_s),
                        int(day_s),
                        int(h),
                        int(m),
                        int(s))
    except ValueError:
        return None


def get_index_today(date_list: List[datetime]) -> List[int]:
    tz = pytz.timezone('Europe/Moscow')
    current_date = datetime.now(tz=tz)
    # current_date = datetime(2024, 1, 2, tzinfo=tz)
    logging.info(current_date)
    start_dt = datetime(year=current_date.year,
                        month=current_date.month,
                        day=current_date.day,
                        hour=5,
                        minute=0)

    end_dt = start_dt + timedelta(hours=20)

    indexes_in_range = [i for i, dt in enumerate(date_list) if dt is not None and start_dt <= dt <= end_dt]
    logging.info(indexes_in_range)
    return indexes_in_range


def timing_decorator(func: object):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        execution_time = end_time - start_time
        print(f'Время выполнения функции {func.__name__}: {execution_time} секунд')
        return result

    return wrapper
