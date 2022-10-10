import pytest
from unittest.mock import MagicMock

from project.dao.models import Movie
from project.dao.models import Genre
from project.dao.models import Director
from project.dao.movie import MovieDAO
from project.dao.genre import GenreDAO
from project.dao.director import DirectorDAO


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='One', description='FilmOne', trailer='TrailerOne',
                    year=1111, rating=1.1, genre_id=1, director_id=1)

    movie_2 = Movie(id=2, title='Two', description='FilmTwo', trailer='TrailerTwo',
                    year=2222, rating=2.2, genre_id=1, director_id=1)

    movie_3 = Movie(id=3, title='Three', description='FilmThree', trailer='TrailerThree',
                    year=3333, rating=3.3, genre_id=1, director_id=1)

    all_movies = {1: movie_1, 2: movie_2, 3: movie_3}

    movie_dao.get_one = MagicMock(side_effect=all_movies.get)
    movie_dao.get_all = MagicMock(return_value=all_movies.values())
    movie_dao.create = MagicMock(return_value=Movie(id=1))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name='GenreOne')
    genre_2 = Genre(id=2, name="GenreTwo")
    genre_3 = Genre(id=3, name='GenreThree')

    all_genre = {1: genre_1, 2: genre_2, 3: genre_3}

    genre_dao.get_one = MagicMock(side_effect=all_genre.get)
    genre_dao.get_all = MagicMock(return_value=all_genre.values())
    genre_dao.create = MagicMock(return_value=Genre(id=1))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director_1 = Director(id=1, name='DirectorOne')
    director_2 = Director(id=2, name='DirectorTwo')
    director_3 = Director(id=3, name='DirectorThree')

    all_directors = {1: director_1, 2: director_2, 3: director_3}

    director_dao.get_one = MagicMock(side_effect=all_directors.get)
    director_dao.get_all = MagicMock(return_value=all_directors.values())
    director_dao.create = MagicMock(return_value=Director(id=1))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao
