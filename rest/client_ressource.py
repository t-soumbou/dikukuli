from services.client_service import ClientService as clientService
from jsonconv.entity_json_serializer import ClientJsonSerializer as json_serializer
from bottle import get, post, put, delete, response
from rest import common_ressource
import hashlib


@get('/api/clients')
def get_all():
    try:
        entities = clientService().find_all()
        return common_ressource.get_all(json_serializer, entities)
    except Exception as e:
        return common_ressource.error_500(e)


@get('/api/client/<id_client>')
def get_by_id(id_client):
    try:
        result = clientService().find_by_id(id_client)
        return common_ressource.get_by_id(result, json_serializer)
    except Exception as e:
        return common_ressource.error_500(e)


@post('/api/client')
def create():
    try:
        entity = common_ressource.body_from_json(json_serializer)
        phone = entity.tel
        is_phone_exist = clientService.exists_by_phone(phone)
        password = entity.password
        if is_phone_exist:
            from util import utils
            token = str(utils.random_with_N_digits(4))
            encrypt = hashlib.md5(password.encode('utf8')).hexdigest()
            entity.password = encrypt
            entity.token = token
            result = clientService().insert(entity)
            text = 'Entrez le code suivant pour confirmer votre inscription: '
            utils.sendConfirmSMS(phone, text, token)
            return common_ressource.create(result, json_serializer)
    except Exception as e:
        return common_ressource.error_500(e)


@post('/api/auth')
def auth():
    try:
        credentials = common_ressource.body_from_json(json_serializer)
        password = credentials.password
        phone = credentials.tel
        encrypt = hashlib.md5(password.encode('utf8')).hexdigest()
        entity = clientService.find_by_phone(phone)
        if entity.token == '1' and entity.password == encrypt:
            return common_ressource.get_by_id(entity, json_serializer)
    except Exception as e:
        return common_ressource.error_500(e)


@get('/api/valid/<id_client>/<token>')
def valid_token(id_client, token):
    try:
        is_valid = clientService.valid_token(id_client, token)
        return common_ressource.update(is_valid)
    except Exception as e:
        return common_ressource.error_500(e)


@put('/api/client/<id_client>')
def update(id_client):
    try:
        entity = common_ressource.body_from_json(json_serializer)
        entity.id_client = id_client
        result = clientService().update(entity)
        return common_ressource.update(result)
    except Exception as e:
        return common_ressource.error_500(e)


@put('/api/client')
def save():
    try:
        entity = common_ressource.body_from_json(json_serializer)
        result = clientService().save(entity)
        return common_ressource.save(result, json_serializer, entity)
    except Exception as e:
        return common_ressource.error_500(e)


@delete('/api/client/<id_client>')
def delete(id_client):
    try:
        result = clientService().delete_by_id(id_client)
        return common_ressource.delete(result)
    except Exception as e:
        return common_ressource.error_500(e)


@get('/api/client/count')
def count():
    try:
        result = clientService().count_all()
        return common_ressource.count(result)
    except Exception as e:
        print(e)
        response.status = 400
