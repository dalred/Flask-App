from flask_restx import Resource, Namespace

from helpers.decorators import admin_required, auth_required
from implemented import user_service
from dao.model.user import UserSchema
from flask import request, jsonify, make_response
users_ns = Namespace('users')
user_schema = UserSchema()
users_schema = UserSchema(many=True)



@users_ns.route('/')
class UsersView(Resource):
    @admin_required
    def get(self, user_id):
        role = request.args.get('role')
        username = request.args.get('username')
        data = {
            "username": username,
            "role": role
        }
        return users_schema.dump(user_service.get_all(data)), 201

    def post(self):
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f"/users/{user.id}"}

    @auth_required
    def delete(self, user_id: int):
        user_service.delete(user_id)
        return "", 204

    @auth_required
    def put(self, user_id: int):
        req_json = request.json
        user_service.update(req_json, user_id)
        return "", 204

@users_ns.route('/<int:uid>')
class UserView(Resource):
    @admin_required
    def get(self, user_id, uid):
        return make_response(jsonify(user_schema.dump(user_service.get_one(uid))), 200)





