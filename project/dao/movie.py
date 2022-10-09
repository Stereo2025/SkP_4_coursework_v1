from flask import current_app
from sqlalchemy import desc
from project.dao.models import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, pk):
        return self.session.query(Movie).get(pk)

    def get_all(self, page=None):

        return self.session.query(Movie).all() if not page else self.session.query(Movie).paginate(
            page, current_app.config['ITEMS_PER_PAGE'], error_out=False).items

    def get_new_movies(self, filter_=None, page=None):

        if filter_ == 'new':
            movies = self.session.query(Movie).order_by(desc(Movie.year))
        else:
            movies = self.session.query(Movie).order_by(Movie.year)

        if page:
            return movies.paginate(page, current_app.config['ITEMS_PER_PAGE'], error_out=False).items

        return movies

    def create(self, data):

        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie):

        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, pk):

        movie = self.get_one(pk)
        self.session.delete(movie)
        self.session.commit()

    def get_favorite_movie(self, user):

        user = user.like_movies
        return user

    def add_to_favorite(self, movie, user):
        user.like_movies.append(movie)
        self.session.commit()

    def delete_favorite_movie(self, movie, user):
        user.like_movies.remove(movie)
        self.session.commit()
#######################################################################################################################
