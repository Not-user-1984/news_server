FROM --platform=linux/amd64 python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

RUN python manage.py makemigrations

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "config.wsgi:application", "--bind", "0:8000"]