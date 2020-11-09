# Python class for service of Client

from entities.client import Client
from dao.commons import common_dao
from sqlalchemy import text


class ClientDao(object):
    def __init__(self):
        self.entity_class = Client

    def find_all(self):
        return common_dao.find_all(self.entity_class)

    def find_by_id(self, id_client):
        query = self.build_query(id_client)
        return common_dao.find(self.entity_class, query)

    def find_by_phone(self, phone):
        query = self.build_query_phone(phone)
        return common_dao.find(self.entity_class, query)

    def insert(self, entity):
        query = self.build_query(entity.id_client)
        if common_dao.exists(self.entity_class, query):
            return False
        else:
            return common_dao.insert(entity)

    def update(self, entity):
        query = self.build_query(entity.id_client)
        if common_dao.exists(self.entity_class, query):
            return common_dao.update(self.entity_class, entity, query)
        else:
            return False

    def save(self, entity):
        query = self.build_query(entity.id_client)
        if common_dao.exists(self.entity_class, query):
            return {
                'entity': common_dao.update(self.entity_class, entity, query),
                'isNew': False
            }
        else:
            return {
                'entity': common_dao.insert(entity),
                'isNew': True
            }

    def delete_by_id(self, id_client):
        query = self.build_query(id_client)
        if common_dao.exists(self.entity_class, query):
            return common_dao.delete(self.entity_class, query)
        else:
            return False

    def delete(self, entity):
        query = self.build_query(entity.id_client)
        if common_dao.exists(self.entity_class, query):
            return common_dao.delete(self.entity_class, query)
        else:
            return False

    def exists_by_id(self, id_client):
        query = self.build_query(id_client)
        return common_dao.exists(self.entity_class, query)

    def exists(self, entity):
        query = self.build_query(entity.id_client)
        return common_dao.exists(self.entity_class, query)

    def count_all(self):
        return common_dao.count_all(self.entity_class)

    def exists_by_phone(self, tel):
        query = self.build_query_phone(tel)
        return common_dao.exists(self.entity_class, query)

    def valid_token(self, id_client, token):
        entity = self.find_by_id(id_client)
        valid = False
        if entity.token == token:
            entity.token = '1'
            valid = self.update(entity)
        return valid

    def build_query(self, id_client):
        """
        SQLAlchemy query
        """
        return text("Client.id_client ={}".format(id_client))

    def build_query_phone(self, phone):
        """
        SQLAlchemy query
        """
        return text("Client.tel ={}".format(phone))
