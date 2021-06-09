from cerberus import Validator
from app.config import MESSAGE_CERBERUS
from functools import wraps
from flask import request, jsonify

def validate_schema(schema):
    """This decorator validate the request payload's using
    cerberus models for each route
    """
    def wrapper(fn):
        @wraps(fn)
        def f_decorada(*args, **kwargs):
            v = Validator(schema)
            if not v.validate(request.get_json()):
                return jsonify({'message': MESSAGE_CERBERUS}), 400
            return fn(*args, **kwargs)
        return f_decorada
    return wrapper