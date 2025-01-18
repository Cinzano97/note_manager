from note_manager.greetings import username, title, created_date, issue_date, status, content

username = input('Введите имя пользователя: ')
title = input('Введите заголовок заметки: ')
content = input('Введите описание заметки: ')
status = input('Введите статус заметки: ')
created_date = input('Введите дату создания заметки в формате "день-месяц-год": ')
issue_date = input('Введите дата истечения заметки (дедлайн) в формате "день-месяц-год": ')
print(username, title, content, status, created_date, issue_date)