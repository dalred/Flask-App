import jwt
from marshmallow import Schema
from marshmallow.fields import Int, Str
from marshmallow_enum import EnumField

from helpers.constants import PWD_SALT
refresh_token= "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NDM4MTY1NTIsInVzZXJfaWQiOjMsInJvbGUiOiJhZG1pbiJ9.tt4_13uZHVmQOeF-2nkbWMYRniyGsTC-AfjFvWNedo4"
data = jwt.decode(jwt=refresh_token, key=PWD_SALT, algorithms='HS256')

print(data)