import feedparser


def update_feed(feed_url, latest_note_time):
    rss_d = feedparser.parse(feed_url)
    notes = rss_d.entries

    for i in range(len(notes)):
        if old_note_link == notes[i]['guid']:
            notes = notes[0:i]
            break
    if len(notes) == 0:
        return
    db_update_feed(chat_id, notes[0]['guid'])
    rss_mem_flash()

    # send message
    for note in notes[::-1]:
        send_message(context, chat_id, note)