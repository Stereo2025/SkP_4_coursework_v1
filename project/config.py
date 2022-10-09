import base64


class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./course_work_4.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    PWD_HASH_SALT = base64.b64decode("salt")
    PWD_HASH_ITERATIONS = 100_000
    TOKEN_EXPIRE_MINUTES = 30
    TOKEN_EXPIRE_DAYS = 130
    JWT_ALGORITHM = 'HS256'
    JWT_SECRET = 's3cR$eT'

    ITEMS_PER_PAGE = 12
#######################################################################################################################
