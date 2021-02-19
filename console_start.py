from flomo.flomo import init_flomo, add_user, sync_all_user
from utils import logger
import schedule
from config import *


# CLI界面下，给一个人使用，而不使用 Telegram BOT，需要在 config 设置相关信息。


def flomo_task_init():
    try:
        init_flomo()
        add_user(FLOMO_API, QINGMANG_RSS_API)
    except Exception:
        logger.info("exception @flomo_task_init, it's ok, maybe you have used the program before.")


def flomo_task():
    logger.info("sync to flomo start")
    sync_all_user()
    logger.info("sync finish")


if __name__ == '__main__':
    if FLOMO_ON:
        flomo_task_init()
        schedule.every(delay).seconds.do(flomo_task)

    # start block
    while True:
        schedule.run_pending()
