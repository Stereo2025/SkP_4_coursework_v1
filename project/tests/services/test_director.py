import pytest
from project.service.director import DirectorService


class TestDirectorService:

    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        genre = self.director_service.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        assert len(self.director_service.get_all()) > 0
        assert self.director_service.get_all() is not None

    def test_create(self):
        genre_dao = {'id': 4, 'name': 'Genre4'}
        genre = self.director_service.create(genre_dao)
        assert genre.id is not None

    def test_update(self):
        genre_dao = {'id': 2, 'name': 'TestName'}
        self.director_service.update(genre_dao)

    def test_delete(self):
        self.director_service.delete(1)
