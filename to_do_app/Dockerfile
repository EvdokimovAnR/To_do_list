FROM python:3.9.13

WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt

CMD python manage.py runserver \
    && python manage.py initialize_db \
    && python manage.py runserver 0.0.0.0:8000