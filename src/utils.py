from datetime import datetime
from time import time
from typing import List

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
    now = datetime.now()

    start_of_day = datetime(now.year, now.month, now.day, 6, 0)
    end_of_day = datetime(now.year, now.month, now.day + 1, 0, 59)

    indexes_in_range = [i for i, dt in enumerate(date_list) if start_of_day <= dt <= end_of_day]

    return indexes_in_range

def timing_decorator(func: object):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {execution_time} секунд")
        return result
    return wrapper