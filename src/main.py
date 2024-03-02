from asyncio import run as start
import logging
from aiogram import Bot, Dispatcher
from src.settings import config
from bot.handlers import router
from src.sheduler.start import create_sheduler, start_scheduler
from src.bot.middlewares import SchedulerMiddleware

bot = Bot(
    token=config.TG_BOT_TOKEN,
    parse_mode="HTML"
)
scheduler = create_sheduler()
dp = Dispatcher()
dp.update.middleware.register(SchedulerMiddleware(scheduler))
dp.include_router(router)


async def main() -> None:
    start_scheduler(scheduler, bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(filename="../log/bot_ballons.log",
                        level=logging.INFO,
                        format="%(asctime)s %(name)s %(levelname)s %(message)s",
                        )
    start(main())
