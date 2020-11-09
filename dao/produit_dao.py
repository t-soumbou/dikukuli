# Python class for service of Produit

from entities.produit import Produit
from dao.commons import common_dao
from sqlalchemy import text


class ProduitDao(object):
    def __init__(self):
        self.entity_class = Produit

    def find_all(self):
        return common_dao.find_all(self.entity_class)

    def find_by_id(self, id_produit):
        query = self.build_query(id_produit)
        return common_dao.find(self.entity_class, query)

    def insert(self, entity):
        query = self.build_query(entity.id_produit)
        if common_dao.exists(self.entity_class, query):
            return False
        else:
            return common_dao.insert(entity)

    def update(self, entity):
        query = self.build_query(entity.id_produit)
        if common_dao.exists(self.entity_class, query):
            return common_dao.update(self.entity_class, entity, query)
        else:
            return False

    def save(self, entity):
        query = self.build_query(entity.id_produit)
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

    def delete_by_id(self, id_produit):
        query = self.build_query(id_produit)
        if common_dao.exists(self.entity_class, query):
            return common_dao.delete(self.entity_class, query)
        else:
            return False

    def delete(self, entity):
        query = self.build_query(entity.id_produit)
        if common_dao.exists(self.entity_class, query):
            return common_dao.delete(self.entity_class, query)
        else:
            return False

    def exists_by_id(self, id_produit):
        query = self.build_query(id_produit)
        return common_dao.exists(self.entity_class, query)

    def exists(self, entity):
        query = self.build_query(entity.id_produit)
        return common_dao.exists(self.entity_class, query)

    def count_all(self):
        return common_dao.count_all(self.entity_class)

    def build_query(self, id_produit):
        """
        SQLAlchemy query
        """
        return text("Produit.id_produit ={}".format(id_produit))
