from services.facture_service import  FactureService as factureService
from jsonconv.entity_json_serializer import FactureJsonSerializer as json_serializer
from bottle import get, post, put, delete, response
from rest import common_ressource


@get('/api/factures')
def get_all():
    try:
        entities = factureService().find_all()
        return common_ressource.get_all(json_serializer, entities)
    except Exception as e:
        return common_ressource.error_500(e)


@get('/api/facture/<id_facture>')
def get_by_id(id_facture):
    try:
        result = factureService().find_by_id(id_facture)
        return common_ressource.get_by_id(result, json_serializer)
    except Exception as e:
        return common_ressource.error_500(e)


@post('/api/facture')
def create():
    try:
        entity = common_ressource.body_from_json(json_serializer)
        result = factureService().insert(entity)
        return common_ressource.create(result, json_serializer)
    except Exception as e:
        return common_ressource.error_500(e)


@put('/api/facture/<id_facture>')
def update(id_facture):
    try:
        entity = common_ressource.body_from_json(json_serializer)
        entity.id_compte = id_facture
        result = factureService().update(entity)
        return common_ressource.update(result)
    except Exception as e:
        return common_ressource.error_500(e)


@put('/api/facture')
def save():
    try:
        entity = common_ressource.body_from_json(json_serializer)
        result = factureService().save(entity)
        return common_ressource.save(result, json_serializer, entity)
    except Exception as e:
        return common_ressource.error_500(e)


@delete('/api/facture/<id_facture>')
def delete(id_facture):
    try:
        result = factureService().delete_by_id(id_facture)
        return common_ressource.delete(result)
    except Exception as e:
        return common_ressource.error_500(e)


@get('/api/facture/count')
def count():
    try:
        result = factureService().count_all()
        return common_ressource.count(result)
    except Exception as e:
        print(e)
        response.status = 400
