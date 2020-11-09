from services.approvisionnement_service import ApprovisionnementService as approvisionnementService
from jsonconv.entity_json_serializer import ApprovisionnementJsonSerializer as json_serializer
from bottle import get, post, put, delete, response
from rest import common_ressource


@get('/api/approvisionnements')
def get_all():
    try:
        entities = approvisionnementService().find_all()
        return common_ressource.get_all(json_serializer, entities)
    except Exception as e:
        return common_ressource.error_500(e)


@get('/api/approvisionnement/<id_fournisseur>/<id_produit>')
def get_by_id(id_fournisseur, id_produit):
    try:
        result = approvisionnementService().find_by_id(id_fournisseur, id_produit)
        return common_ressource.get_by_id(result, json_serializer)
    except Exception as e:
        return common_ressource.error_500(e)


@post('/api/approvisionnement')
def create():
    try:
        entity = common_ressource.body_from_json(json_serializer)
        result = approvisionnementService().insert(entity)
        return common_ressource.create(result, json_serializer)
    except Exception as e:
        return common_ressource.error_500(e)


@put('/api/approvisionnement/<id_fournisseur>/<id_produit>')
def update(id_fournisseur, id_produit):
    try:
        entity = common_ressource.body_from_json(json_serializer)
        entity.id_fournisseur = id_fournisseur
        entity.id_produit = id_produit
        result = approvisionnementService().update(entity)
        return common_ressource.update(result)
    except Exception as e:
        return common_ressource.error_500(e)


@put('/api/approvisionnement')
def save():
    try:
        entity = common_ressource.body_from_json(json_serializer)
        result = approvisionnementService().save(entity)
        return common_ressource.save(result, json_serializer, entity)
    except Exception as e:
        return common_ressource.error_500(e)


@delete('/api/approvisionnement/<id_fournisseur>/<id_produit>')
def delete(id_fournisseur, id_produit):
    try:
        result = approvisionnementService().delete_by_id(id_fournisseur, id_produit)
        return common_ressource.delete(result)
    except Exception as e:
        return common_ressource.error_500(e)


@get('/api/approvisionnement/count')
def count():
    try:
        result = approvisionnementService().count_all()
        return common_ressource.count(result)
    except Exception as e:
        print(e)
        response.status = 400
