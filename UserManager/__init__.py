from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from pyramid.renderers import JSON
from UserManager import db_client

from UserManager.resources import Root
from bson import json_util
import json

# def included(config):
#     config.add_route('users', '/users')
#     config.add_route('user', '/users/{name}')


# def main(global_config, **settings):
#     config = Configurator()
#     config.include(included, route_prefix='/users')
#     config.include(included, route_prefix='/users/{name}')
#     config.include('.db_client')


class MongoJSONRenderer:
    def __init__(self, info):
        pass

    def __call__(self, value, system):
        request = system.get('request')
        if request is not None:
            if not hasattr(request, 'response_content_type'):
                request.response_content_type = 'application/json'
        return json.dumps(value, default=json_util.default)


def main(global_config, **settings):
    config = Configurator(settings=settings, root_factory=Root)
    config.add_renderer('json', MongoJSONRenderer)
    config.include('.db_client')
    config.scan('.views')

    return config.make_wsgi_app()


