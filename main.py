import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

event_loop = asyncio.new_event_loop()
asyncio.set_event_loop(event_loop)

bot = Bot(BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage, loop=event_loop)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    from bot_handlers import dp

    asyncio.run(main())
