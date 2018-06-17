FROM python:3.6-stretch
COPY . /jolie-backend
WORKDIR /jolie-backend
RUN pip install pipenv && pipenv install --system
CMD gunicorn --bind 0.0.0.0:8000 wsgi:app

