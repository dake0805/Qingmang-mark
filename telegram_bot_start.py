from telegram.ext import Updater, CommandHandler

from telegram_bot.command import *
from config import *
from flomo.flomo_repo import init_flomo_data
from flomo.task import flomo_monitor
from telegram_bot.tg_repo import *
from telegram_bot.feed_monitor import tg_massage_monitor


def add_tg_method():
    updater = Updater(token=token, use_context=True, request_kwargs=REQUEST_KWARGS)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("add", add))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("start", help))
    dp.add_handler(CommandHandler("flomo", flomo))
    updater.job_queue.run_repeating(tg_massage_monitor, delay)
    updater.job_queue.run_repeating(flomo_monitor, delay)

    return updater


def init_db():
    # try to create a _database if missing
    try:
        init_sqlite_data()
        init_flomo_data()
    except sqlite3.OperationalError:
        pass


if __name__ == '__main__':
    init_db()
    updater = add_tg_method()
    updater.start_polling()
    updater.idle()
    conn.close()
