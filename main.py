from aiogram import Bot, Dispatcher
import asyncio

from Handlers import commands, questons
from Callbacks import pagination


async def main():
    bot = Bot(token='6814882755:AAFFPFQERNN2-xzxjg3I4mWyWU-qDloAH7E', parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(
        commands.router, 
        pagination.router,
        questons.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())