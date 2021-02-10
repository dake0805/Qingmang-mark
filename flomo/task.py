from flomo.flomo import *
from qingmang.feed import update_feed
from flomo.flomo_repo import db_load_flomo_users


def flomo_monitor(context):
    users = db_load_flomo_users()
    for u in users:
        old_update_time = u.last_update_time
        marks, new_update_time = update_feed(u.feed_url, old_update_time)

        if (marks is None) | (new_update_time is None):
            # no updates
            return
        for mark in marks:
            send_to_flomo(u.flomo_api, mark)
