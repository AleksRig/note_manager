import datetime

# Глобальные переменные для хранения данных заметки
username = ""
title = ""
content = ""
status = "в процессе"
created_date = None
issue_date = None
titles = []

def format_date(date_str): # Функция для изменения формата вывода дат
    date_obj = datetime.datetime.strptime(date_str, '%d-%m-%Y').date()
    return date_obj.strftime('%d.%m')

def initialize_note(): # Функция для ввода данных от пользователя
    global username, title, content, created_date, issue_date
    print("Введите имя пользователя:")
    username = input()

    print("Введите название заметки:")
    title = input()

    print("Введите содержание заметки:")
    content = input()

    print("Введите дату создания заметки в формате ДД-ММ-ГГГГ:")
    created_date_input = input()
    created_date = format_date(created_date_input)

    print("Введите дату завершения заметки в формате ДД-ММ-ГГГГ:")
    issue_date_input = input()
    issue_date = format_date(issue_date_input)

def add_titles(): # Функция для ввода заголовков
    global titles
    while True:
        print("Введите заголовок (или оставьте пустым для завершения):")
        title_input = input()
        if not title_input:
            break
        titles.append(title_input.strip())

def display_current_status(): # Функция для вывода текущего статуса
    global status
    print(f"\nТекущий статус заметки: {status}\n")

def change_status(): # Функция для выбора статуса заметки пользователем
    global status
    print("Выберите новый статус заметки:")
    statuses = {
        1: "выполнено",
        2: "в процессе",
        3: "отложено"
    }
    for key, value in statuses.items():
        print(f"{key}. {value}")

    # while True:
    user_choice = input("Ваш выбор: ")
    if user_choice.isdigit() and int(user_choice) in statuses.keys():
        status = statuses[int(user_choice)]

    else:
        print("Некорректный ввод. Попробуйте снова.\n")

def show_note_details(): # Функция для вывода данных введенных пользователем
    details = [
        ("Имя пользователя:", username),
        ("Название заметки:", title),
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
            print(f"\n{key} {value}")

def change_status_anytime(): # Функция для изменения статуса заметки
    global status
    while True:

        print("Текущий статус заметки: ", status)
        new_status = input("Вы хотите изменить статус(да или нет)?")
        if new_status == "да":
            change_status()
            show_note_details()
        else:
            print("Оставьте статус неизменным.")

if __name__ == "__main__":
    initialize_note()
    add_titles()
    display_current_status()
    change_status()
    show_note_details()
    change_status_anytime()
