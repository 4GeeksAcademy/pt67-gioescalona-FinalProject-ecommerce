from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from api.models import db, User, Shirts, Jeans, Shoes
from api.utils import APIException
from flask_cors import CORS

api = Blueprint('api', __name__)
CORS(api)

@api.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email or not password:
        return jsonify({"msg": "Missing email or password"}), 400

    user = User.query.filter_by(email=email).first()

    if not user or user.password != password:  # En producción, usa hashing para la contraseña
        return jsonify({"msg": "Bad email or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token), 200

@api.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user).first()
    if user is None:
        raise APIException("USER NOT FOUND", status_code=404)
    return jsonify(user.serialize()), 200

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    response_body = {
        "message": "Hello! I'm a message that came from the backend."
    }
    return jsonify(response_body), 200

# Métodos GET ALL
@api.route('/users', methods=['GET'])
def handle_users():
    users = User.query.all()
    users_serialized = list(map(lambda item: item.serialize(), users))
    response_body = {
        "msg": "OK",
        "data": users_serialized
    }
    return jsonify(response_body), 200

@api.route('/shirts', methods=['GET'])
def handle_shirts():
    shirts = Shirts.query.all()
    shirts_serialized = list(map(lambda item: item.serialize(), shirts))
    response_body = {
        "msg": "OK",
        "data": shirts_serialized
    }
    return jsonify(response_body), 200

@api.route('/jeans', methods=['GET'])
def handle_jeans():
    jeans = Jeans.query.all()
    jeans_serialized = list(map(lambda item: item.serialize(), jeans))
    response_body = {
        "msg": "OK",
        "data": jeans_serialized
    }
    return jsonify(response_body), 200

@api.route('/shoes', methods=['GET'])
def handle_shoes():
    shoes = Shoes.query.all()
    shoes_serialized = list(map(lambda item: item.serialize(), shoes))
    response_body = {
        "msg": "OK",
        "data": shoes_serialized
    }
    return jsonify(response_body), 200

# Métodos POST
@api.route('/users', methods=['POST'])
def create_user():
    body = request.json
    new_user = User(email=body["email"], password=body["password"], is_active=True)  # Ajustar según tu modelo
    db.session.add(new_user)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": new_user.id
    }
    return jsonify(response_body), 201

@api.route('/shirts', methods=['POST'])
@jwt_required()
def create_shirt():
    body = request.json
    new_shirt = Shirts(talla=body["talla"], color=body["color"], marca=body["marca"], user_id=body["user_id"])
    db.session.add(new_shirt)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": new_shirt.id
    }
    return jsonify(response_body), 201

@api.route('/jeans', methods=['POST'])
@jwt_required()
def create_jean():
    body = request.json
    new_jean = Jeans(talla=body["talla"], color=body["color"], marca=body["marca"], user_id=body["user_id"])
    db.session.add(new_jean)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": new_jean.id
    }
    return jsonify(response_body), 201

@api.route('/shoes', methods=['POST'])
@jwt_required()
def create_shoe():
    body = request.json
    new_shoe = Shoes(talla=body["talla"], color=body["color"], marca=body["marca"], user_id=body["user_id"])
    db.session.add(new_shoe)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": new_shoe.id
    }
    return jsonify(response_body), 201
