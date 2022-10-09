from main import app
from project.db_config.initial_db import db


def create_data():
    with app.app_context():
        db.drop_all()
        db.create_all()


if __name__ == '__main__':
    create_data()
#######################################################################################################################
