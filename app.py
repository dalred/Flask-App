from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.directors import directors_ns
from views.genres import genres_ns
from views.movies import movies_ns
from views.users import users_ns
from views.auth import auth_ns
import prettytable
from create_table_user import create_table_user


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(users_ns)
    api.add_namespace(auth_ns)
    #create_data(app)

def create_data(app):
    with app.app_context():
        create_table_user()

app = create_app(Config())
app.debug = True

# if __name__ == '__main__':
#     app.run(host="localhost", debug=True)
    #client = app.test_client()  # TODO вы можете раскомментировать
    #response = client.post('/movies/', json=INSTANCE_movie)
    # with app.app_context():
    #     session = db.session()  # свой json в соответствующий аргумент
    #     cursor = session.execute("SELECT * FROM user").cursor  # функции post
    #     mytable = prettytable.from_db_cursor(cursor)
    #     mytable.max_width = 30
    #     print("БАЗА ДАННЫХ")
    #     print(mytable)
