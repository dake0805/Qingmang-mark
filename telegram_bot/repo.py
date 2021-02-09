import sqlite3

conn = sqlite3.connect("""../db/tg_bot.db""", check_same_thread=False)
c = conn.cursor()

# [0]: RSS feed 的链接
# [1]: 上次查询的最新一条的时间
rss_memcache_dict = {}


def rss_mem_flash():
    # if the dict is not empty, empty it.
    if bool(rss_memcache_dict):
        rss_memcache_dict.clear()
    for row in db_load_all():
        rss_memcache_dict[row[0]] = (row[1], row[2])


def init_sqlite_data():
    c.execute('''CREATE TABLE rss (chat_id text, feed_url text, last_time text)''')
    conn.commit()


def db_load_all():
    c.execute('SELECT * FROM rss')
    rows = c.fetchall()
    return rows


def db_save(chat_id, feed_url, last_time):
    q = [chat_id, feed_url, last_time]
    c.execute('''INSERT INTO rss('chat_id','feed_url','last_time') VALUES(?,?,?)''', q)
    conn.commit()


def db_update_feed(chat_id, new_update_time):
    q = [new_update_time, chat_id]
    c.execute('''UPDATE rss SET last_time = ? where chat_id = ?''', q)
    conn.commit()
