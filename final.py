from datetime import datetime

username = input("Введите Имя пользователя: ")
title1 = input("Введите первый заголовок: ")
title2 = input("Введите второй заголовок: ")
title3 = input("Введите третий заголовок: ")
content = input("Введите Описание заметки:")
status = input("Введите Статус заметки: ")
created_date = input("Введите Дата создания заметки (в формате ДД-ММ-ГГ): ")
issue_date = input("Введите Дата истечения заметки (дедлайн), (в формате ДД-ММ-ГГ): ")
title_list = [title1, title2, title3]

note = {}
note['Имя пользователя: '] = username
note['Описание заметки: '] = content
note['Статус заметки: '] = status
note['Дата создания заметки: '] = created_date
note['Дата истечения заметки (дедлайн): '] = issue_date
note['Заголовки: '] = title_list

print("\nЗаметка:")

for key, value in note.items():
    print(f"{key}: {value}")

def format_date_without_year(date_str):
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    return date_obj.strftime("%d-%m")
