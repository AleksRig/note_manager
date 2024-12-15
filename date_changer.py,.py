from datetime import datetime
username = "Радмир"
title = "План на день"
content = "Что нужно сделать сегодня"
status = "В работе"
created_date = "15-12-2024"
issue_date = "15-01-2025"

def format_date_without_year(date_str):
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    return date_obj.strftime("%d-%m")

print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", format_date_without_year(created_date))
print("Дата истечения заметки (дедлайн):", format_date_without_year(issue_date))

