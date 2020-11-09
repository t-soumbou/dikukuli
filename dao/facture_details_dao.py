# Python class for service of facture

from entities.facture_details import Facture_Details
from dao.commons import common_dao
from sqlalchemy import text


class FactureDetailsDao(object):
    def __init__(self):
        self.entity_class = Facture_Details

    def find_all(self):
        return common_dao.find_all(self.entity_class)

    def find_by_id(self, id_produit, id_commande, id_facture):
        query = self.build_query(id_produit, id_commande, id_facture)
        return common_dao.find(self.entity_class, query)

    def insert(self, entity):
        query = self.build_query(entity.id_produit, entity.id_commande, entity.id_facture)
        if common_dao.exists(self.entity_class, query):
            return False
        else:
            return common_dao.insert(entity)

    def update(self, entity):
        query = self.build_query(entity.id_produit, entity.id_commande, entity.id_facture)
        if common_dao.exists(self.entity_class, query):
            return common_dao.update(self.entity_class, entity, query)
        else:
            return False

    def save(self, entity):
        query = self.build_query(entity.id_produit, entity.id_commande, entity.id_facture)
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

    def delete_by_id(self, id_produit, id_commande, id_facture):
        query = self.build_query(id_produit, id_commande, id_facture)
        if common_dao.exists(self.entity_class, query):
            return common_dao.delete(self.entity_class, query)
        else:
            return False

    def delete(self, entity):
        query = self.build_query(entity.id_produit, entity.id_commande, entity.id_facture)
        if common_dao.exists(self.entity_class, query):
            return common_dao.delete(self.entity_class, query)
        else:
            return False

    def exists_by_id(self, id_produit, id_commande, id_facture):
        query = self.build_query(id_produit, id_commande, id_facture)
        return common_dao.exists(self.entity_class, query)

    def exists(self, entity):
        query = self.build_query(entity.id_produit, entity.id_commande, entity.id_facture)
        return common_dao.exists(self.entity_class, query)

    def count_all(self):
        return common_dao.count_all(self.entity_class)

    def build_query(self, id_produit, id_commande, id_facture):
        """
        SQLAlchemy query
        """
        return text("Facture_Details.id_produit ={} and Facture_Details.id_facture and Facture_Details.id_commande".format(id_produit, id_commande, id_facture))
