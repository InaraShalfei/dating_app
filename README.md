# Проект dating_app

Сайт для знакомств (API, бэкэнд)

## Адрес сайта

http://85.143.172.73/

## Существующие эндпоинты

### Регистрация нового пользователя

```
POST /api/clients/create

Content-Type: multipart/form-data
```

Обязательные поля для заполнения:

* first_name
* last_name
* email
* password
* gender
* avatar (attached file, обработка при регистрации - наложение водяного знака)
* longitude
* latitude

### Получение токена авторизации

```
POST /api/auth/jwt/create
```

Необходимо передавать токен с каждым запросом с заголовком `Authorization` со значением `Bearer {token}`.

### Эндпоинт оценивания участником другого участника

```
POST /api/clients/{id}/match
```

В случае возникновения взаимной симпатии ответом приходит адрес почты
другого пользователя, и оба пользователя получают письмо с текстом "Вы понравились пользователю {имя}".

### Получение списка всех пользователей 

```
GET /api/list
```

Возвращаются следующие данные пользователей (с пагинацией - 5 пользователей на странице):

* first_name
* last_name
* gender
* avatar
* longitude
* latitude

Поле `email` не отображается в целях приватности.

Доступна фильтрация по `first_name`, `last_name`, `gender` и дистанции до участников.
Для фильтрации по дистанции используйте следующие query parameters в URL:

* distance_min=x - не ближе, чем x километров
* distance_max=y - не далее, чем y километров

Пример получения списка всех Андреев в радиусе 15 км:

```
GET /api/list?first_name=Андрей&distance_max=15
```

## Postman Collection

[![Посмотреть онлайн](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/15098807-50f7f1c7-99cb-42fd-afd8-3c331559b364?action=collection%2Ffork&collection-url=entityId%3D15098807-50f7f1c7-99cb-42fd-afd8-3c331559b364%26entityType%3Dcollection%26workspaceId%3D8a8cf576-6103-4466-a588-11eda8a6b5fb#?env%5BDating%20Prod%5D=W3sia2V5IjoiQkFTRV9VUkwiLCJ2YWx1ZSI6Imh0dHA6Ly84NS4xNDMuMTcyLjczL2FwaS8iLCJlbmFibGVkIjp0cnVlfV0=)

> Не забудьте выбрать `Dating Prod` environment