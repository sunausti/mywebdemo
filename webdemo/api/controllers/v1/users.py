import pecan
from pecan import request
from wsme import types as wtypes
from pecan import rest
from webdemo.api import expose

class User(wtypes.Base):
    name = wtypes.text
    age = int
    id = wtypes.text

class Users(wtypes.Base):
    users = [User]

class UserController(rest.RestController):

    def __init__(self, user_id):
        self.user_id = user_id
    @expose.expose(User)
    def get(self):
        user_info = {
            'id': self.user_id,
            'name': 'Alice',
            'age': 30,
        }
        return User(**user_info)

class UsersController(rest.RestController):

    @expose.expose(Users)
    def get(self):
        user_info_list = [
            {
                'name': 'Alice',
                'age': 30,
            },
            {
                'name': 'Bob',
                'age': 40,
            }
        ]
        users_list = [User(**user_info) for user_info in user_info_list]
        return Users(users=users_list)
    @expose.expose(None, body=User, status_code=201)
    def post(self, user):
        print user
    @pecan.expose()
    def _lookup(self, user_id, *remainder):
        return UserController(user_id), remainder