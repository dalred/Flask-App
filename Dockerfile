FROM python:3.8-slim
WORKDIR /code
COPY . .
python3 -m pip install -r requirements.txt

CMD flask run -h 0.0.0.0 -p 80

