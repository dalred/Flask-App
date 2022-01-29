from flask_restx import Resource, Namespace
from implemented import user_service
from flask import request, abort
from service.auth import AuthService

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
        tokens = authService.generate_tokens(data)
        authService.user_service.update(tokens, tokens['id'])
        return tokens, 201

    def put(self):
        req_json = request.json
        token = req_json.get("refresh_token")
        tokens = authService.approve_refresh_token(token)
        authService.user_service.update(tokens, tokens['id'])
        return tokens, 201