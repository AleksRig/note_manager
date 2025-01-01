from datetime import datetime


def get_user_input(): # Функция для ввода данных от пользователя
    note = {}
    note['username'] = input("Введите имя пользователя: ")
    note['title'] = input("Введите название заметки: ")
    note['description'] = input("Введите описание заметки: ")

    # Ввод даты
    while True:
        try:
            created_date = input("Введите дату создания (формат: DD.MM.YYYY): ")
            note['created_date'] = datetime.strptime(created_date, '%d.%m.%Y')

            deadline_date = input("Введите дату завершения (формат: DD.MM.YYYY): ")
            note['deadline_date'] = datetime.strptime(deadline_date, '%d.%m.%Y')
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


def display_note(note): #Функция для вывода полученных данных
    print("\nИнформация о заметке:")
    print(f"Пользователь: {note['username']}")
    print(f"Название: {note['title']}")
    print(f"Описание: {note['description']}")
    print(f"Дата создания: {note['created_date'].strftime('%d.%m.%Y')}")
    print(f"Дедлайн: {note['deadline_date'].strftime('%d.%m.%Y')}")
    print("Заголовки:", ", ".join(note['headers']))
    print(f"Статус: {note['status']}")


def change_status(note): #Функция для изменения статуса заметки 
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

def main(): #Функция для создания меню заметки
    note = get_user_input()

    while True:
        print("\nМеню:")
        print("1. Показать заметку")
        print("2. Изменить статус")
        print("3. Выход")

        choice = input("Выберите действие (1-3): ")

        if choice == '1':
            display_note(note)
        elif choice == '2':
            change_status(note)
        elif choice == '3':
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
