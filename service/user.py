from dao.user import UserDAO
import base64
import hashlib
import hmac
from helpers.constants import SECRET_HERE, PWD_HASH_ITERATIONS, algo
from functions import set_keys


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_user(bid)

    def get_by_name(self, username):
        user = self.dao.get_user_by_name(username)
        return user

    def get_by_username_role(self, username, role):
        user = self.dao.get_user_and_role(username, role)
        return user

    def get_all(self, data):
        role = data.get('role')
        username = data.get('username')
        if role:
            users = self.dao.get_all_users_by_role(role)
            return users
        if username:
            return self.get_by_name(username)
        users = self.dao.get_all_users()
        return users

    def create(self, data):
        data["password"] = self.make_user_password_hash(data.get("password"))
        return self.dao.create_user(data)

    def update(self, data, bid):
        update = self.get_one(bid)
        set_keys(data, update)
        self.dao.update(update)

    # def update(self, **kwargs):
    #     update = self.get_one(kwargs['id'])
    #     set_keys(kwargs['data'], update)
    #     self.dao.update(update)

    def delete(self, rid):
        self.dao.delete(rid)

    def make_user_password_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            SECRET_HERE,
            PWD_HASH_ITERATIONS
        ))

    def compare_passwords(self, password_hash, other_password) -> bool:
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac('sha256', other_password.encode(), SECRET_HERE, PWD_HASH_ITERATIONS)
        )
