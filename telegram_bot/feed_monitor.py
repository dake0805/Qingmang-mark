import html

from config import *
from qingmang.feed import update_feed
from telegram_bot.repo import *


def rss_monitor(context):
    # todo
    users = db_load_tg_users()
    for u in users:
        old_update_time = u.last_update_time
        marks, new_update_time = update_feed(u.feed_url, old_update_time)

        if (marks is None) | (new_update_time is None):
            # no updates
            return

        db_update_feed(u.chat_id, new_update_time)

        # send message
        for mark in marks:
            send_message(context, u.chat_id, mark)


def send_message(context, chat_id, mark):
    page_title = mark.page_title
    page_link = mark.page_url
    mark_content = mark.mark_content
    mark_note = mark.mark_note
    if len(mark_content) == 0 & len(mark_note) == 0:
        text = message_template_3 % (page_link, page_title
                                     )
    elif len(mark_note) == 0:
        text = message_template_2 % (page_link, page_title, mark_content
                                     )
    else:
        text = message_template_1 % (page_link, page_title,
                                     mark_content,
                                     mark_note
                                     )
    context.bot.send_message(chat_id=chat_id,
                             parse_mode='HTML',
                             text=text
                             )


def telegram_reserve_char_replace(text):
    return html.escape(text)
