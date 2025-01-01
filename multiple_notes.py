from datetime import datetime
import json
import os


def get_user_input(): # Функция для ввода данных от пользователя
    note = {}
    note['username'] = input("Введите имя пользователя: ")
    note['title'] = input("Введите название заметки: ")
    note['description'] = input("Введите описание заметки: ")

    # Ввод даты
    while True:
        try:
            created_date = input("Введите дату создания (формат: DD.MM.YYYY): ")
            note['created_date'] = created_date

            deadline_date = input("Введите дату завершения (формат: DD.MM.YYYY): ")
            note['deadline_date'] = deadline_date
            # Проверка формата дат
            datetime.strptime(created_date, '%d.%m.%Y')
            datetime.strptime(deadline_date, '%d.%m.%Y')
            break
        except ValueError:
            print("Неверный формат даты. Попробуйте снова.")

    # Ввод заголовков
    headers = []
    while True:
        header = input("Введите заголовок (или 'готово' для завершения): ")
        if header.lower() == 'готово':
            break
        headers.append(header)
    note['headers'] = headers

    # Выбор статуса
    statuses = ['выполнено', 'в процессе', 'отложено']
    while True:
        print("\nДоступные статусы:")
        for i, status in enumerate(statuses, 1):
            print(f"{i}. {status}")
        try:
            choice = int(input("Выберите статус (1-3): "))
            if 1 <= choice <= 3:
                note['status'] = statuses[choice - 1]
                break
        except ValueError:
            pass
        print("Неверный выбор. Попробуйте снова.")

    return note


def load_notes(): # Функция для сохранения заметки в файл
    if os.path.exists('notes.json'):
        with open('notes.json', 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


def save_notes(notes): # Функция для сохранения заметки
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=2)


def display_note(note): # Функция для вывода полученных данных
    print("\nИнформация о заметке:")
    print(f"Пользователь: {note['username']}")
    print(f"Название: {note['title']}")
    print(f"Описание: {note['description']}")
    print(f"Дата создания: {note['created_date']}")
    print(f"Дедлайн: {note['deadline_date']}")
    print("Заголовки:", ", ".join(note['headers']))
    print(f"Статус: {note['status']}")


def display_all_notes(notes): # Функция для работы с сохраненными заметками
    if not notes:
        print("\nЗаметок пока нет.")
        return

    print("\nСписок всех заметок:")
    for i, note in enumerate(notes, 1):
        print(f"\n{i}. Заметка:")
        display_note(note)


def change_status(note): # Функция для работы со статусами заметок
    statuses = ['выполнено', 'в процессе', 'отложено']
    print("\nТекущий статус:", note['status'])
    print("Доступные статусы:")
    for i, status in enumerate(statuses, 1):
        print(f"{i}. {status}")

    while True:
        try:
            choice = int(input("Выберите новый статус (1-3): "))
            if 1 <= choice <= 3:
                note['status'] = statuses[choice - 1]
                print("Статус успешно изменен!")
                break
        except ValueError:
            pass
        print("Неверный выбор. Попробуйте снова.")


def check_deadline(note): # Функция для проверки дедлайна заметок
    current_date = datetime.now()
    deadline = datetime.strptime(note['deadline_date'], '%d.%m.%Y')
    days_left = (deadline - current_date).days

    print("\nПроверка дедлайна:")
    if days_left < 0:
        print("Дедлайн просрочен!")
    elif days_left == 0:
        print("Дедлайн сегодня!")
    else:
        print(f"До дедлайна осталось {days_left} дней")


def select_note(notes): # Функция для просмотра заметок
    if not notes:
        print("\nЗаметок пока нет.")
        return None

    display_all_notes(notes)
    while True:
        try:
            choice = int(input("\nВыберите номер заметки: "))
            if 1 <= choice <= len(notes):
                return notes[choice - 1]
        except ValueError:
            pass
        print("Неверный выбор. Попробуйте снова.")


def main(): # Меню для работы с заметками
    notes = load_notes()

    while True:
        print("\nГлавное меню:")
        print("1. Создать новую заметку")
        print("2. Показать все заметки")
        print("3. Изменить статус заметки")
        print("4. Проверить дедлайн заметки")
        print("5. Выход")

        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            new_note = get_user_input()
            notes.append(new_note)
            save_notes(notes)
            print("Заметка успешно создана и сохранена!")

        elif choice == '2':
            display_all_notes(notes)

        elif choice == '3':
            note = select_note(notes)
            if note:
                change_status(note)
                save_notes(notes)

        elif choice == '4':
            note = select_note(notes)
            if note:
                check_deadline(note)

        elif choice == '5':
            print("Программа завершена.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()