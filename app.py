from flask import Flask
from flask_jwt_extended import JWTManager

from app.config import Config
from app.db import db
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.routes.auth_routes import auth_bp
from app.routes.user_routes import users_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializar DB
    db.init_app(app)

    # Inicializar JWT
    JWTManager(app)

    with app.app_context():
        # Crear tablas si no existen (solo desarrollo)
        db.create_all()

        # Inicializar repos/services globales
        user_repo = UserRepository(db.session)
        app.user_service = UserService(user_repo)

    # Registrar blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
