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