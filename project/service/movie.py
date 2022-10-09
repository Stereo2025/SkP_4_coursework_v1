from project.dao.movie import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, pk):
        return self.dao.get_one(pk)

    def get_all(self, page):
        return self.dao.get_all(page)

    def get_new(self, filter_, page):
        return self.dao.get_new_movies(filter_, page)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):

        pk = data.get('id')
        movie = self.dao.get_one(pk)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.dao.update(movie)

    def update_partial(self, data):

        pk = data.get('id')
        movie = self.dao.get_one(pk)

        if 'title' in data:
            movie.title = data.get('title')
        if 'description' in data:
            movie.description = data.get('description')
        if 'trailer' in data:
            movie.trailer = data.get('trailer')
        if 'year' in data:
            movie.year = data.get('year')
        if 'rating' in data:
            movie.rating = data.get('rating')
        if 'genre_id' in data:
            movie.genre_id = data.get('genre_id')
        if 'director_id' in data:
            movie.director_id = data.get('director_id')

        self.dao.update(movie)

    def delete(self, pk):
        self.dao.delete(pk)

    def get_favorite(self, user):
        return self.dao.get_favorite_movie(user)

    def add_favorite(self, movie, user):
        return self.dao.add_to_favorite(movie, user)

    def delete_favorite(self, movie, user):
        return self.dao.delete_favorite_movie(movie, user)
#######################################################################################################################
