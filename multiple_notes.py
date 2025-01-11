import datetime


def create_note(note_id):

    # Функция для создания новой заметки.

    note = {}
    note['id'] = note_id
    note['user_name'] = input("Введите имя пользователя: ")

    # Выбор статуса
    note['status'] = get_status()

    note['description'] = input("Введите описание заметки: ")

    # Получаем дату создания от пользователя
    note['creation_date'] = get_creation_date()

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

def get_creation_date():

    # Функция для получения даты создания заметки от пользователя.

    while True:
        date_str = input("Введите дату создания заметки (дд-мм-гггг): ")
        try:
            date_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y")
            return date_obj.strftime("%d-%m")  # Форматируем дату в дд-мм для хранения
        except ValueError:
            print("Неверный формат даты. Используйте дд-мм-гггг")


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
    print("Заголовки:")
    for header in note['headers']:
        print(f"- {header}")
    print("-" * 20)

    check_deadline(note)


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
            if note['user_name'] == user_name:
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
            if header_to_change in note['headers']:
                found_note = note
                break
        if not found_note:
            print("Заметка с таким заголовком не найдена.")
            return
        new_status = get_status()
        found_note['status'] = new_status
        print("Статус заметки успешно изменен.")
    else:
        print("Некорректный ввод. Пожалуйста, выберите 'u' или 'h'.")

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


def main():
    # Основная функция программы, реализующая меню и управление заметками."

    notes = []
    note_id_counter = 1  # Счетчик ID заметок

    while True:
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Просмотреть все заметки")
        print("3. Изменить статус заметки")
        print("4. Выйти")

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
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
