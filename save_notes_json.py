import datetime
import yaml
import json


def create_note(note_id):
    # Функция для создания новой заметки.
    note = {}
    note['id'] = note_id
    note['user_name'] = input("Введите имя пользователя: ")
    note['status'] = get_status()
    note['description'] = input("Введите описание заметки: ")
    note['creation_date'] = get_datetime_str(input("Введите дату создания (ГГГГ-MM-ДД): "))
    note['end_date'] = get_datetime_str(input("Введите дату завершения (ГГГГ-MM-ДД): "))
    note['headers'] = get_headers()
    return note


def get_status():
    # Функция для получения статуса заметки.
    while True:
        print("Выберите статус заметки:")
        print("1. Отложено")
        print("2. В процессе")
        print("3. Выполнено")
        choice = input("> ")
        if choice == '1':
            return "Отложено"
        elif choice == '2':
            return "В процессе"
        elif choice == '3':
            return "Выполнено"
        else:
            print("Неверный выбор. Попробуйте снова.")


def get_headers():
    # Функция для получения заголовков.
    headers = []
    print("Введите заголовки (нажмите Enter, чтобы закончить):")
    while True:
        header = input("> ")
        if not header:
            break
        headers.append(header)
    return headers


def get_datetime_str(date_str):
    # Функция для получения даты в формате ГГГГ-MM-ДД.
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        print("Неверный формат даты. Используйте ГГГГ-MM-ДД")
        return get_datetime_str(input("Повторите ввод: "))


def display_note(note):
    # Выводит информацию о заметке.
    print(f"ID: {note['id']}")
    print(f"Имя пользователя: {note['user_name']}")
    print(f"Статус: {note['status']}")
    print(f"Описание: {note['description']}")
    print(f"Дата создания: {note['creation_date']}")
    print(f"Дедлайн: {note['end_date']}")
    print("Заголовки:")
    for header in note['headers']:
        print(f"- {header}")
    print("-" * 20)


def check_deadline(note):
    # Проверяет дедлайн и выводит сообщение.
    try:
        creation_date = datetime.date.fromisoformat(note['creation_date'].replace('-', '/'))
        end_date = datetime.date.fromisoformat(note['end_date'].replace('-', '/'))
        today = datetime.date.today()

        if end_date < creation_date:
            print("!!! Ошибка: Дата завершения раньше даты создания !!!")
        elif end_date == today:
            print("!!! Дедлайн сегодня !!!")
        elif end_date < today:
            print("!!! Дедлайн прошел !!!")
        else:
            days_left = (end_date - today).days
            print(f"До дедлайна осталось: {days_left} дней")
    except ValueError as e:
        print(f"Ошибка при обработке дат: {e}")


def save_notes_to_file(notes, filename):
    # Сохраняет список заметок в файл в формате YAML.
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            yaml.dump(notes, file, default_flow_style=False, allow_unicode=True)
        print(f"Заметки успешно сохранены в {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении заметок в {filename}: {e}")


def save_notes_json(notes, filename):
    # Сохраняет список заметок в файл в формате JSON.
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(notes, file, indent=4, ensure_ascii=False)
        print(f"Заметки успешно сохранены в {filename} в формате JSON")
    except Exception as e:
        print(f"Ошибка при сохранении заметок в {filename}: {e}")


def load_notes_from_file(filename):
    # Загружает заметки из файла (YAML или JSON) и создает файл, если он отсутствует.
    try:
        with open(filename, 'r+', encoding='utf-8') as file:  # Открываем файл в режиме r+
            if filename.lower().endswith('.json'):
                try:
                    notes = json.load(file)
                    return notes
                except json.JSONDecodeError as e:
                    print(f"Ошибка при загрузке из JSON файла {filename}. Проверьте его содержимое. Подробности: {e}")
                    return []
            else:
                try:
                    notes = yaml.safe_load(file)
                    if notes is None:
                        return []
                    return notes
                except yaml.YAMLError as e:
                    print(f"Ошибка при чтении файла {filename}. Проверьте его содержимое. Подробности: {e}")
                    return []
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Создан новый файл.")
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                return []
        except Exception as e:
            print(f"Ошибка при создании файла {filename}: {e}")
            return []
    except Exception as e:
        print(f"Ошибка при загрузке заметок: {e}")
        return []


def change_status(notes):
    # Функция для изменения статуса заметки.
    if not notes:
        print("Нет заметок для изменения.")
        return

    change_by = input("Изменить заметку по имени пользователя (u) или заголовку (h)? (u/h): ").lower()

    if change_by == 'u':
        user_name = input("Введите имя пользователя заметки, статус которой вы хотите изменить: ")
        found_note = None
        for note in notes:
            if note['user_name'].lower() == user_name.lower():
                found_note = note
                break
        if not found_note:
            print("Заметка с таким именем пользователя не найдена.")
            return
        new_status = get_status()
        found_note['status'] = new_status
        print("Статус заметки успешно изменен.")
    elif change_by == 'h':
        header_to_change = input("Введите заголовок заметки, статус которой вы хотите изменить: ")
        found_note = None
        for note in notes:
            for header in note['headers']:
                if header.lower() == header_to_change.lower():
                    found_note = note
                    break
            if found_note:
                break
        if not found_note:
            print("Заметка с таким заголовком не найдена.")
            return
        new_status = get_status()
        found_note['status'] = new_status
        print("Статус заметки успешно изменен.")
    else:
        print("Некорректный ввод. Пожалуйста, выберите 'u' или 'h'.")


