# API Yatube
###  Описание
API Yatube позволяет публиковать записи, комментировать их, а так же подписываться на интересных авторов. Любой пользователь API Yatube способен посмотреть интересующие его посты и комментарии, даже если он не аутентифицирован в системе, но все же, некоторые возможности недоступны неаутентифицированному пользователю.
___
### Запуск проекта
Для запуска в dev-режиме вам необходимо выполнить следующие действия:

 1. Клонировать репозиторий и перейти в него
```
git clone https://github.com/Timoha23/api_final_yatube.git
```
2. Установить и активировать виртуальное окружение
```
python -m venv venv
```
либо
```
python3 -m venv env
```
3. Активируйте виртуальное окружение
```
source venv/Scripts/activate
```
4. Установите все зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
5. Выполните миграции
```
python manage.py migrate
```
6. Запустите проект
```
python manage.py runserver
```
___
### Примеры запросов к API
1. Получение всех публикаций 
>GET api/v1/posts/
```
[
    {
        "id": 1,
        "author": "first_user",
        "text": "First test post",
        "pub_date": "2022-07-26T11:05:49.301575Z",
        "image": null,
        "group": null
    },
    ...
]
```
2. Получить список комментариев для определенной публикации
>GET api/v1/posts/1/comments/
```
[
    {
        "id": 1,
        "author": "first_user",
        "text": "First test comment",
        "created": "2022-07-26T19:05:49.178715",
        "post": 1
    }
    ...
]
```
### *Более детально ознакомиться со всеми запросами API вы сможете при запуске проекта, перейдя на страницу ```redoc/``` где описана документация к API.*

## Использованные технологии

* Python 3.9;
* Django 2.2.16;
* Pillow 8.3.1;
* Django REST Framework 3.12.4;
* Djoser 2.1.0;
* Simple JWT 4.7.2;
* SQLite.

**Автор:**
*Ершов Тимофей Сергеевич*
