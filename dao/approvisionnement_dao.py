# Python class for service of Approvisionnement

from entities.approvisionnement import Approvisionnement
from dao.commons import common_dao
from sqlalchemy import text


class ApprovisionnementDao(object):
    def __init__(self):
        self.entity_class = Approvisionnement

    def find_all(self):
        return common_dao.find_all(self.entity_class)

    def find_by_id(self, id_fournisseur, id_produit):
        query = self.build_query(id_fournisseur, id_produit)
        return common_dao.find(self.entity_class, query)

    def insert(self, entity):
        query = self.build_query(entity.id_fournisseur, entity.id_produit)
        if common_dao.exists(self.entity_class, query):
            return False
        else:
            return common_dao.insert(entity)

    def update(self, entity):
        query = self.build_query(entity.id_fournisseur, entity.id_produit)
        if common_dao.exists(self.entity_class, query):
            return common_dao.update(self.entity_class, entity, query)
        else:
            return False

    def save(self, entity):
        query = self.build_query(entity.id_fournisseur, entity.id_produit)
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

    def delete_by_id(self, id_fournisseur, id_produit):
        query = self.build_query(id_fournisseur, id_produit)
        if common_dao.exists(self.entity_class, query):
            return common_dao.delete(self.entity_class, query)
        else:
            return False

    def delete(self, entity):
        query = self.build_query(entity.id_fournisseur, entity.id_produit)
        if common_dao.exists(self.entity_class, query):
            return common_dao.delete(self.entity_class, query)
        else:
            return False

    def exists_by_id(self, id_fournisseur, id_produit):
        query = self.build_query(id_fournisseur, id_produit)
        return common_dao.exists(self.entity_class, query)

    def exists(self, entity):
        query = self.build_query(entity.id_fournisseur, entity.id_produit)
        return common_dao.exists(self.entity_class, query)

    def count_all(self):
        return common_dao.count_all(self.entity_class)

    def build_query(self, id_fournisseur, id_produit):
        """
        SQLAlchemy query
        """
        return text("Approvisionnement.id_fournisseur ={} and Approvisionnement.id_produit "
                    .format(id_fournisseur, id_produit))
