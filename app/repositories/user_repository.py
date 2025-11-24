from app.models import User
from app.db import db

class UserRepository:
    """Responsable únicamente de las operaciones CRUD en la base de datos."""

    def __init__(self, session):
        self.session = session

    def add(self, user: User):
        self.session.add(user)
        self.session.commit()
        return user

    def get_by_id(self, user_id: int):
        return self.session.query(User).get(user_id)

    def get_all(self):
        return self.session.query(User).all()

    def get_by_email(self, email: str):
        return self.session.query(User).filter(User.email == email).first()

    def get_by_username(self, username: str):
        return self.session.query(User).filter(User.username == username).first()

    def update(self, user: User, data: dict):
        for key, value in data.items():
            if key == 'password':
                user.set_password(value)
            elif hasattr(user, key):
                setattr(user, key, value)

        self.session.commit()
        return user

    def delete(self, user: User):
        self.session.delete(user)
        self.session.commit()
