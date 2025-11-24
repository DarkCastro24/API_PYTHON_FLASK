from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required


users_bp = Blueprint("users", __name__)


@users_bp.route("/users", methods=["GET"])
@jwt_required()
def list_users():
    users = current_app.user_service.list_users()
    return jsonify([u.to_dict() for u in users])


@users_bp.route("/users", methods=["POST"])
@jwt_required()
def create_user():
    data = request.get_json() or {}

    user = current_app.user_service.create_user(data)

    return jsonify({
        "msg": "Usuario creado",
        "user": user.to_dict()
    }), 201


@users_bp.route("/users/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id):
    user = current_app.user_service.get_user(user_id)
    return jsonify(user.to_dict())


@users_bp.route("/users/<int:user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):
    data = request.get_json() or {}

    user = current_app.user_service.update_user(user_id, data)

    return jsonify({
        "msg": "Usuario actualizado",
        "user": user.to_dict()
    })


@users_bp.route("/users/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    current_app.user_service.delete_user(user_id)

    return jsonify({"msg": "Usuario eliminado"})
