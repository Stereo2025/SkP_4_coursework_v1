from project.dao.models import User


class UserDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, pk):

        return self.session.query(User).get(pk)

    def get_all(self):

        return self.session.query(User).all()

    def get_by_email(self, email):

        return self.session.query(User).filter(User.email == email).first()

    def create(self, data):

        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user):

        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, pk):

        user = self.get_one(pk)
        self.session.delete(user)
        self.session.commit()
#######################################################################################################################
