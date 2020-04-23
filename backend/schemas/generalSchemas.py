from marshmallow import Schema, fields, validate

email = fields.Email(required=True, validate=validate.Email())

username = fields.String(required=True, allow_none=False, validate=validate.Length(max=50))

password = fields.String(required=True, validate=[validate.Length(min=8, max=256), 
    validate.Regexp("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)(?!.*\s).{8,}$", error="Not strong enough")])
