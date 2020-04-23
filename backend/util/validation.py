from flask import request, abort
from marshmallow import ValidationError

def validate_with(schema):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not request.json:
                abort(400, "Missing Email/Username/Password")

            try:
                data = schema().load(request.get_json())
            except ValidationError as error:
                abort(400, error.messages)

            return func(data=data, *args, **kwargs)
        return wrapper
    return decorator