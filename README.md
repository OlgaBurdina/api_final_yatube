# api_final_yatube

Полная реализация API для Yatube.

## Возможности API

API доступен только аутентифицированным пользователям.
В проекте использована аутентификация по JWT-токенам.
Аутентифицированный пользователь авторизован на изменение и удаление своего контента;
в остальных случаях доступ предоставляется только для чтения.

Для взаимодействия с ресурсами настроены такие эндпоинты:

- api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен
- api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост
- api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id
- api/v1/groups/ (GET): получаем список всех групп
- api/v1/groups/{group_id}/ (GET): получаем информацию о группе по id
- api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать
- api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id у поста с id=post_id.

В ответ на запросы POST, PUT и PATCH API возвращает объект, который был добавлен или изменён.

Доступ к эндпоинту /follow/ предоставляется только аутентифицированным пользователям. Данный эндопоинт имеет 2 метода:

- GET — возвращает все подписки пользователя, сделавшего запрос.
Возможен поиск по подпискам по параметру search
- POST — подписать пользователя, сделавшего запрос на пользователя, переданного в теле запроса.
При попытке подписаться на самого себя, пользователь получает информативное сообщение об ошибке.

Добавление новых пользователей через API не требуется.

## Примеры запросов

POST .../api/v1/posts/

```js
  {
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "group": 1
  }
```

POST .../api/v1/posts/14/comments/

```js
  {
    "text": "тест тест"
  }
```

GET .../api/v1/groups/2/

### Используемые технологии

- Python 3.9
- Django 3.2
- djangorestframework 3.12.4

### Запуск проекта

Cоздать и активировать виртуальное окружение:

```bash
python -m venv env
```

```bash
. venv/Scripts/activate
```

```python
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

Запустить проект:

```text
python manage.py runserver
```

### Разработчики

[Бурдина Ольга](https://github.com/OlgaBurdina): весь проект.
