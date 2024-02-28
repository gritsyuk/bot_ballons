from asyncio import run as start
import logging
from aiogram import Bot, Dispatcher
from src.settings import config
from bot.handlers import router
from bot.sheduler_job import (send_list_delivery,
                              reminder_watch_calendar,
                              set_jobs)
from bot.sheduler import create_sheduler

bot = Bot(
    token=config.TG_BOT_TOKEN,
    parse_mode="HTML"
)
dp = Dispatcher()

dp.include_router(router)


async def main() -> None:
    scheduler = create_sheduler()

    scheduler.add_job(
        func=set_jobs,
        trigger="cron",
        args=(bot, scheduler),
        day_of_week='mon-sun',
        hour=21,
        minute=25
    )
    scheduler.add_job(
        func=send_list_delivery,
        trigger="cron",
        args=(bot,),
        day_of_week='mon-sun',
        # hour=00,
        # minute=49,
        second='*/30'
    )
    # scheduler.add_job(
    #                 func=reminder_watch_calendar,
    #                 trigger="cron",
    #                 args=(bot,),  
    #                 day_of_week='mon-sun',
    #                 hour=20, 
    #                 minute=00,
    #                 # replace_existing=True
    #             )

    scheduler.start()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(filename="bot_ballons.log",
                        level=logging.INFO,
                        format="%(asctime)s %(name)s %(levelname)s %(message)s",
                        )
    start(main())