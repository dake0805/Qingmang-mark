import feedparser

from telegram_bot.repo import *


# todo 检查链接有效性
def add(update, context):
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



def help(update, context):
    text = """
轻芒杂志马克 Telegram bot
五分钟更新一次
添加订阅：
/add https://qingmang.me/users/your_secret
    """
    update.effective_message.reply_text(text)
