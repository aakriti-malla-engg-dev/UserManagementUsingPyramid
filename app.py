from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def list_users(request):
    return Response('List of users: \n')


def get_user(request):
    return Response('A user named %(name)s\n' % request.matchdict)


if __name__ == '__main__':
    config = Configurator()

    config.add_route('users', '/users')
    config.add_route('user', '/users/{name}')

    config.add_view(list_users, route_name='users')
    config.add_view(get_user, route_name='user')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
