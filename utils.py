import logging
import time

t_format = "%a, %d %b %Y %H:%M:%S +0000"


def str2datetime(str):
    return time.strptime(str, t_format)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
