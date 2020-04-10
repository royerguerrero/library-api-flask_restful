from flask import make_response, request, jsonify
from functools import wraps
from config import Config
import jwt, datetime

def token_requered(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-token')

        if not token:
            return make_response(jsonify({'message': 'Token is missing!'}), 403)

        try:
            data = jwt.decode(token, Config.SECRET_KEY)
        except:
            return make_response(jsonify({'message': 'Token is invalid!'}), 403)

        return f(*args, **kwargs)

    return decorated

