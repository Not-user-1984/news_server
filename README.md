## Проект **NEWS_SErves** 


![python version](https://img.shields.io/badge/Python-3.9-green)
![django version](https://img.shields.io/badge/Django-4.1-green)
![Docker version](https://img.shields.io/badge/Docker-4.15-green)
![Djangorestframework version](https://img.shields.io/badge/Djangorestframework-3.14-green)
![PyJWT version](https://img.shields.io/badge/PyJWT-2.6-green)
![gunicornversion](https://img.shields.io/badge/gunicorn-20.01-green)
![gunicornversion](https://img.shields.io/badge/nginx-1.19.3-green)


#### Проект доступен по адресу

[http://84.201.167.210/api/v1/news/](http://84.201.167.210/api/v1/news/)

[Документация Api](http://84.201.167.210:8002/)
Документация сделана Snippets запушина в контeйнере Docker (не работает тестирование, но посмотреть какие ручки есть можно)

[админка](http://84.201.167.210/admin/)
User: Test  Pass: 1234 (в админке можно выбирать роль у каждого пользователя)
<hr>

## Описание
[servis_likes](backend/src/news_server/servis_likes.py)
Лайки сделаны через redis(развернут контейнер в docker)

[0002_data_loading.py](backend/src/news_server/migrations/0002_data_loading.py)
 сделана загрузка тестовых новостей и пользователей через миграцию 
<br> 
<hr>
<details>
<summary><strong>Запуск в Docker контейнерах</strong></summary>
<br>
Установите Docker.

Склонировать проект с git
```
https://github.com/Not-user-1984/testovoe_itfox
```

В директории infra/local_dev необходимо создать файл .env:
```
cd infra/local_dev
touch .env
```

В котором требуется указать переменные окружения, пример:
```
echo SECRET_KEY=************ >> .env

echo DB_ENGINE=django.db.backends.postgresql >> .env

echo DB_NAME=postgres >> .env

echo POSTGRES_USER=postgres  >> .env

echo POSTGRES_PASSWORD=postgres >> .env

echo DB_HOST=db  >> .env

echo DB_PORT=5432  >> .env
```

В директории infra/local_dev/ngix в файле nginx.conf измените адрес(ip/домен), необходимо указать адрес вашего сервера.

Запустите docker compose
```
docker-compose up -d --build
```

Примените миграции
```
docker-compose exec backend python manage.py migrate
```

Создайте суперпользователя
```
docker-compose exec backend python manage.py createsuperuser
```

Далее соберите статику
```
docker-compose exec backend python manage.py collectstatic --noinput
```
</details>
<br>
<hr>

<details>
<summary><strong> Уровни доступа</strong></summary>
<br>

### Уровни доступа пользователей:
Гость (неавторизованный пользователь)
Авторизованный пользователь
Администратор

### Что могут делать неавторизованные пользователи
- Создать аккаунт.
- Просматривать новости и коментарии.


### Что могут делать авторизованные пользователи
- Входить в систему под своим логином и паролем.
- Выходить из системы (разлогиниваться).
- Менять свой пароль.
- Создавать/редактировать/удалять новости если он их создал
- Ставить лайки


### Что может делать администратор 
Администратор обладает всеми правами авторизованного пользователя. 
Плюс к этому он может:
- изменять пароль любого пользователя,
- создавать/блокировать/удалять аккаунты пользователей,
- редактировать/удалять любые новости,
- добавлять/удалять/ любые комментарии.


</details>

<br>
<hr>
<details>

<br>
<summary><strong> API Примеры запросов: </strong></summary>
<br>

Примеры запросов:
Для регистрации пользователя, необходимо отправить POST запрос на адрес:
```
http://84.201.167.210/api/v1/users/
```
Тело запроса
```
{
  "email": "user@example.com",
  "username": "string",
  "password": "string"
}
```

Для получения токена, следует отправить POST запрос на адрес:
```
http://84.201.167.210/api/v1/jwt/create
```
Тело запроса
```
{
    "password": "baiden_lox",
    "email": "vova_not_is@yandex.ru"
}
```

Получить список новостей можно отправив GET запрос на эндпоинт:
```
http://84.201.167.210/api/v1/news/
```

Чтобы создать новость отправить POST запрос на адрес(Доступно только с токеном):
```
http://84.201.167.210/api/v1/news/
```

Тело запроса
```
{
  "title": "Новая новость",
  "text": "новая новость"
}
```

Чтобы создать комментрарий к новости POST (Доступно только с токеном):
```
http://84.201.167.210/api/v1/news/2/comments/
```
Тело запроса
```
{
  "text": "uhsffsfsffs",
  "news": 2
}
```

</details>

<br>
<br>
<br>
<hr>

#### **Разработчик**:
[Дима Плужников](https://github.com/Not-user-1984)

#### **Tg**:
@DmitryPluzhnikov