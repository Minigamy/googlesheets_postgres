# googlesheets_postgres
Collect information from google sheets and upload it to Postgres DB.

# Описание
Данный скрипт загружает данные из таблицы Google Sheets, добавляет столбец «стоимость в руб.» по курсу ЦБ и загружает в БД.
Скрипт обновляет данные каждую минуту.

Ссылка на Google таблицу:
https://docs.google.com/spreadsheets/d/1qYgv1AGB7eyeNyYciHAvyGZkR9fvxUKUWjvqy4No568/edit#gid=0

***
# Запуск в Docker
1) Скачиваем/клонируем репозиторий `https://github.com/Minigamy/googlesheets_postgres`
2) Запускаем контейнеры с Postgresql, pgAdmin и скриптом командой в терминале `docker-compose up --build -d` (Обязательно должен быть установлен и запущен Docker)

Все, база данных, pgAdmin и скрипт работают. Теперь можно подключиться к БД через pgAdmin и проверить таблицу.

***
## `pgAdmin`

Для подключения к pgAdmin потребуется выполнить следующие действия:
1) В браузере открыть страничку `http://127.0.0.1:5050/`
2) Ввести логин и пароль:
*     Логин: myemail@email.com
*     Пароль: root
![Скриншот](https://github.com/Minigamy/Django_PG-in-Docker/blob/0abcb081a973670c7acaea74a0c0b810a2e85b8f/media/pgadmin_start.png)
<p align="center">pgAdmin - Вход</p> 

3) Во вкладке General заполняем поле Name. Можно выбрать любое имя.
4) Во вкладке Connection необходимо заполнить следующие поля:
*     Host name/address: pg_db
*     Port: 5432
*     Username: root
*     Password: root
![Скриншот](https://github.com/Minigamy/Django_PG-in-Docker/blob/0abcb081a973670c7acaea74a0c0b810a2e85b8f/media/pgadmin_connect.png)
<p align="center">pgAdmin - Подключение</p> 

5) Сохраняем на кнопку `Save`


***
# Запуск без Docker

1) Скачиваем/клонируем репозиторий `https://github.com/Minigamy/googlesheets_postgres`
2) Устанавливаем зависимости из файла req.txt командой в терминале `pip install -r req.txt`
3) Запускаем скрипт `scheduler.py`

Для корректной работы БД в файле `main.py` в самом начале необходимо указать ваши данные `USER` и `PASSWORD` для подключения к БД.
В данном случает это:

    USER = "postgres"

    PASSWORD = "postgres"

