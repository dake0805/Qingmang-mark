# ==========================telegram==================================
# telegram bot token
token = ""

# set telegram use proxy
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Working-Behind-a-Proxy
REQUEST_KWARGS = {
    'proxy_url': 'http://127.0.0.1:7890/',
}

# seconds
delay = 100

# ==========================flomo==================================
FLOMO_API = ""

# ==========================format==================================

message_template_tg_1 = """
<b><a href="%s">%s</a></b>
=====
<b>%s</b>
--------
%s
              """

message_template_tg_2 = """
<b><a href="%s">%s</a></b>
=====
<b>%s</b>
              """

message_template_tg_3 = """
<b><a href="%s">%s</a></b>
              """

message_template_flomo_1 = """
#轻芒杂志 %s|%s
> %s
--------
%s
"""
message_template_flomo_2 = """
#轻芒杂志 %s|%s
> %s
"""
message_template_flomo_3 = """
#轻芒杂志 %s
%s
"""
