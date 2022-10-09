from flask import Flask
from flask_restx import Api
from flask_cors import CORS

from project.config import Config
from project.db_config.initial_db import db
from project.views.movies import movie_ns
from project.views.directors import director_ns
from project.views.genres import genre_ns
from project.views.users import user_ns
from project.views.auth import auth_ns
from project.views.favorites import favorites_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.url_map.strict_slashes = False
    application.app_context().push()
    return application


def configure_app(application: Flask):
    CORS(app=app)
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(favorites_ns)


app_config = Config()
app = create_app(app_config)
configure_app(app)

if __name__ == '__main__':
    app.run(host="localhost", port=5000)
#######################################################################################################################
