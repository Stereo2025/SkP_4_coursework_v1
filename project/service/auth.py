import calendar
import datetime
import jwt
from flask import abort, current_app
from project.service.user import UserService


class AuthService:

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)

        if user is None:
            abort(401)

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                abort(401)

        data = {"email": user.email}

        min15 = datetime.datetime.utcnow() + datetime.timedelta(minutes=current_app.config['TOKEN_EXPIRE_MINUTES'])
        data["exp"] = calendar.timegm(min15.timetuple())
        access_token = jwt.encode(data, current_app.config['JWT_SECRET'],
                                  algorithm=current_app.config['JWT_ALGORITHM'])

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=current_app.config['TOKEN_EXPIRE_DAYS'])
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, current_app.config['JWT_SECRET'],
                                   algorithm=current_app.config['JWT_ALGORITHM'])

        return {"access_token": access_token, "refresh_token": refresh_token}

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=current_app.config['JWT_SECRET'],
                          algorithms=[current_app.config['JWT_ALGORITHM']])
        user_email = data.get("email")

        return self.generate_tokens(user_email, None, is_refresh=True)

    def get_user_by_token(self, token):
        payload = jwt.decode(jwt=token, key=current_app.config['JWT_SECRET'],
                             algorithms=[current_app.config['JWT_ALGORITHM']])
        user_email = payload.get("email")
        user_instance = self.user_service.get_by_email(user_email)

        return user_instance
#######################################################################################################################
