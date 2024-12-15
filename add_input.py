from datetime import datetime
username = input("Введите Имя пользователя:")
title = input("Введите Заголовок заметки:")
content = input("Введите Описание заметки:")
status = input("Введите Статус заметки:")
created_date = input("Введите Дата создания заметки:")
issue_date = input("Введите Дата истечения заметки (дедлайн):")

def format_date_without_year(date_str):
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    return date_obj.strftime("%d-%m")

print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", format_date_without_year(created_date))
print("Дата истечения заметки (дедлайн):", format_date_without_year(issue_date))
