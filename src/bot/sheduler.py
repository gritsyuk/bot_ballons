from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


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