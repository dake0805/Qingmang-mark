import os
from telegram.ext import Updater, CommandHandler

from config import *
from command import *
from telegram_bot.feed_monitor import rss_monitor
from repo import *


def add_tg_method():
    updater = Updater(token=token, use_context=True, request_kwargs=REQUEST_KWARGS)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("add", add))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("start", help))

    updater.job_queue.run_repeating(rss_monitor, delay)

    return updater


def init_db():
    # try to create a _database if missing
    try:
        init_sqlite_data()
    except sqlite3.OperationalError:
        pass


if __name__ == '__main__':
    init_db()
    updater = add_tg_method()
    updater.start_polling()
    updater.idle()
    conn.close()
