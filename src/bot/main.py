from asyncio import run as start
import logging
from aiogram import Bot, Dispatcher
from src.settings import config
from src.bot.handlers import router
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from src.bot.sheduler_job import send_orders, reminder_watch_calendar, set_jobs


bot = Bot(
    token=config.TG_BOT_TOKEN, 
    parse_mode="HTML"
    )
dp = Dispatcher()

dp.include_router(router)

scheduler = AsyncIOScheduler()

async def main() -> None:
    scheduler.add_job(
                    func=set_jobs,
                    trigger="cron",
                    args=(bot, scheduler),  
                    day_of_week='mon-sun',
                    hour=5, 
                    minute=00,
                )
    # scheduler.add_job(
    #                     func=send_orders,
    #                     trigger="cron",
    #                     args=(bot,),  
    #                     day_of_week='mon-sun',
    #                     hour=5, 
    #                     minute=00,
    #                 )
    scheduler.add_job(
                    func=reminder_watch_calendar,
                    trigger="cron",
                    args=(bot,),  
                    day_of_week='mon-sun',
                    hour=20, 
                    minute=00,
                )
    scheduler.start()


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(filename="/var/log/bot_ballons.log", 
                        level=logging.INFO,
                        format="%(asctime)s %(name)s %(levelname)s %(message)s",
                       )
    start(main())

