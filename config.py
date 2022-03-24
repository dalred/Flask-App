class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'postgresql://flaskappuserdb:skyproskypro123@postgres/movies'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PWD_SALT = '249y823r9v8238r9u'.encode("utf-8")
    PWD_ITERATIONS = 1000

