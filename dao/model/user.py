from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from service.enums import UserRole
from setup_db import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String(255))
    role = db.Column(db.Enum(UserRole))
    access_token = db.Column(db.String)
    refresh_token = db.Column(db.String)

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str(load_only=True)
    role = EnumField(UserRole, required=True, default=UserRole.user)
    access_token = fields.Str()
    refresh_token = fields.Str()

