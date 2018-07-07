from pecan import rest
from wsme import types as wtypes
import wsmeext.pecan as wsme_pecan
from webdemo.api import expose


class V1Controller(rest.RestController):

    @expose.expose(wtypes.text)
#    @wsme_pecan.wsexpose(wtypes.text)
    def get(self):
        return 'webdemo v1controller'