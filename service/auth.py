from service.user import UserService
from flask import abort
import datetime, calendar, jwt
from helpers.constants import SECRET_HERE as secret, algo


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service
    #Просто мои фантазии, на практике реализация скорее всего другая.
    def validate_tokens(self, token):
        try:
            data = jwt.decode(token, secret, algorithms=[algo])
            username = data.get('username')
            # role = data.get('role')
            # Так как роль не указывается в ПостЗапросе невозможно выполнить связку
            user = self.user_service.get_by_name(username).first()
            #user = self.user_service.get_by_username_role(username, role).first()
            if user.access_token == token:
                return True
            else:
                abort(401)
        except Exception as e:
            abort(401)


    def generate_tokens(self, data, is_refresh=False):
        # Наверное это неправильно, хотелось бы пояснений, что же делать,
        # Так как роль не указывается в ПостЗапросе невозможно выполнить связку
        username = data.get('username')
        password = data.get('password')
        #role = data.get('role')
        user = self.user_service.get_by_name(username).first()
        #user = self.user_service.get_by_username_role(username, role).first()
        if user is None:
            abort(404)

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                abort(400)

        data = {
            "username": user.username,
            "role": user.role,
            "id": user.id
        }
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, secret, algorithm=algo)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, secret, algorithm=algo)
        tokens = {"id": user.id, "access_token": access_token, "refresh_token": refresh_token}
        return tokens

    def check_token(self, data):
        expire_time = datetime.datetime.fromtimestamp(data["exp"])
        if expire_time < datetime.datetime.now():
            return False
        else:
            return True

    def approve_refresh_token(self, refresh_token):
        try:
            data = jwt.decode(jwt=refresh_token, key=secret, algorithms=algo)
            if not self.check_token(data):
                abort(401)
            else:
                return self.generate_tokens(data, is_refresh=True)
        except Exception as e:
            abort(401)
