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
    
while True:
    print('1. Создать заметку')
    print('2. Редактировать заметку')
    print('3. Удалить заметку')
    print('4. Вывести список заметок')
    print('5. Вывести выбранную заметку')
    print('0. Выход')
    choice = input('Выберите действие: ')
    if choice == '1':
        title = input('Введите заголовок заметки: ')
        body = input('Введите текст заметки: ')
        manager.add_note(title, body)
        print('Заметка успешно добавлена.')
    elif choice == '2':
        note_id = int(input('Введите ID заметки: '))
        title = input('Введите новый заголовок заметки: ')
        body = input('Введите новый текст заметки: ')
        if manager.edit_note(note_id, title, body):
            print('Заметка успешно отредактирована.')
        else:
            print('Заметка с таким ID не найдена.')
    elif choice == '3':
        note_id = int(input('Введите ID заметки: '))
        if manager.delete_note(note_id):
            print('Заметка успешно удалена.')
        else:
            print('Заметка с таким ID не найдена.')
    elif choice == '4':
        notes = manager.get_all_notes()
        if len(notes) > 0:
            for note in notes:
                print(f'ID: {note.note_id}, Заголовок: {note.title}, Дата создания: {note.created_at}')
        else:
            print('Список заметок пуст.')
    elif choice == '5':
        note_id = int(input('Введите ID заметки: '))
        note = manager.get_note_by_id(note_id)
        if note:
            print(f'Заголовок: {note.title}\nТекст: {note.body}\nДата создания: {note.created_at}\nДата изменения: {note.updated_at}')
        else:
            print('Заметка с таким ID не найдена.')
    elif choice == '0':
        break
    else:
        print('Неверный выбор. Попробуйте еще раз.')