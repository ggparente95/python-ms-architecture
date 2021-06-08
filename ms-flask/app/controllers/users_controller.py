import json
from flask import request, Blueprint, jsonify
from app.services.users_service import get_users


users = Blueprint('users', __name__)


@users.route('/users', methods=['GET'])
def get_all_users():
    users = get_users()
    return jsonify(users), 200
