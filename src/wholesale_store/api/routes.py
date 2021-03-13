from flask import jsonify

from wholesale_store.api import api


@api.route('/healthcheck', methods=['GET'])
def healthcheck():
    return  jsonify(status="up"), 200
