import json
from Note import Note
from datetime import datetime
class NotesManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = []

    def load_notes(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                for note_data in data:
                    note = Note(
                        note_data["id"],
                        note_data["title"],
                        note_data["body"]
                    )
                    note.created_at = datetime.strptime(note_data["created_at"], "%Y-%m-%d %H:%M:%S")
                    note.updated_at = datetime.strptime(note_data["updated_at"], "%Y-%m-%d %H:%M:%S")
                    self.notes.append(note)
        except FileNotFoundError:
            pass

    def save_notes(self):
        data = [note.to_dict() for note in self.notes]
        with open(self.file_path, "w") as file:
            json.dump(data, file)

    def create_note(self, title, body):
        id = len(self.notes) + 1
        note = Note(id, title, body)
        self.notes.append(note)

    def read_notes(self):
        for note in self.notes:
            print(note)
            print()

    def update_note(self, id, title, body):
        for note in self.notes:
            if note.id == id:
                note.update(title, body)
                break

    def delete_note(self, id):
        for note in self.notes:
            if note.id == id:
                self.notes.remove(note)
                break

def main():
    file_path = "notes.json"
    manager = NotesManager(file_path)
    manager.load_notes()

    while True:
        print("1. Создать заметку")
        print("2. Показать список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            manager.create_note(title, body)
            manager.save_notes()
            print("Заметка успешно создана!")

        elif choice == "2":
            manager.read_notes()

        elif choice == "3":
            id = int(input("Введите ID заметки, которую хотите отредактировать: "))
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            manager.update_note(id, title, body)
            manager.save_notes()
            print("Заметка успешно отредактирована!")

        elif choice == "4":
            id = int(input("Введите ID заметки, которую хотите удалить: "))
            manager.delete_note(id)
            manager.save_notes()
            print("Заметка успешно удалена!")

        elif choice == "5":
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()            