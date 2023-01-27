from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

USERS = {
    'Aakriti': {
        'name': 'Aakriti',
        'place': 'Delhi'
    },
    'Jass': {
        'name': 'Jass',
        'place': 'bengaluru'
    }
}


@view_config(route_name='user', renderer='json')
def get_user(request):
    name = request.matchdict['name']
    return USERS[name]


@view_config(route_name='users', renderer='json')
def list_users(request):
    return USERS


if __name__ == '__main__':
    config = Configurator()
    config.include('pyramid_debugtoolbar')
    config.add_route('users', '/users')
    config.add_route('user', '/users/{name}')
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
