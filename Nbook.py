import json
import datetime

class Note:
    def __init__(self, note_id, title, body, created_at, updated_at):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_at = created_at
        self.updated_at = updated_at

class NoteManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.notes = self.load_notes()