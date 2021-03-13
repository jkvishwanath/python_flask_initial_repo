from flask import Blueprint

api = Blueprint('api', __name__, )

# pylint: disable=wrong-import-position
# pylint: disable=cyclic-import
from wholesale_store.api import routes
