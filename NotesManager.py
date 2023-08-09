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