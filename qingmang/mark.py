from dataclasses import dataclass


@dataclass
class Mark:
    page_url: str
    page_title: str
    mark_content: str
    mark_note: str
