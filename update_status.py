from datetime import datetime

# Запросим ввод данных пользователем
username = input("Введите Имя пользователя: ")
content = input("Введите Описание заметки:")
status = input("Введите Статус заметки: ")
created_date = input("Введите Дата создания заметки (в формате ДД-ММ-ГГ): ")
issue_date = input("Введите Дата истечения заметки (дедлайн), (в формате ДД-ММ-ГГ): ")

# Создадим список для хранения заголовок и словарь для хранения введенных данных
title_list = []
note = {}

# Сохраним введенные данные в словарь
note['Имя пользователя: '] = username
note['Описание заметки: '] = content
note['Статус заметки: '] = status
note['Дата создания заметки: '] = created_date
note['Дата истечения заметки (дедлайн): '] = issue_date
note['Заголовки: '] = title_list


# Создадим цикл, чтобы пользователь сам выбирал количество заголовков
while True:
    title = input("Введите заголовок (или оставьте пустым для завершения ввода): ")
    if not title:
        break
    title_list.append(title)

# Выведем полученные пользователем данные
print("\nЗаметка:")
for key, value in note.items():
    print(f"{key}: {value}")

# Добавим возможность измениения статуса заметки
while True:
    # Функция для изменения статуса заметки
    def update_status(note):
        new_status = input("Введите новый статус заметки ('новая', 'в процессе', 'завершенная'): ")
        note['status'] = new_status
        return note

    # Добавим возможность изменить статус заметки
    update_choice = input("\nХотите изменить статус заметки? (да/нет): ").lower()
    if update_choice == 'да':
        note = update_status(note)

    # Выводим обновленную заметку
    print("\nОбновленная заметка:")
    for key, value in note.items():
        print(f"{key}: {value}")

# Изменим вывод даты с формата ДД-ММ-ГГ в формат ДД-ММ
def format_date_without_year(date_str):
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    return date_obj.strftime("%d-%m")
