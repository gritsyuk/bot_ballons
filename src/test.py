from pytz import utc
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from asyncio import run as start
from asyncio import sleep
jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
# executors = {
#     'default': ThreadPoolExecutor(20),
#     'processpool': ProcessPoolExecutor(5)
# }
# job_defaults = {
#     'coalesce': False,
#     'max_instances': 3
# }
# scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)




async def test1(text):
    print(text)


async def main() -> None:
    scheduler = AsyncIOScheduler(jobstores=jobstores)
    scheduler.add_job(
                    func=test1,
                    trigger="cron",
                    args=("dgfgh",),  
                    day_of_week='mon-sun',
                    hour=22, 
                    minute=56,
                )
    scheduler.start()


if __name__ == "__main__":
    start(main())