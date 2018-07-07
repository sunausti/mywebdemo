from pecan import rest
from wsme import types as wtypes
import wsmeext.pecan as wsme_pecan
from webdemo.api import expose
from webdemo.api.controllers.v1 import users as v1_users

class V1Controller(rest.RestController):
    users = v1_users.UsersController()
    @expose.expose(wtypes.text)
#    @wsme_pecan.wsexpose(wtypes.text)
    def get(self):
        return 'webdemo v1controller'