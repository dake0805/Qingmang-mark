import sqlite3

from user import FlomoUser

conn = sqlite3.connect("""../db/flomo.db""", check_same_thread=False)
c = conn.cursor()


def init_flomo_data():
    c.execute('''CREATE TABLE flomo (flomo_api text, feed_url text, last_time text)''')
    conn.commit()


def db_load_flomo_users():
    c.execute('SELECT * FROM flomo')
    rows = c.fetchall()
    list = []
    for row in rows:
        list.append(FlomoUser(row[0], row[1], row[2]))
    return list


def db_save(flomo_api, feed_url, last_time):
    q = [flomo_api, feed_url, last_time]
    c.execute('''INSERT INTO flomo('flomo_api','feed_url','last_time') VALUES(?,?,?)''', q)
    conn.commit()


def db_update_feed(flomo_api, new_update_time):
    q = [new_update_time, flomo_api]
    c.execute('''UPDATE flomo SET last_time = ? where chat_id = ?''', q)
    conn.commit()
