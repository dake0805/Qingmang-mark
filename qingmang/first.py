# 检查 feed 正确，返回 last update time
import feedparser


def add_feed(feed_url):
    try:
        feed_url
    except IndexError:
        raise Exception()

    try:
        if feed_url.startswith("https://qingmang.me/users/"):
            rss_d = feedparser.parse(feed_url)
            rss_d.entries[0]['title']
        else:
            raise
    except IndexError:
        raise

    return rss_d.entries[0]['published']
