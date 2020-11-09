from services.produit_commande_service import ProduitCommandeService as service
from jsonconv.entity_json_serializer import ProduitCommandeJsonSerializer as json_serializer
from bottle import get, post, put, delete, response
from rest import common_ressource


@get('/api/produitCommandes')
def get_all():
    try:
        entities = service().find_all()
        return common_ressource.get_all(json_serializer, entities)
    except Exception as e:
        return common_ressource.error_500(e)


@get('/api/produitCommande/<id_produit>/<id_commande>')
def get_by_id(id_produit, id_commande):
    try:
        result = service().find_by_id(id_produit, id_commande)
        return common_ressource.get_by_id(result, json_serializer)
    except Exception as e:
        return common_ressource.error_500(e)


@post('/api/produitCommande')
def create():
    try:
        entity = common_ressource.body_from_json(json_serializer)
        result = service().insert(entity)
        return common_ressource.create(result, json_serializer)
    except Exception as e:
        return common_ressource.error_500(e)


@put('/api/produitCommande/<id_produit>/<id_commande>')
def update(id_produit, id_commande):
    try:
        entity = common_ressource.body_from_json(json_serializer)
        entity.id_commande = id_commande
        entity.id_produit = id_produit
        result = service().update(entity)
        return common_ressource.update(result)
    except Exception as e:
        return common_ressource.error_500(e)


@put('/api/produitCommande')
def save():
    try:
        entity = common_ressource.body_from_json(json_serializer)
        result = service().save(entity)
        return common_ressource.save(result, json_serializer, entity)
    except Exception as e:
        return common_ressource.error_500(e)


@delete('/api/produitCommande/<id_produit>/<id_commande>')
def delete(id_produit, id_commande):
    try:
        result = service().delete_by_id(id_produit, id_commande)
        return common_ressource.delete(result)
    except Exception as e:
        return common_ressource.error_500(e)


@get('/api/produitCommande/count')
def count():
    try:
        result = service().count_all()
        return common_ressource.count(result)
    except Exception as e:
        print(e)
        response.status = 400
