from datetime import datetime

username = input("Введите Имя пользователя:")
title1 = input("Введите первый заголовок: ")
title2 = input("Введите второй заголовок: ")
title3 = input("Введите третий заголовок: ")
content = input("Введите Описание заметки:")
status = input("Введите Статус заметки:")
created_date = input("Введите Дата создания заметки:")
issue_date = input("Введите Дата истечения заметки (дедлайн):")

title_list = [title1, title2, title3]
note = []
note.extend([username, content, status, created_date, issue_date, title_list])

def format_date_without_year(date_str):
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    return date_obj.strftime("%d-%m")

print('\nИнформация о заметке:')
print(f"Имя пользователя: {note[0]}")
print(f"Содержание заметки: {note[1]}")
print(f"Статус заметки: {note[2]}")
print(f"Дата создания заметки: ", format_date_without_year(created_date))
print(f"Дата истечения заметки (дедлайн): ", format_date_without_year(issue_date))
print(f"Заголовки: ")

for index, title_list in enumerate(note[5], start=1):
    print(f"\tЗаголовок {index}: {title_list}")


