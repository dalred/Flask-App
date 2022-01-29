from flask_restx import Resource, Namespace

from implemented import user_service
from dao.model.user import UserSchema
from flask import request, jsonify, make_response
users_ns = Namespace('users')
user_schema = UserSchema()
users_schema = UserSchema(many=True)



@users_ns.route('/')
class UsersView(Resource):
    def get(self):
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

@users_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        return make_response(jsonify(user_schema.dump(user_service.get_one(uid))), 200)

    def put(self, uid: int):
        req_json = request.json
        user_service.update(req_json, uid)
        return "", 204

    def delete(self, uid: int):
        user_service.delete(uid)
        return "", 204

    def patch(self, uid: int):
        req_json = request.json
        user_service.update(req_json, uid)
        return "", 204

