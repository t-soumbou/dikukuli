from bottle import route, response, hook, request
import traceback
import json


@hook('after_request')
def enable_cors():
    """
    Add headers to enable CORS
    """
    _allow_origin = '*'
    _allow_methods = 'PUT, GET, POST, DELETE, OPTIONS'
    _allow_headers = 'Authorization, Origin, Accept, Content-Type, X-Requested-With'

    response.headers['Access-Control-Allow-Origin'] = _allow_origin
    response.headers['Access-Control-Allow-Methods'] = _allow_methods
    response.headers['Access-Control-Allow-Headers'] = _allow_headers

    """
    Set the 'content type' response header
    """
    # response.content_type = 'application/json; charset=UTF8' # charset not set in the response :-(
    response.set_header('Content-Type', 'application/json; charset=UTF8')


@route('/', method='OPTIONS')
@route('/<path:path>', method='OPTIONS')
def options_handler(path=None):
    return


@route('/<>', method=['GET', 'POST', 'PUT', 'DELETE'])
@route('/<>/<>', method=['GET', 'POST', 'PUT', 'DELETE'])
@route('/<>/<>/<>', method=['GET', 'POST', 'PUT', 'DELETE'])
@route('/<>/', method=['GET', 'POST', 'PUT', 'DELETE'])
@route('/<>/<>/', method=['GET', 'POST', 'PUT', 'DELETE'])
@route('/<>/<>/<>/', method=['GET', 'POST', 'PUT', 'DELETE'])
@route('/', method=['GET', 'POST', 'PUT', 'DELETE'])
def error_400():
    """
    Returns a 400 status : "Bad request"
    """
    response.status = 400


def error_500(e):
    """
    Returns a 500 status : "Internal Server Error"
    with the error description in the response payload
    """
    traceback.print_exc()
    response.status = 500
    return {"error": 500, "error_description": "{}".format(e)}


def get_all(json_serializer, entities):
    result = [json_serializer.to_json(entity) for entity in entities]
    response.status = 200
    return json.dumps(result)


def get_by_id(result, json_serializer):
    if result:
        response.status = 200
        return json_serializer.to_json(result)
    else:
        response.status = 404


def create(result, json_serializer):
    if result:
        response.status = 201
        return json_serializer.to_json(result)
    else:
        response.status = 409


def update(result):
    if result:
        response.status = 200
    else:
        response.status = 404


def save(result, json_serializer, entity):
    if result['isNew']:
        response.status = 201
        return json_serializer.to_json(result['entity'])
    else:
        response.status = 200
        return json_serializer.to_json(entity)


def delete(result):
    if result:
        response.status = 204
    else:
        response.status = 404


def count(result):
    response.status = 200
    return {"count": result}


def body_from_json(json_serializer):
    body = request.body
    if body:
        body_str = body.read().decode('utf-8')
        return json_serializer.from_json(body_str)
    else:
        response.status = 400
