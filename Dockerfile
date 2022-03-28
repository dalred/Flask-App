FROM python:3.8-slim-buster
WORKDIR /code
COPY . .
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt

CMD flask run -h 0.0.0.0 -p 80

