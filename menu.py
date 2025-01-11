import datetime


def create_note(note_id):
    # Функция для создания новой заметки.

    note = {}
    note['id'] = note_id
    note['user_name'] = input("Введите имя пользователя: ")

    # Выбор статуса
    note['status'] = get_status()

    note['description'] = input("Введите описание заметки: ")

    # Получаем текущую дату создания
    now = datetime.datetime.now()
    note['creation_date'] = now.strftime("%d-%m")  # Формат день-месяц

    # Получаем дату завершения от пользователя
    note['end_date'] = get_end_date()

    # Заголовки
    note['headers'] = []
    print("Введите заголовки (нажмите Enter, чтобы закончить):")
    while True:
        header = input("> ")
        if not header:
            break
        note['headers'].append(header)

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


def get_end_date():
    # Функция для получения даты завершения заметки от пользователя.

    while True:
        date_str = input("Введите дату завершения заметки (дд-мм-гггг): ")
        try:
            date_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y")
            return date_obj.strftime("%d-%m")  # Форматируем дату в дд-мм для хранения
        except ValueError:
            print("Неверный формат даты. Используйте дд-мм-гггг")


def display_note(note):
    # Функция для вывода информации о заметке на экран.

    print(f"Номер заметки: {note['id']}")
    print(f"Имя пользователя: {note['user_name']}")
    print(f"Статус: {note['status']}")
    print(f"Описание: {note['description']}")
    print(f"Дата создания: {note['creation_date']}")
    print(f"Дата завершения: {note['end_date']}")

    # Проверка дедлайна и вывод информации
    check_deadline(note)

    print("Заголовки:")
    for header in note['headers']:
        print(f"- {header}")
    print("-" * 20)


def check_deadline(note):
    # Функция для проверки дедлайна заметки и вывода сообщения.

    creation_date_str = note['creation_date']
    end_date_str = note['end_date']

    creation_date_obj = datetime.datetime.strptime(creation_date_str, "%d-%m").date()
    end_date_obj = datetime.datetime.strptime(end_date_str, "%d-%m").date()

    days_left = (end_date_obj - creation_date_obj).days

    if end_date_obj < creation_date_obj:
        print(f"!!! Дедлайн прошел {-days_left} дней назад !!!")
    elif end_date_obj == creation_date_obj:
        print("!!! Дедлайн сегодня !!!")
    elif end_date_obj > creation_date_obj:
        print(f"До дедлайна осталось: {days_left} дней")


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
        "Какое поле вы хотите обновить? (Имя пользователя(Имя), Статус, Описание, Дата завершения, Заголовки): ").lower()

    if field_to_update == 'Имя пользователя' or 'имя пользователя' or 'имя' or "Имя":
        new_value = input("Введите новое имя пользователя: ")
        found_note['user_name'] = new_value
    elif field_to_update == 'Статус' or 'статус':
        new_value = get_status()
        found_note['status'] = new_value
    elif field_to_update == 'Описание' or 'описание':
        new_value = input("Введите новое описание: ")
        found_note['description'] = new_value
    elif field_to_update == 'Дата завершения' or 'дата завершения':
        new_value = get_end_date()
        found_note['end_date'] = new_value
    elif field_to_update == 'Заголовки' or 'заголовки':
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


def search_notes(notes):  # Я использовал свою реализацию данной функции

    # Функция для поиска заметок по имени пользователя, заголовку или описанию

    if not notes:
        print("Нет заметок для поиска.")
        return

    search_term = input("Введите текст для поиска(Имя пользователя, Заголовок, Описание): ").lower()
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
    else:
        print("Заметки не найдены.")


def main():
    # Основная функция программы, реализующая меню и управление заметками.

    notes = []
    note_id_counter = 1  # Счетчик ID заметок

    while True:
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Просмотреть все заметки")
        print("3. Изменить статус заметки")
        print("4. Удалить заметку")
        print("5. Поиск заметок")
        print("6. Обновить заметку")
        print("7. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            note = create_note(note_id_counter)
            notes.append(note)
            print("Заметка создана!")
            note_id_counter += 1
        elif choice == '2':
            if not notes:
                print("Нет заметок для просмотра.")
            else:
                for note in notes:
                    display_note(note)
        elif choice == '3':
            change_status(notes)
        elif choice == '4':
            delete_note(notes)
        elif choice == '5':
            search_notes(notes)
        elif choice == '6':
            update_note(notes)
        elif choice == '7':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
