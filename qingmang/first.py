import feedparser


# check feed link is correct, return time of top mark.
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
