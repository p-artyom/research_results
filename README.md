# Результаты исследований

## Описание

Лаборатории при исследовательском центре отправляют результаты исследований в
центральный офис - в день проводится около 100 исследований. Cервис
предоставляет возможность получить результаты всех завершённых исследований с
фильтрацией по id лаборатории. Это полностью рабочий проект, который состоит
из бэкенд-приложения на _Django_. Проект готов к запуску в контейнерах.
Пагинация, эндпоинты и представления покрыты тестами. Настроен _CI_ при пуше в
ветку _main_. Эндпоинт закрыт аутентификацией при помощи JWT-токена.

## Технологии

- Python 3.11.5;
- Django 4.2;
- Django REST framework 3.14;
- PostgreSQL 14;
- Nginx 1.22.1.

## Запуск приложения локально в docker-контейнерах

Инструкция написана для компьютера с установленной _ОС Windows_ 10 или 11.

- Установите _Windows Subsystem for Linux_ по инструкции с официального сайта
[Microsoft](https://learn.microsoft.com/ru-ru/windows/wsl/install);

- Зайдите на
[официальный сайт Docker](https://www.docker.com/products/docker-desktop/),
скачайте и установите файл _Docker Desktop_;

- В корне проекта создайте .env файл и заполните следующими данными:

  - в переменной `POSTGRES_DB` должно быть название базы данных;

  - в переменной `POSTGRES_USER` должно быть имя пользователя БД;

  - в переменной `POSTGRES_PASSWORD` должен быть пароль пользователя БД;

  - в переменной `DB_NAME` должен быть адрес, по которому _Django_ будет
  соединяться с базой данных;

  - в переменной `DB_PORT` должен быть порт, по которому _Django_ будет
  обращаться к базе данных;

  - в переменную `SECRET_KEY` укажите секретный ключ для конкретной установки
  _Django_;

  - в переменную `DEBUG` укажите значение режима отладки;

  - в переменную `ALLOWED_HOSTS` укажите список строк, представляющих имена
  хоста/домена, которые может обслуживать это _Django_ приложение.

- В терминале в папке с `docker-compose.yml` выполните команду:

```text
docker compose up
```

- Перейдите в новом терминале в директорию, где лежит файл
`docker-compose.yml`, и выполните команды:

```text
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py collectstatic
docker compose exec backend cp -r /app/collected_static/. /backend_static/static/
```

- После запуска доступны следующие эндпоинты:

  - `http://127.0.0.1:8000/schema/` - Документация API;

  - `http://127.0.0.1:8000/admin/` - Админ-панель;

  - `http://127.0.0.1:8000/auth/users/` - Регистрация пользователя;

  - `http://127.0.0.1:8000/auth/jwt/create/` - Получение токена авторизации;

  - `http://127.0.0.1:8000/api/v1/tests/` - Список результатов исследований;

  - `http://127.0.0.1:8000/api/v1/tests/{id}/` - Получить конкретный результат
  исследования.

- Отправьте POST-запрос на `http://127.0.0.1:8000/auth/users/`, передав в
полях `email`, `username`, `password`:

```json
{
    "email": "user@example.com",
    "username": "example_username",
    "password": "example_password"
}
```

- Теперь можно получить токен: отправьте POST-запрос на эндпоинт
`http://127.0.0.1:8000/auth/jwt/create/`, передав действующий логин и пароль в
полях `username`, `password`:

```json
{
    "username": "example_username",
    "password": "example_password"
}
```

- API вернёт JWT-токен:

```json
{
    "access": "example_access_token",
    "refresh": "example_refresh_token"
}
```

- Токен вернётся в поле `access`, а данные из поля `refresh` пригодятся для
обновления токена. Этот токен надо будет передавать в заголовке каждого
запроса, в поле `Authorization`. Перед самим токеном должно стоять ключевое
слово `Bearer` и пробел;

- После можно получить список результатов исследований: отправьте GET-запросе
на эндпоинт `http://127.0.0.1:8000/api/v1/tests/`. Ответ будет следующим:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "lab_id": 1,
            "duration_seconds": 60,
            "results": [
                {
                    "id": 1,
                    "score": "0.56000",
                    "indicator_name": "example_indicator_name",
                    "metric_name": "example_metric_name",
                    "metric_unit": "example_metric_unit",
                    "is_within_normal_range": true
                }
            ]
        }
    ]
}
```

## Чек-лист

- [x] Модели данных;

- [x] API метод получения результатов исследований;

- [x] Тесты;

- [x] Docker compose;

- [x] База данных - PostgreSQL 14;

- [x] Документация API;

- [x] CI;

- [x] Описание и инструкция по запуску проекта.

## Автор

Пилипенко Артем
