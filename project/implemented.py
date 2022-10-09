from project.dao.movie import MovieDAO
from project.dao.director import DirectorDAO
from project.dao.genre import GenreDAO
from project.dao.user import UserDAO
from project.service.movie import MovieService
from project.service.genre import GenreService
from project.service.director import DirectorService
from project.service.user import UserService
from project.service.auth import AuthService
from project.db_config.initial_db import db


movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)

auth_service = AuthService(user_service)
#######################################################################################################################
