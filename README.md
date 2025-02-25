# <p align="center">To-Do List</p>
## О проекте:
Добро пожаловать в приложение To-Do List! Это удобный инструмент для управления вашими задачами. Вы можете создавать, редактировать, удалять и отмечать задачи как выполненные. Регистрация и авторизация позволяют вам получить доступ к личному кабинету, где вы можете управлять своими задачами и настройками профиля. Приложение также поддерживает поиск задач, чтобы вы могли быстро находить нужные вам записи.
## Технологии:
* Python 3.9.13
* Django 4.2.13
* Django REST framework 3.15.2
* PostgreSQL
* HTML/CSS
* Django Templates
## Использование:
* Зарегистрируйтесь или войдите в систему, если у вас уже есть аккаунт.
* Создавайте новые задачи.
* Редактируйте или удаляйте существующие задачи.
* Используйте поиск, чтобы быстро находить задачи по названию
* Отмечайте задачи как выполненные и управляйте своим списком дел.
## Обзор веб-приложения:
### Авторизация:
![image](https://github.com/user-attachments/assets/8c2144b3-ace4-4b3a-b582-d4c38cbae410)
### Регистрация:
![image](https://github.com/user-attachments/assets/f46727fd-2a95-4f90-9c47-1f52b24e9379)
### Главная страница:
![image](https://github.com/user-attachments/assets/4b6660be-f849-48bf-bb03-8326417bbc86)
### Редактирование задачи:
![image](https://github.com/user-attachments/assets/a692f41b-878b-4143-8c29-8c77419a4113)

## Установка:
1. Клонируйте репозиторий:
```
https://github.com/EvdokimovAnR/To_do_list.git

cd To_do_list
```
Если вы не используете Git, вы можете просто скачать репозиторий исходного кода в ZIP-архив и распаковать его на свой компьютер.

2. Cоздайте виртуальное окружение:
* Для Mac и Linux: ``` python3 -m venv venv  ```
* Для Windows: ```python -m venv venv ```
  
3. Активируйте виртуальную среду:
* Для Mac и Linux: ``` source venv/bin/activate ```
* Для Windows: ```venv/bin/activate```
4. Установите  зависимости:
```
pip install -r requirements.txt
```
5. Создать в корне проекта .env и заполнить его по аналогии с файлом .env
6. Настройте и заполните базу данных:
```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata categories.json
python manage.py loaddata products.json
python manage.py loaddata productinfo.json
python manage.py loaddata users.json
```
7. Запустите сервер:
```
python manage.py runserver
```
Откройте браузер и перейдите по адресу http://127.0.0.1:8000











