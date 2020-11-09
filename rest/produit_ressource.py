from services.produit_service import ProduitService as produitService
from jsonconv.entity_json_serializer import ProduitJsonSerializer as json_serializer
from bottle import get, post, put, delete, response
from rest import common_ressource


@get('/api/produits')
def get_all():
    try:
        entities = produitService().find_all()
        return common_ressource.get_all(json_serializer, entities)
    except Exception as e:
        return common_ressource.error_500(e)


@get('/api/produit/<id_produit>')
def get_by_id(id_produit):
    try:
        result = produitService().find_by_id(id_produit)
        return common_ressource.get_by_id(result, json_serializer)
    except Exception as e:
        return common_ressource.error_500(e)


@post('/api/produit')
def create():
    try:
        entity = common_ressource.body_from_json(json_serializer)
        result = produitService().insert(entity)
        return common_ressource.create(result, json_serializer)
    except Exception as e:
        return common_ressource.error_500(e)


@put('/api/produit/<id_produit>')
def update(id_produit):
    try:
        entity = common_ressource.body_from_json(json_serializer)
        entity.id_produit = id_produit
        result = produitService().update(entity)
        return common_ressource.update(result)
    except Exception as e:
        return common_ressource.error_500(e)


@put('/api/produit')
def save():
    try:
        entity = common_ressource.body_from_json(json_serializer)
        result = produitService().save(entity)
        return common_ressource.save(result, json_serializer, entity)
    except Exception as e:
        return common_ressource.error_500(e)


@delete('/api/produit/<id_produit>')
def delete(id_produit):
    try:
        result = produitService().delete_by_id(id_produit)
        return common_ressource.delete(result)
    except Exception as e:
        return common_ressource.error_500(e)


@get('/api/produit/count')
def count():
    try:
        result = produitService().count_all()
        return common_ressource.count(result)
    except Exception as e:
        print(e)
        response.status = 400
