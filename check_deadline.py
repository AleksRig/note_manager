from datetime import datetime

# Глобальные переменные для хранения данных заметки
username = ""
content = ""
status = "в процессе"
created_date = None
issue_date = None
titles = []


def format_date(date_str):  # Функция для изменения формата вывода дат
    date_obj = datetime.strptime(date_str, '%d-%m-%Y').date()

    return date_obj.strftime('%d.%m')


def initialize_note():  # Функция для ввода данных от пользователя
    global username, content, created_date, issue_date
    print("Введите имя пользователя:")
    username = input()

    print("Введите содержание заметки:")
    content = input()

    try:  # Проверка правильности введенной даты создания
        print("Введите дату создания заметки в формате ДД-ММ-ГГГГ:")
        created_date_input = input()
        created_date = format_date(created_date_input)

    except():
        print("Некорректный формат даты. Попробуйте ввести дату в формате ГГГГ-ММ-ДД.")
        created_date_input = input()
        created_date = format_date(created_date_input)

    try:  # Проверка правильности введенной даты завершения
        print("Введите дату завершения заметки в формате ДД-ММ-ГГГГ:")
        issue_date_input = input()
        issue_date = format_date(issue_date_input)

    except():
        print("Некорректный формат даты. Попробуйте ввести дату в формате ГГГГ-ММ-ДД.")
        issue_date_input = input()
        issue_date = format_date(created_date_input)


def add_titles():  # Функция для ввода заголовков
    global titles
    while True:
        print("Введите заголовок (или оставьте пустым для завершения):")
        title_input = input()
        if not title_input:
            break
        titles.append(title_input.strip())


def display_current_status():  # Функция для вывода текущего статуса
    global status
    print(f"\nТекущий статус заметки: {status}\n")


def change_status():  # Функция для выбора статуса заметки пользователем
    global status
    print("Выберите новый статус заметки:")
    statuses = {
        1: "выполнено",
        2: "в процессе",
        3: "отложено"
    }
    for key, value in statuses.items():
        print(f"{key}. {value}")

    user_choice = input("Ваш выбор: ")
    if user_choice.isdigit() and int(user_choice) in statuses.keys():
        status = statuses[int(user_choice)]

    else:
        print("Некорректный ввод. Попробуйте снова.\n")


def show_note_details():  # Функция для вывода данных введенных пользователем
    details = [
        ("Имя пользователя:", username),

        ("Содержание заметки:", content),
        ("Статус заметки:", status),
        ("Дата создания:", created_date),
        ("Срок выполнения:", issue_date),
        ("Заголовки:", titles)
    ]
    print("\n\nЗаметка создана:")
    for key, value in details:
        if isinstance(value, list):
            print(f"{key}")
            for item in value:
                print(f"- {item}")
        else:
            print(f"{key} {value} \n ")


def change_status_anytime():  # Функция для изменения статуса заметки
    global status
    while True:
        print("\n Текущий статус заметки: ", status)
        new_status = input("\n Вы хотите изменить статус(да или нет)?")

        if new_status == "да":
            change_status()
            show_note_details()

        else:
            print("\n Оставьте статус неизменным.")

def check_deadline(): # Функция для проверки дедлайна
    created_date_obj = datetime.strptime(created_date, "%Y-%m-%d").date()
    issue_date_obj = datetime.strptime(issue_date, "%Y-%m-%d").date()
    difference = issue_date_obj - created_date_obj
    days_difference = difference.days

    return days_difference

    days_diff = calculate_days_difference(current_date_input, deadline_input)

    if days_diff == 0:
        print("Сегодня последний день дедлайна!")
    elif days_diff > 0:
        print(f"До дедлайна осталось {days_diff} дней.")
    else:
        print(f"Дедлайн завершился {abs(days_diff)} дня(-ей) назад.")


if __name__ == "__main__":
    initialize_note()
    add_titles()
    display_current_status()
    change_status()
    show_note_details()
    change_status_anytime()
    format_date()
    check_deadline()


