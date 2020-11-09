from services.stock_service import StockService as stockService
from jsonconv.entity_json_serializer import StockJsonSerializer as json_serializer
from bottle import get, post, put, delete, response
from rest import common_ressource


@get('/api/stocks')
def get_all():
    try:
        entities = stockService().find_all()
        return common_ressource.get_all(json_serializer, entities)
    except Exception as e:
        return common_ressource.error_500(e)


@get('/api/stock/<id_stock>')
def get_by_id(id_stock):
    try:
        result = stockService().find_by_id(id_stock)
        return common_ressource.get_by_id(result, json_serializer)
    except Exception as e:
        return common_ressource.error_500(e)


@post('/api/stock')
def create():
    try:
        entity = common_ressource.body_from_json(json_serializer)
        result = stockService().insert(entity)
        return common_ressource.create(result, json_serializer)
    except Exception as e:
        return common_ressource.error_500(e)


@put('/api/stock/<id_stock>')
def update(id_stock):
    try:
        entity = common_ressource.body_from_json(json_serializer)
        entity.id_stock = id_stock
        result = stockService().update(entity)
        return common_ressource.update(result)
    except Exception as e:
        return common_ressource.error_500(e)


@put('/api/stock')
def save():
    try:
        entity = common_ressource.body_from_json(json_serializer)
        result = stockService().save(entity)
        return common_ressource.save(result, json_serializer, entity)
    except Exception as e:
        return common_ressource.error_500(e)


@delete('/api/stock/<id_stock>')
def delete(id_stock):
    try:
        result = stockService().delete_by_id(id_stock)
        return common_ressource.delete(result)
    except Exception as e:
        return common_ressource.error_500(e)


@get('/api/stock/count')
def count():
    try:
        result = stockService().count_all()
        return common_ressource.count(result)
    except Exception as e:
        print(e)
        response.status = 400