def update_note(notes):
    # Функция для обновления любого поля заметки.
    if not notes:
        print("Нет заметок для обновления.")
        return

    update_by = input("Обновить заметку по имени пользователя (u) или заголовку (h)? (u/h): ").lower()

    if update_by == 'u':
        user_name = input("Введите имя пользователя заметки для обновления: ")
        found_note = None
        for note in notes:
            if note['user_name'].lower() == user_name.lower():
                found_note = note
                break
        if not found_note:
            print("Заметка с таким именем пользователя не найдена.")
            return
    elif update_by == 'h':
        header_to_update = input("Введите заголовок заметки для обновления: ")
        found_note = None
        for note in notes:
            for header in note['headers']:
                if header.lower() == header_to_update.lower():
                    found_note = note
                    break
            if found_note:
                break
        if not found_note:
            print("Заметка с таким заголовком не найдена.")
            return
    else:
        print("Некорректный ввод. Пожалуйста, выберите 'u' или 'h'.")
        return

    field_to_update = input(
        "Какое поле вы хотите обновить? (user_name, status, description, end_date, headers): ").lower()

    if field_to_update == 'user_name':
        new_value = input("Введите новое имя пользователя: ")
        found_note['user_name'] = new_value
    elif field_to_update == 'status':
        new_value = get_status()
        found_note['status'] = new_value
    elif field_to_update == 'description':
        new_value = input("Введите новое описание: ")
        found_note['description'] = new_value
    elif field_to_update == 'end_date':
        new_value = get_datetime_str(input("Введите новую дату завершения (ГГГГ-MM-ДД): "))
        found_note['end_date'] = new_value
    elif field_to_update == 'headers':
        new_headers = []
        print("Введите новые заголовки (нажмите Enter, чтобы закончить):")
        while True:
            header = input("> ")
            if not header:
                break
            new_headers.append(header)
        found_note['headers'] = new_headers
    else:
        print("Неверное поле для обновления.")
        return

    print("Заметка успешно обновлена.")


def delete_note(notes):
    # Функция для удаления заметки по имени пользователя или заголовку.
    if not notes:
        print("Нет заметок для удаления.")
        return

    delete_by = input("Удалить заметку по имени пользователя (u) или заголовку (h)? (u/h): ").lower()

    if delete_by == 'u':
        user_name = input("Введите имя пользователя заметки для удаления: ")
        notes[:] = [note for note in notes if note['user_name'].lower() != user_name.lower()]
        print(f"Заметки пользователя '{user_name}' удалены.")
    elif delete_by == 'h':
        header_to_delete = input("Введите заголовок заметки для удаления: ")
        notes[:] = [note for note in notes if
                    not any(header.lower() == header_to_delete.lower() for header in note['headers'])]
        print(f"Заметки с заголовком '{header_to_delete}' удалены.")
    else:
        print("Некорректный ввод. Пожалуйста, выберите 'u' или 'h'.")


def search_notes(notes):
    # Функция для поиска заметок по имени пользователя, заголовку или описанию.
    if not notes:
        print("Нет заметок для поиска.")
        return

    search_term = input("Введите текст для поиска: ").lower()
    found_notes = []

    for note in notes:
        if (search_term in note['user_name'].lower() or
                search_term in note['description'].lower() or
                any(search_term in header.lower() for header in note['headers'])):
            found_notes.append(note)

    if found_notes:
        print("Найденные заметки:")
        for note in found_notes:
            display_note(note)
            check_deadline(note)
    else:
        print("Заметки не найдены.")


def main():
    # Основная функция приложения.
    filename = "notes.yaml"
    filename_json = "notes.json"
    notes = []

    # Попытка загрузить заметки из файлов при запуске
    loaded_notes = load_notes_from_file(filename)
    if loaded_notes:
        notes.extend(loaded_notes)  # Добавляем загруженные заметки в основной список
    else:
        loaded_notes = load_notes_from_file(filename_json)
        if loaded_notes:
            notes.extend(loaded_notes)

    while True:
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Просмотреть все заметки")
        print("3. Изменить статус заметки")
        print("4. Удалить заметку")
        print("5. Поиск заметок")
        print("6. Обновить заметку")
        print("7. Сохранить в JSON")
        print("8. Сохранить в YAML")
        print("9. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            note_id_counter = len(notes) + 1
            note = create_note(note_id_counter)
            notes.append(note)
            print("Заметка создана!")
        elif choice == '2':
            if not notes:
                print("Нет заметок для просмотра.")
            else:
                for note in notes:
                    display_note(note)
                    check_deadline(note)
        elif choice == '3':
            change_status(notes)
        elif choice == '4':
            delete_note(notes)
        elif choice == '5':
            search_notes(notes)
        elif choice == '6':
            update_note(notes)
        elif choice == '7':
            save_notes_json(notes, filename_json)
        elif choice == '8':
            save_notes_to_file(notes, filename)
        elif choice == '11':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
