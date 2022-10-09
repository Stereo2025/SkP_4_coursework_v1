from main import app
from contextlib import suppress
from typing import Any, Dict, List
from sqlalchemy.exc import IntegrityError
from project.utils import read_json
from project.dao.models import Movie
from project.dao.models import Genre
from project.dao.models import Director
from project.db_config.initial_db import db


def load_data(data: List[Dict[str, Any]], model) -> None:
    for item in data:
        item['id'] = item.pop('pk')
        db.session.add(model(**item))


if __name__ == '__main__':
    fixtures: Dict[str, List[Dict[str, Any]]] = read_json("fixtures.json")

    with app.app_context():
        load_data(fixtures['movies'], Movie)
        load_data(fixtures['directors'], Director)
        load_data(fixtures['genres'], Genre)

        with suppress(IntegrityError):
            db.session.commit()
#######################################################################################################################
