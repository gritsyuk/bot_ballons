from aiogram import Bot, Dispatcher
import asyncio
from src.settings import config
from src.bot.handlers import router
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from src.sheduler_job import send_orders, reminder_watch_calendar


bot = Bot(
    token=config.TG_BOT_TOKEN, 
    parse_mode="HTML"
    )
dp = Dispatcher()

dp.include_router(router)

scheduler = AsyncIOScheduler()

async def main() -> None:
    
    scheduler.add_job(
                        func=send_orders,
                        trigger="cron",
                        args=(bot,),  
                        day_of_week='mon-sun',
                        hour=6, 
                        minute=00,
                    )
    scheduler.add_job(
                    func=reminder_watch_calendar,
                    trigger="cron",
                    args=(bot,),  
                    day_of_week='mon-sun',
                    minute='*/5',
                )
    scheduler.start()


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

