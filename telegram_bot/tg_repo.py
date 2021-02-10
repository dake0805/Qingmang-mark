import sqlite3

from user import TelegramUser

conn = sqlite3.connect("""../db/tg_bot.db""", check_same_thread=False)
c = conn.cursor()


def init_sqlite_data():
    c.execute('''CREATE TABLE tg (chat_id text, feed_url text, last_time text)''')
    conn.commit()


def db_load_tg_users():
    c.execute('SELECT * FROM tg')
    rows = c.fetchall()
    list = []
    for row in rows:
        list.append(TelegramUser(row[0], row[1], row[2]))
    return list



def db_save(chat_id, feed_url, last_time):
    q = [chat_id, feed_url, last_time]
    c.execute('''INSERT INTO tg('chat_id','feed_url','last_time') VALUES(?,?,?)''', q)
    conn.commit()


def db_update_feed(chat_id, new_update_time):
    q = [new_update_time, chat_id]
    c.execute('''UPDATE tg SET last_time = ? where chat_id = ?''', q)
    conn.commit()
