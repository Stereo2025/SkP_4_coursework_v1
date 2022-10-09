from flask import request
from flask_restx import Namespace, Resource
from project.implemented import director_service
from project.dao.models import director_schema, directors_schema
from project.helpers.decorators import auth_required
from project.helpers.parser import page_parser

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):

    @auth_required
    @director_ns.expect(page_parser)
    def get(self):
        directors = director_service.get_all(**page_parser.parse_args())
        query = directors_schema.dump(directors)
        return query, 200

    @auth_required
    def post(self):
        query = request.json
        director = director_service.create(query)
        return '', 201, {"location": f"/directors/{director.id}"}


@director_ns.route('/<int:pk>')
class DirectorView(Resource):

    @auth_required
    def get(self, pk):
        director = director_service.get_one(pk)
        query = director_schema.dump(director)
        return query, 200

    @auth_required
    def put(self, pk):
        query = request.json
        query['id'] = pk
        director_service.update(query)
        return '', 204

    @auth_required
    def delete(self, pk):
        director_service.delete(pk)
        return '', 204
#######################################################################################################################
