import pytest
from project.service.genre import GenreService


class TestGenreService:

    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        assert len(self.genre_service.get_all()) > 0
        assert self.genre_service.get_all() is not None

    def test_create(self):
        genre_dao = {'id': 4, 'name': 'Genre4'}
        genre = self.genre_service.create(genre_dao)
        assert genre.id is not None

    def test_update(self):
        genre_dao = {'id': 2, 'name': 'TestName'}
        self.genre_service.update(genre_dao)

    def test_delete(self):
        self.genre_service.delete(1)
