from services.commande_service import CommandeService as commandeService
from jsonconv.entity_json_serializer import CommandeJsonSerializer as json_serializer
from bottle import get, post, put, delete, response
from rest import common_ressource


@get('/api/commandes')
def get_all():
    try:
        entities = commandeService().find_all()
        return common_ressource.get_all(json_serializer, entities)
    except Exception as e:
        return common_ressource.error_500(e)


@get('/api/commande/<id_commande>')
def get_by_id(id_commande):
    try:
        result = commandeService().find_by_id(id_commande)
        return common_ressource.get_by_id(result, json_serializer)
    except Exception as e:
        return common_ressource.error_500(e)


@post('/api/commande')
def create():
    try:
        entity = common_ressource.body_from_json(json_serializer)
        result = commandeService().insert(entity)
        return common_ressource.create(result, json_serializer)
    except Exception as e:
        return common_ressource.error_500(e)


@put('/api/commande/<id_commande>')
def update(id_commande):
    try:
        entity = common_ressource.body_from_json(json_serializer)
        entity.id_commande = id_commande
        result = commandeService().update(entity)
        return common_ressource.update(result)
    except Exception as e:
        return common_ressource.error_500(e)


@put('/api/commande')
def save():
    try:
        entity = common_ressource.body_from_json(json_serializer)
        result = commandeService().save(entity)
        return common_ressource.save(result, json_serializer, entity)
    except Exception as e:
        return common_ressource.error_500(e)


@delete('/api/commande/<id_commande>')
def delete(id_commande):
    try:
        result = commandeService().delete_by_id(id_commande)
        return common_ressource.delete(result)
    except Exception as e:
        return common_ressource.error_500(e)


@get('/api/commande/count')
def count():
    try:
        result = commandeService().count_all()
        return common_ressource.count(result)
    except Exception as e:
        print(e)
        response.status = 400
