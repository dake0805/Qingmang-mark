import sqlite3

conn = sqlite3.connect('_database/telegram_bot.db', check_same_thread=False)
c = conn.cursor()

# [0]: RSS feed 的链接
# [1]: 上次查询的最后链接
rss_memcache_dict = {}


# RSS________________________________________
def rss_mem_flash():
    # if the dict is not empty, empty it.
    if bool(rss_memcache_dict):
        rss_memcache_dict.clear()
    for row in db_load_all():
        rss_memcache_dict[row[0]] = (row[1], row[2])


# SQLITE
def init_sqlite_data():
    c.execute('''CREATE TABLE rss (chat_id text, feed_link text, last_note text)''')
    conn.commit()


def db_load_all():
    c.execute('SELECT * FROM rss')
    rows = c.fetchall()
    return rows


def db_save(chat_id, feed_link, last_note):
    q = [chat_id, feed_link, last_note]
    c.execute('''INSERT INTO rss('chat_id','feed_link','last_note') VALUES(?,?,?)''', q)
    conn.commit()


def db_update_feed(chat_id, note_new):
    q = [note_new, chat_id]
    c.execute('''UPDATE rss SET last_note = ? where chat_id = ?''', q)
    conn.commit()
