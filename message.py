import json
import time


class Message:

    def __init__(self, text, user, date = time.strftime('%d/%m/%Y %H:%M', time.localtime())):
        self.text = text
        self.user = user
        self.date = date

    def __string__(self):
        message = {
            "text": self.text,
            "username" : self.user,
            "date" : self.date
        }
        return json.dumps(message)
