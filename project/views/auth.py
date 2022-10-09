from flask import request
from flask_restx import Namespace, Resource
from project.implemented import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register')
class RegisterUserView(Resource):

    def post(self):
        query = request.json
        user = user_service.create(query)
        return '', 201, {"location": f"{user.id}"}


@auth_ns.route('/login')
class LoginUserView(Resource):

    def post(self):

        query = request.json
        email = query.get('email', None)
        password = query.get('password', None)

        if None in [email, password]:
            return '', 400

        tokens = auth_service.generate_tokens(email, password)
        return tokens, 201

    def put(self):
        query = request.json
        refresh_token = query.get('refresh_token')
        tokens = auth_service.approve_refresh_token(refresh_token)
        return tokens, 201
#######################################################################################################################
