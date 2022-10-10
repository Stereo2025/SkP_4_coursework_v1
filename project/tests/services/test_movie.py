import pytest
from project.service.movie import MovieService


class TestMovieService:

    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        assert len(self.movie_service.get_all(page=1)) > 0
        assert self.movie_service.get_all(page=1) is not None

    def test_create(self):
        movie_dao = {
            'id': 1,
            'title': 'One',
            'description': 'FilmOne',
            'trailer': 'TrailerOne',
            'year': 1111,
            'rating': 1.1,
            'genre_id': 1,
            'director_id': 1
        }
        movie = self.movie_service.create(movie_dao)
        assert movie.id is not None

    def test_update(self):
        movie_dao = {
            'id': 1,
            'title': 'One',
            'description': 'FilmOne',
            'trailer': 'TrailerOne',
            'year': 1111,
            'rating': 1.1,
            'genre_id': 1,
            'director_id': 1
        }
        self.movie_service.update(movie_dao)

    def test_update_partial(self):
        movie_dao = {'id': 2, 'title': 'HelloWorld'}
        self.movie_service.update_partial(movie_dao)

    def test_delete(self):
        self.movie_service.delete(1)
