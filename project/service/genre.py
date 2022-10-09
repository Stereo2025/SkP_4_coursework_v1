from project.dao.genre import GenreDAO


class GenreService:

    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, pk):
        return self.dao.get_one(pk)

    def get_all(self, page=None):
        return self.dao.get_all(page)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        genre_id = data.get('id')
        genre = self.dao.get_one(genre_id)
        genre.name = data.get('name')
        self.dao.update(data)

    def delete(self, pk):
        self.dao.delete(pk)
#######################################################################################################################
