from wsgiref.simple_server import make_server

from pyramid.config import Configurator


def included(config):
    config.add_route('users', '/users')
    config.add_route('user', '/users/{name}')


def main(global_config, **settings):
    config = Configurator()
    config.include(included, route_prefix='/users')
    config.include(included, route_prefix='/users/{name}')
