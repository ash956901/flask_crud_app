from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
