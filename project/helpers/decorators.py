import jwt
from flask import current_app, request, abort


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(404)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            jwt.decode(token, current_app.config['JWT_SECRET'],
                       algorithms=[current_app.config['JWT_ALGORITHM']])

        except Exception as exception:
            print('JWT Decode Exception', exception)
            abort(401)

        return func(*args, **kwargs)

    return wrapper
#######################################################################################################################
