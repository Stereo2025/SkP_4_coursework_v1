from flask import request
from flask_restx import Namespace, Resource
from project.implemented import genre_service
from project.dao.models import genre_schema, genres_schema
from project.helpers.decorators import auth_required
from project.helpers.parser import page_parser

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresVIew(Resource):

    @auth_required
    @genre_ns.expect(page_parser)
    def get(self):
        genres = genre_service.get_all(**page_parser.parse_args())
        query = genres_schema.dump(genres)
        return query, 200

    @auth_required
    def post(self):
        query = request.json
        genre = genre_service.create(query)
        return '', 201, {"location": f"/genres/{genre.id}"}


@genre_ns.route('/<int:pk>')
class GenreView(Resource):

    @auth_required
    def get(self, pk):
        genre = genre_service.get_one(pk)
        query = genre_schema.dump(genre)
        return query, 200

    @auth_required
    def put(self, pk):
        query = request.json
        query['id'] = pk
        genre_service.update(query)
        return '', 204

    @auth_required
    def delete(self, pk):
        genre_service.delete(pk)
        return '', 204
#######################################################################################################################
