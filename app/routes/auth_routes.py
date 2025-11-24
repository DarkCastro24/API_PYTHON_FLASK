from flask import Blueprint, request, jsonify, current_app

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}

    required = ["username", "email", "password"]
    for field in required:
        if field not in data:
            return jsonify({"msg": f"Falta campo {field}"}), 400

    user = current_app.user_service.register_user(
        username=data["username"],
        email=data["email"],
        password=data["password"],
        full_name=data.get("full_name"),
        age=data.get("age")
    )

    return jsonify({"msg": "Usuario creado", "user": user.to_dict()}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}

    if "email" not in data or "password" not in data:
        return jsonify({"msg": "email y password requeridos"}), 400

    auth = current_app.user_service.authenticate(data["email"], data["password"])

    if not auth:
        return jsonify({"msg": "Credenciales inválidas"}), 401

    return jsonify({
        "access_token": auth["access_token"],
        "user": auth["user"].to_dict()
    })
