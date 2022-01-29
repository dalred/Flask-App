from flask_restx import Resource, Namespace

from helpers.decorators import auth_required, admin_required
from implemented import director_service
from dao.model.director import DirectorSchema
from flask import request, jsonify, make_response

directors_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        return make_response(jsonify(directors_schema.dump(director_service.get_all())), 200)

    @admin_required
    def post(self):
        req_json = request.json
        director = director_service.create(req_json)
        return "", 201, {"location": f"/directors/{director.id}/"}

@directors_ns.route('/<int:uid>')
class DirectorView(Resource):
    @auth_required
    def get(self, uid):
        return make_response(jsonify(director_schema.dump(director_service.get_one(uid))), 200)

    @admin_required
    def put(self, uid: int):
        req_json = request.json
        director_service.update(req_json, uid)
        return "", 204

    @admin_required
    def delete(self, uid: int):
        director_service.delete(uid)
        return "", 204
