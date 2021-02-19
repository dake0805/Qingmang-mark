import xml.etree.ElementTree as ET

import feedparser
import html2text
from utils import *
from qingmang.mark import Mark


# 处理 rss 里的每条笔记内容格式

def update_feed(feed_url, last_time_str):
    rss_d = feedparser.parse(feed_url)
    marks = rss_d.entries

    for i in range(len(marks)):
        if has_feed_before(marks[i], last_time_str):
            marks = marks[0:i]
            break
    if len(marks) == 0:
        return None, None

    mark_list = []

    for mark in marks[::-1]:
        mark_list.append(parse(mark))
    return mark_list, marks[0]['published']  # todo last update time


def has_feed_before(mark_xml, last_time_str):
    current_mark_time = str2datetime(mark_xml['published'])
    last_time = str2datetime(last_time_str)
    return current_mark_time <= last_time


# if old_note_link == notes[i]['guid']:


def parse(mark_xml):
    page_title = mark_xml['title']
    page_url = mark_xml['link']
    mark_content, mark_note = parse_mark_note(mark_xml['description'])
    return Mark(page_url, page_title, mark_content, mark_note)


def parse_mark_note(xml):
    xml = "<root>" + xml + "</root>"
    tree = ET.ElementTree(ET.fromstring(xml, parser=ET.XMLParser(encoding='utf-8')))
    mark_content = x2t(tree.findall('./div')[0])
    mark_note = x2t(tree.findall('./div')[1])
    return mark_content, mark_note


# todo
def x2t(xml):
    xml_str = ET.tostring(xml, encoding="utf-8").decode("utf-8")
    xml_str = xml_str.replace('<blockquote>', '<p>')
    xml_str = xml_str.replace('</blockquote>', '</p>')
    return str.strip(html2text.html2text(xml_str))


