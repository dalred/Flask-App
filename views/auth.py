from flask_restx import Resource, Namespace
from implemented import user_service
from flask import request, abort

from service.Jwt_token import JwtToken
from service.auth import AuthService
from service.security import compare_passwords

auth_ns = Namespace('auth')
authService = AuthService(user_service)


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        data = request.json
        username = data.get("username", None)
        password = data.get("password", None)
        if None in [username, password]:
            abort(400)
        user = user_service.get_by_name(username)
        if not user or not compare_passwords(user.password, password):
            abort(401)
        tokens = JwtToken({'user_id': user.id, 'role': user.role}).get_tokens()
        authService.user_service.update(tokens, user.id)
        return tokens, 201

    def put(self):
        refresh_token = request.json.get("refresh_token")
        data = JwtToken.decode_token(refresh_token)
        user_id = data.get("user_id")
        user = user_service.get_one(user_id)
        tokens = JwtToken({'user_id': user.id, 'role': user.role}).get_tokens()
        authService.user_service.update(tokens, user.id)
        return tokens, 201
