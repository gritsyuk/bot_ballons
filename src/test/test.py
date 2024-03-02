from apscheduler.schedulers.asyncio import AsyncIOScheduler

from asyncio import run as start
from asyncio import sleep
# jobstores = {
#     'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
# }
# executors = {
#     'default': ThreadPoolExecutor(20),
#     'processpool': ProcessPoolExecutor(5)
# }
# job_defaults = {
#     'coalesce': False,
#     'max_instances': 3
# }
# scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)

from src.gs import today_delivery_list


async def test1(text):
    print(text)


deliveries_date = list(map(from_str_datatime, deliveries_date_col))


async def main() -> None:
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        func=today_delivery_list,
        trigger="cron",
        args=(deliveries_date(),),
        day_of_week='mon-sun',
        second='*/10',
    )
    scheduler.start()
    await sleep(180)


if __name__ == "__main__":
    start(main())
