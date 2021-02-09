import os
from telegram.ext import Updater, CommandHandler

from config import *
from command_handler import *
from feed_monitor import rss_monitor
from repo import *


def set_proxy():
    os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"
    os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"


def add_tg_method():
    updater = Updater(token=token, use_context=True)
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
    rss_mem_flash()


if __name__ == '__main__':
    set_proxy()
    init_db()
    updater = add_tg_method()
    updater.start_polling()
    updater.idle()
    conn.close()
