# 检查 feed 正确，返回 last update time
import feedparser


# todo
def add_feed(feed_url):
    # try if there are 2 arguments passed
    try:
        feed_url
    except IndexError:
        raise Exception()

    # try if the url is a valid RSS feed
    try:
        rss_d = feedparser.parse(feed_url)
        rss_d.entries[0]['title']
    except IndexError:
        raise

    return rss_d.entries[0]['published']

# rss_d.entries[0]['published'])
