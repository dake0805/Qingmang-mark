import requests

from flomo.flomo_repo import *
from qingmang.feed import update_feed
from qingmang.first import *
from qingmang.mark import Mark
from utils import logger


# 尝试初始化数据库


def init_flomo():
    try:
        init_flomo_data()
    except sqlite3.OperationalError:
        pass


# 数据库添加新用户
def add_user(flomo_api, feed_url):
    if flomo_api.startswith('https://flomoapp.com/iwh/'):
        last_update_time = add_feed(feed_url)
        db_save(flomo_api, feed_url, last_update_time)
    else:
        logger.warn("wrong flomo api @add_user")
        raise Exception("wrong flomo api.")


# 已查询到的一条马克发送到 FLOMO
def send_to_flomo(flomo_api, mark: Mark):
    text = mark.text_flomo()
    data = {'content': text}
    r = requests.post(flomo_api, data)


# 执行一次同步任务
def sync_all_user():
    users = db_load_flomo_users()
    for u in users:
        old_update_time = u.last_update_time
        marks, new_update_time = update_feed(u.feed_url, old_update_time)

        if (marks is None) | (new_update_time is None):
            # no updates
            return

        db_update_feed(u.flomo_api, new_update_time)
        for mark in marks:
            send_to_flomo(u.flomo_api, mark)
