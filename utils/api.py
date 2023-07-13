from flask import request
from functools import wraps
import config

def requires_api_token(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        api_token = request.headers.get('Authorization')
        if api_token != config.API_TOKEN:
            return {'error': 'Invalid API token'}, 401
        return func(*args, **kwargs)
    return decorated