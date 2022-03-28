FROM python:3.8-slim-buster
WORKDIR /code
COPY . .
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
RUN pip install -r requirements.txt

CMD flask run -h 0.0.0.0 -p 80

