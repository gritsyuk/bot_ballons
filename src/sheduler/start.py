from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from src.sheduler.sheduler_job import send_list_delivery, set_jobs, reminder_watch_calendar
from aiogram import Bot


def create_sheduler() -> AsyncIOScheduler():
    # jobstores = {
    # 'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
    # }
    executors = {
        'default': ThreadPoolExecutor(20),
        'processpool': ProcessPoolExecutor(5)
    }
    # job_defaults = {
    #     'coalesce': False,
    #     'max_instances': 3
    # }
    # scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
    return AsyncIOScheduler()


def start_scheduler(scheduler: AsyncIOScheduler, bot: Bot):
    scheduler.add_job(
        func=set_jobs,
        trigger="cron",
        args=(bot, scheduler),
        day_of_week='mon-sun',
        hour=5,
        minute=1
    )
    scheduler.add_job(
        func=send_list_delivery,
        trigger="cron",
        args=(bot,),
        day_of_week='mon-sun',
        hour=5,
        minute=0,
        # second='*/30'
    )
    scheduler.add_job(
        func=reminder_watch_calendar,
        trigger="cron",
        args=(bot,),
        day_of_week='mon-sun',
        hour=20,
        minute=00,
        # replace_existing=True
    )

    scheduler.start()

    return scheduler
