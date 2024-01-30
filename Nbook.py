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
        def load_notes(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                notes = []
                for note_data in data:
                    note = Note(note_data['note_id'], note_data['title'], note_data['body'], 
                                note_data['created_at'], note_data['updated_at'])
                    notes.append(note)
                return notes
        except FileNotFoundError:
            return []

    def save_notes(self):
        data = []
        for note in self.notes:
            note_data = {
                'note_id': note.note_id,
                'title': note.title,
                'body': note.body,
                'created_at': note.created_at,
                'updated_at': note.updated_at
            }
            data.append(note_data)
        with open(self.file_name, 'w') as file:
            json.dump(data, file)

    def add_note(self, title, body):
        note_id = 1 if len(self.notes) == 0 else max(note.note_id for note in self.notes) + 1
        created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        updated_at = created_at
        note = Note(note_id, title, body, created_at, updated_at)
        self.notes.append(note)
        self.save_notes()

    def edit_note(self, note_id, title, body):
        for note in self.notes:
            if note.note_id == note_id:
                note.title = title
                note.body = body
                note.updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                return True
        return False

    def delete_note(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                self.notes.remove(note)
                self.save_notes()
                return True
        return False

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None

    def get_all_notes(self):
        return self.notes
    manager = NoteManager('notes.json')