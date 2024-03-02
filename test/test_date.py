from datetime import datetime, timedelta
import pytz


async def curet_time():
    tz = pytz.timezone('Europe/Moscow')
    current_date = datetime.now(tz=tz)

    start_dt = datetime(year=current_date.year,
                        month=current_date.month,
                        day=current_date.day,
                        hour=5,
                        minute=0)

    end_dt = start_dt + timedelta(hours=20)

    print(current_date)
    # print(end_dt)


def test_split():
    test_msg = """🎈 НОВАЯ ДОСТАВКА СЕГОДНЯ:

    11:00 | Грайвороновская улица 8К2 |"""
    msg_body = test_msg.split('\n')[2].strip()
    time, adress, info = msg_body.split('|')
    print(time, adress, info)


test_split()
