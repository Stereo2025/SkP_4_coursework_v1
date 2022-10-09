from flask import request
from flask_restx import Resource, Namespace
from project.implemented import user_service, auth_service
from project.dao.models import user_schema
from project.helpers.decorators import auth_required
from project.utils import bytes_to_dict

user_ns = Namespace('user')


@user_ns.route('/')
@user_ns.route('/password')
class UserView(Resource):

    @auth_required
    def get(self):
        token = request.headers['Authorization'].split('Bearer ')[-1]
        user = auth_service.get_user_by_token(token)
        return user_schema.dump(user), 200

    @auth_required
    def put(self):
        query = bytes_to_dict(request.data)
        token = request.headers['Authorization'].split('Bearer ')[-1]
        user = auth_service.get_user_by_token(token)
        query['id'] = user.id
        user_service.update_password(query)

        return '', 204

    @auth_required
    def patch(self):
        query = bytes_to_dict(request.data)
        token = request.headers['Authorization'].split('Bearer ')[-1]
        user = auth_service.get_user_by_token(token)
        query['id'] = user.id
        user_service.update_partial(query)

        return '', 204
#######################################################################################################################
