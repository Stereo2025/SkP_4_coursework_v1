from marshmallow import fields, Schema
from project.db_config.initial_db import db

favorite_user_movies = db.Table(
    'favorite_movies',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True)
)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    favorite_genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    favorite_genre = db.relationship("Genre")
    like_movies = db.relationship('Movie', secondary=favorite_user_movies, backref=db.backref('users'))


class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"))
    director = db.relationship("Director")


class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Director(db.Model):
    __tablename__ = 'directors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class GenreSchema(Schema):
    id = fields.Integer()
    name = fields.String()


class UserSchema(Schema):
    id = fields.Integer()
    email = fields.String()
    password = fields.String()
    name = fields.String()
    surname = fields.String()
    favourite_genre = fields.Nested(GenreSchema)


class DirectorSchema(Schema):
    id = fields.Integer()
    name = fields.String()


class MovieSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Integer()
    rating = fields.Float()
    genre = fields.Nested(GenreSchema)
    director = fields.Nested(DirectorSchema)


director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

user_schema = UserSchema()
#######################################################################################################################
