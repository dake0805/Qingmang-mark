from telegram_bot.tg_repo import *
from qingmang.first import *
from flomo.flomo import add_user


def add(update, context):
    chat_id = update.effective_chat.id
    feed_link = context.args[0]
    try:
        last_update_time = add_feed(feed_link)
    except:
        update.effective_message.reply_text(
            "error @ add()")
        return

    db_save(chat_id, feed_link, last_update_time)
    update.effective_message.reply_text(
        "added")


def flomo(update, context):
    feed_link = context.args[0]
    flomo_api = context.args[1]
    try:
        if flomo_api.startswith('https://flomoapp.com/iwh/'):
            add_user(flomo_api, feed_link)
        else:
            raise Exception
    except:
        update.effective_message.reply_text(
            "error @ flomo()")


def help(update, context):
    text = """
轻芒杂志马克 Telegram bot
三十分钟更新一次
添加订阅: /add 轻芒API
自动同步到 flomo: /flomo 轻芒API FlomoAPI 
    """
    update.effective_message.reply_text(text, disable_web_page_preview=True)
