from dataclasses import dataclass
from config import *


@dataclass
class Mark:
    page_url: str
    page_title: str
    mark_content: str
    mark_note: str

    def text_telegram(self):
        if len(self.mark_content) == 0 & len(self.mark_note) == 0:
            text = message_template_tg_3 % (self.page_url, self.page_title
                                            )
        elif len(self.mark_note) == 0:
            text = message_template_tg_2 % (self.page_url, self.page_title, self.mark_content
                                            )
        else:
            text = message_template_tg_1 % (self.page_url, self.page_title,
                                            self.mark_content,
                                            self.mark_note
                                            )
        return text

    def text_flomo(self):
        if len(self.mark_content) == 0 & len(self.mark_note) == 0:
            text = message_template_flomo_3 % (self.page_url, self.page_title
                                               )
        elif len(self.mark_note) == 0:
            text = message_template_flomo_2 % (self.page_url, self.page_title, self.mark_content
                                               )
        else:
            text = message_template_flomo_1 % (self.page_url, self.page_title,
                                               self.mark_content,
                                               self.mark_note
                                               )
        return text
