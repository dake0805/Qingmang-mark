import sqlite3

import feedparser

from config import delay
from repo import *


#
# def cmd_rss_list(update, context):
#     if bool(rss_dict) is False:
#
#         update.effective_message.reply_text("The database is empty")
#     else:
#         for title, url_list in rss_dict.items():
#             update.effective_message.reply_text(
#                 "Title: " + title +
#                 "\nrss url: " + url_list[0] +
#                 "\nlast checked article: " + url_list[1])


def cmd_rss_add(update, context):
    chat_id = update.effective_chat.id
    feed_link = context.args[0]

    # try if there are 2 arguments passed
    try:
        feed_link
    except IndexError:
        update.effective_message.reply_text(
            "ERROR: The format needs to be: /add http://www.URL.com")
        raise

    # try if the url is a valid RSS feed
    try:
        rss_d = feedparser.parse(feed_link)
        rss_d.entries[0]['title']
    except IndexError:
        update.effective_message.reply_text(
            "ERROR: The link does not seem to be a RSS feed or is not supported")
        raise

    db_save(chat_id, feed_link,
            str(rss_d.entries[0]['guid']))
    rss_mem_flash()
    update.effective_message.reply_text(
        "added \nTITLE: %s\nRSS: %s" % (context.args[0], context.args[1]))


# def cmd_rss_remove(update, context):
#     conn = sqlite3.connect('config/rss.db')
#     c = conn.cursor()
#     q = (context.args[0],)
#     try:
#         c.execute("DELETE FROM rss WHERE name = ?", q)
#         conn.commit()
#         conn.close()
#     except sqlite3.Error as e:
#         print('Error %s:' % e.args[0])
#     rss_load()
#     update.effective_message.reply_text("Removed: " + context.args[0])


def cmd_help(update, context):
    text = """
    轻芒杂志马克 Telegram bot
    五分钟更新一次
    添加订阅：
    /add https://qingmang.me/users/your_secret
    """
    update.effective_message.reply_text(text)
