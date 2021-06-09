import json
from flask import request, Blueprint, jsonify
from app.services.users_service import get_users, get_filtered_users,\
                                       create_user, delete_user, update_user
from app.utils.utils import validate_schema
from app.controllers.cerberus_models.users import schema_create_user,\
                                                  schema_edit_user


users = Blueprint('users', __name__)


@users.route('/users', methods=['GET'])
def get_all_users():
    users = get_users()
    return jsonify(users), 200


@users.route('/users', methods=['POST'])
@validate_schema(schema_create_user)
def create_new_user():
    data = request.get_json()
    user, message = create_user(data)
    if not user:
        return jsonify({"message": message}), 409
    return jsonify({"id": user.id}), 200


@users.route('/users/<user_id>', methods=['GET'])
def get_one_user(user_id):
    user = get_filtered_users(id=user_id)
    if not user:
        return jsonify({}), 404
    return jsonify(user), 200


@users.route('/users/<user_id>', methods=['PUT'])
@validate_schema(schema_edit_user)
def update_one_user(user_id):
    data = request.get_json()
    done, message = update_user(user_id, data)
    if not done:
        return jsonify({"message": message}), 409
    return jsonify({}), 200


@users.route('/users/<user_id>', methods=['DELETE'])
def delete_one_user(user_id):
    done, message = delete_user(id=user_id)
    if not done:
        return jsonify({"message": message}), 409
    return jsonify({}), 200
