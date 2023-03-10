import urllib
import pymongo


def includeme(config):
    settings = config.registry.settings

    # Store DB connection in registry
    db_url = urllib.parse(settings['mongo_uri'])
    conn = pymongo.Connection(host=db_url.hostname, port=db_url.port)
    settings['db_conn'] = conn

    def _get_db(request):
        settings = request.registry.settings
        db = settings['db_conn'][db_url.path[1:]]
        if db_url.username and db_url.password:
            db.authenticate(db_url.username, db_url.password)
        return db

    config.set_request_property(_get_db, 'db', reify=True)
