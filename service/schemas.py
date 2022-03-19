from marshmallow import Schema
from marshmallow.fields import Int
from marshmallow_enum import EnumField

from service.enums import UserRole


class JwtSchema(Schema):
    user_id = Int(required=True)
    role = EnumField(UserRole, required=True)
    exp = Int()

