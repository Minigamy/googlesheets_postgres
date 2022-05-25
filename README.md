# googlesheets_postgres
Collect information from google sheets and upload it to Postgres DB.

# Описание
Данный скрипт загружает данные из таблицы Google Sheets, добавляет столбец «стоимость в руб.» курсу ЦБ и загружает в БД.
Скрипт обновляет данные каждую минуту.

# Запуск

1) Скачиваем/клонируем репозиторий `https://github.com/Minigamy/googlesheets_postgres`
2) Устанавливаем зависимости из файла requirements.txt командой в терминале `pip install -r req.txt`
3) Запускаем скрипт `scheduler.py`

Для корректной работы БД в файле `main.py` в самом начале необходимо указать ваши данные `USER` и `PASSWORD` для подключения к БД.
В данном случает это:

    USER = "postgres"

    PASSWORD = "postgres"
