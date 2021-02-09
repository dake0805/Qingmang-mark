import html

from config import *
from qingmang.feed import update_feed
from telegram_bot.repo import *


def rss_monitor(context):
    # todo
    rss_mem_flash()
    for chat_id, feed_data in rss_memcache_dict.items():
        old_update_time = feed_data[1]
        marks, new_update_time = update_feed(feed_data[0], old_update_time)

        db_update_feed(chat_id, new_update_time)

        # send message
        for mark in marks:
            send_message(context, chat_id, mark)


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
