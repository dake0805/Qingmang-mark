import time

t_format = "%a, %d %b %Y %H:%M:%S +0000"


def str2datetime(str):
    return time.strptime(str, t_format)
