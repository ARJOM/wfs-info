from app import app
from owslib.wfs import WebFeatureService
from flask import request, abort, jsonify


@app.route('/', methods=['GET'])
def index():
    if not request.json:
        abort(404)

    body = request.json
    print(body)
    wfs = WebFeatureService(url=body['url'], version=body['version'])
    response = wfs.get_schema(body['key'])
    return jsonify(response)
