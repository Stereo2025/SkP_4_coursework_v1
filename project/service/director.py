from project.dao.director import DirectorDAO


class DirectorService:

    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, pk):
        return self.dao.get_one(pk)

    def get_all(self, page=None):
        return self.dao.get_all(page)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        director_id = data.get('id')
        director = self.dao.get_one(director_id)
        director.name = data.get('name')
        self.dao.update(data)

    def delete(self, pk):
        self.dao.delete(pk)
#######################################################################################################################
