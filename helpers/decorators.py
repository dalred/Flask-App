from helpers.constants import algo, SECRET_HERE as secret
from flask import request, abort
from implemented import user_service
import jwt
from service.auth import AuthService
authService = AuthService(user_service)



def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            user = jwt.decode(token, secret, algorithms=[algo])
            role = user.get("role")
            if role != "admin":
                abort(400)
            return func(*args, **kwargs, user_id=user['id'])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
    return wrapper


def auth_required(func):
    def wrapper(*args, **kwargs):
        data = request.headers['Authorization']
        if 'Authorization' not in request.headers:
            abort(401)
        token = data.split("Bearer ")[-1]
        try:
            user = jwt.decode(token, secret, algorithms=[algo])
            return func(*args, **kwargs, user_id=user['id'])
        except Exception as e:
            print("JWT Decode Exception", e)
        abort(401)

    return wrapper