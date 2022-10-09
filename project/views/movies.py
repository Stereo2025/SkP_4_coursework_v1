from flask import request
from flask_restx import Resource, Namespace
from project.dao.models import movie_schema, movies_schema
from project.implemented import movie_service
from project.helpers.decorators import auth_required
from project.helpers.parser import page_parser

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):

    @auth_required
    @movie_ns.expect(page_parser)
    def get(self):

        movies = movie_service.get_all(**page_parser.parse_args())
        query = [row for row in request.args.keys()]
        status = request.args.get('status')

        try:
            if not query or 'page' in query and len(query) == 1:
                return movies_schema.dump(movies), 200
            else:
                new_movies = movie_service.get_new(status, **page_parser.parse_args())
                return movies_schema.dump(new_movies), 200
        except Exception as exception:
            return f'{exception}', 404

    @auth_required
    def post(self):
        query = request.json
        movie = movie_service.create(query)
        return '', 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:pk>')
class MovieView(Resource):

    @auth_required
    def get(self, pk):
        movie = movie_service.get_one(pk)
        return movie_schema.dump(movie), 200

    @auth_required
    def put(self, pk):
        query = request.json
        query['id'] = pk
        movie_service.update(query)
        return '', 204

    @auth_required
    def patch(self, pk):
        query = request.json
        query['id'] = pk
        movie_service.update_partial(query)
        return '', 204

    @auth_required
    def delete(self, pk):
        movie_service.delete(pk)
        return '', 204
#######################################################################################################################
