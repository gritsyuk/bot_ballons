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