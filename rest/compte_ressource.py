from services.compte_service import CompteService as compteService
from jsonconv.entity_json_serializer import CompteJsonSerializer as json_serializer
from bottle import get, post, put, delete, response
from rest import common_ressource


@get('/api/comptes')
def get_all():
    try:
        entities = compteService().find_all()
        return common_ressource.get_all(json_serializer, entities)
    except Exception as e:
        return common_ressource.error_500(e)


@get('/api/compte/<id_compte>')
def get_by_id(id_compte):
    try:
        result = compteService().find_by_id(id_compte)
        return common_ressource.get_by_id(result, json_serializer)
    except Exception as e:
        return common_ressource.error_500(e)


@post('/api/compte')
def create():
    try:
        entity = common_ressource.body_from_json(json_serializer)
        result = compteService().insert(entity)
        return common_ressource.create(result, json_serializer)
    except Exception as e:
        return common_ressource.error_500(e)


@put('/api/compte/<id_compte>')
def update(id_compte):
    try:
        entity = common_ressource.body_from_json(json_serializer)
        entity.id_compte = id_compte
        result = compteService().update(entity)
        return common_ressource.update(result)
    except Exception as e:
        return common_ressource.error_500(e)


@put('/api/compte')
def save():
    try:
        entity = common_ressource.body_from_json(json_serializer)
        result = compteService().save(entity)
        return common_ressource.save(result, json_serializer, entity)
    except Exception as e:
        return common_ressource.error_500(e)


@delete('/api/compte/<id_compte>')
def delete(id_compte):
    try:
        result = compteService().delete_by_id(id_compte)
        return common_ressource.delete(result)
    except Exception as e:
        return common_ressource.error_500(e)


@get('/api/compte/count')
def count():
    try:
        result = compteService().count_all()
        return common_ressource.count(result)
    except Exception as e:
        print(e)
        response.status = 400
