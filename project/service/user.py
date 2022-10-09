import base64
import hashlib
import hmac
from flask import current_app

from project.dao.user import UserDAO


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, pk):
        return self.dao.get_one(pk)

    def get_all(self):
        return self.dao.get_all()

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def create(self, data):
        data['password'] = self.get_hash(data.get('password'))
        return self.dao.create(data)

    def update_password(self, data):

        pk = data.get('id')
        user = self.dao.get_one(pk)
        user.password = self.get_hash(data.get('new_password'))
        self.dao.update(user)
        return self.dao

    def update_partial(self, data):

        pk = data.get('id')
        user = self.dao.get_one(pk)

        if 'name' in data:
            user.name = data.get('name')
        if 'surname' in data:
            user.surname = data.get('surname')
        if 'favorite_genre' in data:
            user.favorite_genre_id = data.get('favorite_genre')

        self.dao.update(user)

    def delete(self, pk):
        self.dao.delete(pk)

    def get_hash(self, password):

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'),
            current_app.config['PWD_HASH_SALT'],
            current_app.config['PWD_HASH_ITERATIONS'])

        return base64.b64encode(hash_digest)

    def compare_passwords(self, password_hash, new_password):

        decoded_digest = base64.b64decode(password_hash)
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256', new_password.encode('utf-8'),
            current_app.config['PWD_HASH_SALT'],
            current_app.config['PWD_HASH_ITERATIONS'])

        return hmac.compare_digest(decoded_digest, hash_digest)
#######################################################################################################################
