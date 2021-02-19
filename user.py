from dataclasses import dataclass


@dataclass
class TelegramUser:
    chat_id: str
    feed_url: str
    last_update_time: str


@dataclass
class FlomoUser:
    flomo_api: str
    feed_url: str
    last_update_time: str
