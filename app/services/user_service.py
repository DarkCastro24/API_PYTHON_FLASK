from flask import abort
from flask_jwt_extended import create_access_token
from app.repositories.user_repository import UserRepository
from app.models import User


class UserService:
    """Lógica de negocio: validaciones y reglas antes de persistir/leer datos."""

    def __init__(self, user_repository: UserRepository):
        self.repo = user_repository

    def register_user(self, username, email, password, full_name=None, age=None):
        if self.repo.get_by_email(email) or self.repo.get_by_username(username):
            abort(400, description="Usuario o email ya registrado")

        user = User(
            username=username,
            email=email,
            full_name=full_name,
            age=age
        )
        user.set_password(password)
        return self.repo.add(user)

    def authenticate(self, email, password):
        user = self.repo.get_by_email(email)
        if not user or not user.check_password(password):
            return None

        token = create_access_token(identity=user.id)
        return {"access_token": token, "user": user}

    def list_users(self):
        return self.repo.get_all()

    def get_user(self, user_id):
        user = self.repo.get_by_id(user_id)
        if not user:
            abort(404, description="Usuario no encontrado")
        return user

    def create_user(self, data):
        return self.register_user(
            data.get("username"),
            data.get("email"),
            data.get("password"),
            data.get("full_name"),
            data.get("age")
        )

    def update_user(self, user_id, data):
        user = self.get_user(user_id)
        return self.repo.update(user, data)

    def delete_user(self, user_id):
        user = self.get_user(user_id)
        self.repo.delete(user)
