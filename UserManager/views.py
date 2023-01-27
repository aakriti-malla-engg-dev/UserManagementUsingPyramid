import json
from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from pyramid.view import forbidden_view_config, notfound_view_config
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound

from UserManager.resources import Root, Users, User

import logging

log = logging.getLogger(__name__)


@view_config(renderer='json', context=Root)
def home(context, request):
    return {'info': 'User API'}


@view_config(request_method='GET', context=User, renderer='json')
def get_user(context, request):
    r = context.retrieve()

    if r is None:
        raise HTTPNotFound()
    else:
        return r


@view_config(request_method='DELETE', context=User, renderer='json')
def delete_user(context, request):
    context.delete()

    return Response(
        status='202 Accepted',
        content_type='application/json; charset=UTF-8')


@view_config(request_method='POST', context=Users, renderer='json')
def create_user(context, request):
    r = context.create(request.json_body)

    return Response(
        status='201 Created',
        content_type='application/json; charset=UTF-8')


@view_config(request_method='PUT', context=User, renderer='json')
def update_user(context, request):
    r = context.update(request.json_body, True)

    return Response(
        status='202 Accepted',
        content_type='application/json; charset=UTF-8')


@view_config(request_method='GET', context=Users, renderer='json')
def list_users(context, request):
    return context.retrieve()


@notfound_view_config()
def notfound(request):
    return Response(
        body=json.dumps({'message': 'Custom `Not Found` message'}),
        status='404 Not Found',
        content_type='application/json')


@forbidden_view_config()
def forbidden(request):
    return Response(
        body=json.dumps({'message': 'Custom `Unauthorized` message'}),
        status='401 Unauthorized',
        content_type='application/json')

#
# if __name__ == '__main__':
#     config = Configurator()
#     config.include('pyramid_debugtoolbar')
#     config.add_route('users', '/users')
#     config.add_route('user', '/users/{name}')
#     # config.scan()
#     app = config.make_wsgi_app()
#     server = make_server('0.0.0.0', 6543, app)
#     server.serve_forever()
