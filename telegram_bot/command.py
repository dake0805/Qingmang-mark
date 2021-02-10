from telegram_bot.repo import *
from qingmang.first import *


def add(update, context):
    chat_id = update.effective_chat.id
    feed_link = context.args[0]
    try:
        last_update_time = add_feed(feed_link)
    except Exception:
        update.effective_message.reply_text(
            "ERROR: The format needs to be: /add http://www.URL.com")
        return

    db_save(chat_id, feed_link, last_update_time)
    update.effective_message.reply_text(
        "added")


def help(update, context):
    text = """
轻芒杂志马克 Telegram bot
三十分钟更新一次
添加订阅：
/add https://qingmang.me/users/your_secret
    """
    update.effective_message.reply_text(text, disable_web_page_preview=True)
