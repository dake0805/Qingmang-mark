import requests

from qingmang.mark import Mark
from flomo.flomo_repo import *
from config import *
from qingmang.first import *


def add_user(flomo_api, feed_url):
    last_update_time = add_feed(feed_url)
    db_save(flomo_api, feed_url, last_update_time)


def send_to_flomo(flomo_api, mark: Mark):
    text = mark.text_flomo()
    data = {'content': text}
    r = requests.post(flomo_api, data)
