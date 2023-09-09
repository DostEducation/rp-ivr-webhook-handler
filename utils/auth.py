from flask import request
from functools import wraps
import config
from utils import logger

def authenticate_api_token(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        try:
            api_token = request.headers.get('Authorization')
            if api_token != config.AUTH_TOKEN:
                logger.error(f"Invalid API token {api_token} received in the request.")
                return {'error': 'Invalid API token'}, 401
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Exception occurred while authenticating the API token. Error message: {e}")
    return decorated
