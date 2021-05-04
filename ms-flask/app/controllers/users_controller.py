import json
from flask import request, Blueprint, jsonify

users = Blueprint('users', __name__)

HARDCODED_USERS = [
    {"name": "Pablo", "surname": "Rodriguez"},
    {"name": "Juan", "surname": "Perez"},
    {"name": "Martin", "surname": "Rodriguez"}
]

@users.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(HARDCODED_USERS)
