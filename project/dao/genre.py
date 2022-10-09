from flask import current_app
from project.dao.models import Genre


class GenreDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, pk):
        return self.session.query(Genre).get(pk)

    def get_all(self, page=None):

        return self.session.query(Genre).all() if not page else self.session.query(Genre).paginate(
            page, current_app.config['ITEMS_PER_PAGE'], error_out=False).items

    def create(self, data):

        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def update(self, genre):

        self.session.add(genre)
        self.session.commit()
        return genre

    def delete(self, pk):

        genre = self.get_one(pk)
        self.session.delete(genre)
        self.session.commit()
#######################################################################################################################
