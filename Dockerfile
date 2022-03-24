FROM python:3.8
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY migrations migrations
COPY dao dao
COPY views views
COPY service service
COPY app.py .
COPY config.py .
COPY functions.py .
COPY helpers helpers
COPY implemented.py .
COPY setup_db.py .
COPY create_table_user.py .
COPY flask-app.service.example .

CMD flask run -h 0.0.0.0 -p 80
