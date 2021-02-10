import requests

from qingmang.mark import Mark
from repo import *
from config import *


def add_user(flomo_api, feed_url):



def send_to_flomo(flomo_api, mark: Mark):
    text = message_template_flomo % (mark.page_title, mark.page_url,
                                     mark.mark_content, mark.mark_note)
    data = {'content': text}
    r = requests.post(flomo_api, data)
