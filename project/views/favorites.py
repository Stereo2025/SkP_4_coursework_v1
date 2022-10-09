from flask import request
from flask_restx import Namespace, Resource
from project.implemented import auth_service, movie_service
from project.dao.models import movies_schema
from project.helpers.decorators import auth_required

favorites_ns = Namespace('favorites')


@favorites_ns.route('/movies')
class FavoritesView(Resource):

    @auth_required
    def get(self):
        token = request.headers['Authorization'].split('Bearer ')[-1]
        user = auth_service.get_user_by_token(token)
        favorite_movie = movie_service.get_favorite(user)

        return movies_schema.dump(favorite_movie), 200


@favorites_ns.route('/movies/<int:pk>')
class FavoriteView(Resource):

    @auth_required
    def post(self, pk):
        movie = movie_service.get_one(pk)
        token = request.headers['Authorization'].split('Bearer ')[-1]
        user = auth_service.get_user_by_token(token)
        movie_service.add_favorite(movie, user)

        return '', 201, {"location": f"/favorites/movies/{pk}"}

    @auth_required
    def delete(self, pk):
        movie = movie_service.get_one(pk)
        token = request.headers['Authorization'].split('Bearer ')[-1]
        user = auth_service.get_user_by_token(token)
        movie_service.delete_favorite(movie, user)

        return '', 204
#######################################################################################################################
