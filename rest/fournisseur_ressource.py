from services.fournisseur_service import FournisseurService as fournisseurService
from jsonconv.entity_json_serializer import FactureJsonSerializer as json_serializer
from bottle import get, post, put, delete, response
from rest import common_ressource


@get('/api/fournisseur')
def get_all():
    try:
        entities = fournisseurService().find_all()
        return common_ressource.get_all(json_serializer, entities)
    except Exception as e:
        return common_ressource.error_500(e)


@get('/api/fournisseur/<id_fournisseur>')
def get_by_id(id_fournisseur):
    try:
        result = fournisseurService().find_by_id(id_fournisseur)
        return common_ressource.get_by_id(result, json_serializer)
    except Exception as e:
        return common_ressource.error_500(e)


@post('/api/fournisseur')
def create():
    try:
        entity = common_ressource.body_from_json(json_serializer)
        result = fournisseurService().insert(entity)
        return common_ressource.create(result, json_serializer)
    except Exception as e:
        return common_ressource.error_500(e)


@put('/api/fournisseur/<id_fournisseur>')
def update(id_fournisseur):
    try:
        entity = common_ressource.body_from_json(json_serializer)
        entity.id_fournisseur = id_fournisseur
        result = fournisseurService().update(entity)
        return common_ressource.update(result)
    except Exception as e:
        return common_ressource.error_500(e)


@put('/api/fournisseur')
def save():
    try:
        entity = common_ressource.body_from_json(json_serializer)
        result = fournisseurService().save(entity)
        return common_ressource.save(result, json_serializer, entity)
    except Exception as e:
        return common_ressource.error_500(e)


@delete('/api/fournisseur/<id_fournisseur>')
def delete(id_fournisseur):
    try:
        result = fournisseurService().delete_by_id(id_fournisseur)
        return common_ressource.delete(result)
    except Exception as e:
        return common_ressource.error_500(e)


@get('/api/fournisseur/count')
def count():
    try:
        result = fournisseurService().count_all()
        return common_ressource.count(result)
    except Exception as e:
        print(e)
        response.status = 400
