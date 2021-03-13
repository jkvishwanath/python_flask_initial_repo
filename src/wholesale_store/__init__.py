import uuid

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = str(uuid.uuid4())
    #pylint: disable=import-outside-toplevel
    from wholesale_store.api import api
    app.register_blueprint(api)
    return app

