import feedparser
import html

from config import *
from telegram_bot.repo import *
import xml.etree.ElementTree as ET
import html2text


def rss_monitor(context):
    for chat_id, feed_data in rss_memcache_dict.items():
        old_note_link = feed_data[1]
        rss_d = feedparser.parse(feed_data[0])
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


def send_message(context, chat_id, note):
    page_title = note['title']
    page_link = note['link']
    mark_content, mark_note = parse_mark_note(note['description'])
    if len(mark_content) == 0 & len(mark_note) == 0:
        text = message_template_3 % (page_link, page_title
                                     )
    elif len(mark_note) == 0:
        text = message_template_2 % (page_link, page_title, mark_content
                                     )
    else:
        text = message_template_1 % (page_link, page_title,
                                     mark_content,
                                     mark_note
                                     )
    context.bot.send_message(chat_id=chat_id,
                             parse_mode='HTML',
                             text=text
                             )


def parse_mark_note(xml):
    xml = "<root>" + xml + "</root>"
    tree = ET.ElementTree(ET.fromstring(xml, parser=ET.XMLParser(encoding='utf-8')))
    mark_content = x2t(tree.findall('./div')[0])
    mark_note = x2t(tree.findall('./div')[1])
    return telegram_reserve_char_replace(mark_content), telegram_reserve_char_replace(mark_note)


def x2t(xml):
    xml_str = ET.tostring(xml, encoding="utf-8")
    return str.strip(html2text.html2text(xml_str.decode("utf-8")))


def telegram_reserve_char_replace(text):
    return html.escape(text)
