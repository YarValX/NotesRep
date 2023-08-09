import json
from datetime import datetime

class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self, title, body):
        self.title = title
        self.body = body
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __str__(self):
        return f"ID: {self.id}\nTitle: {self.title}\nBody: {self.body}\nCreated at: {self.created_at}\nUpdated at: {self.updated_at}"