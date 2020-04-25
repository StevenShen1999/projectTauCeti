from flask import request, abort
from marshmallow import ValidationError
from json import dumps, loads

def validate_with(schema):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not request.json:
                abort(400, "Missing Parametres")

            try:
                data = schema().load(request.get_json())
            except ValidationError as error:
                errorMessages = []
                for i in error.messages:
                    errorMessages.append(f"{i.capitalize()}: {error.messages[i]}")
                abort(400, "; ".join(errorMessages))

            return func(data=data, *args, **kwargs)
        return wrapper
    return decorator

def validate_with_form(schema):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not request.form:
                abort(400, "Missing Parametres")

            try:
                formData = schema().load(loads(dumps(dict(request.form))))
            except ValidationError as error:
                errorMessages = []
                for i in error.messages:
                    errorMessages.append(f"{i.capitalize()}: {error.messages[i]}")
                abort(400, "; ".join(errorMessages))

            return func(data=formData, *args, **kwargs)
        return wrapper
    return decorator

def validate_with_args(schema):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not request.args:
                abort(400, "missing Parametres")

            try:
                argsData = schema().load(loads(dumps(dict(request.args))))
            except ValidationError as error:
                errorMessages = []
                for i in error.messages:
                    errorMessages.append(f"{i.capitalize()}: {error.messages[i]}")
                abort(400, "; ".join(errorMessages))

            return func(data=argsData, *args, **kwargs)
        return wrapper
    return decorator