from flask_restx import Resource, Namespace

from helpers.decorators import auth_required, admin_required
from implemented import genre_service
from dao.model.genre import GenreSchema
from flask import request, jsonify, make_response

genres_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self, user_id):
        return make_response(jsonify(genres_schema.dump(genre_service.get_all())), 200)

    @admin_required
    def post(self, user_id):
        req_json = request.json
        genre = genre_service.create(req_json)
        return "", 201, {"location": f"/genres/{genre.id}/"}


@genres_ns.route('/<int:uid>')
class GenreView(Resource):
    @auth_required
    def get(self, user_id, uid: int):
        return make_response(jsonify(genre_schema.dump(genre_service.get_one(uid))), 200)

    @admin_required
    def put(self, user_id, uid: int):
        req_json = request.json
        genre_service.update(req_json, uid)
        return "", 204

    @admin_required
    def delete(self, user_id, uid: int):
        genre_service.delete(uid)
        return "", 204
