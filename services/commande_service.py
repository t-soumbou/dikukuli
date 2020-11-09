# Python class for service of Commande

from dao.commande_dao import CommandeDao


class CommandeService:
    def __init__(self):
        self.dao = CommandeDao()

    def find_by_id(self, id_commande):
        """
        Tries to find an entity using its Id / Primary Key
        :param id_commande: PK of the entity to find
        :return: False if entity not found, entity if found
        """
        return self.dao.find_by_id(id_commande)

    def find_all(self):
        """
        Finds all entities.
        :return:  all entities
        """
        return self.dao.find_all()

    def insert(self, entity):
        """
        Insert the given entity in the database
        :param entity: to be inserted (supposed to have a valid Id/PK )
        :return: false if not found, entity if found
        """
        return self.dao.insert(entity)

    def update(self, entity):
        """
        Updates the given entity in the database
        :param entity: to be updated (supposed to have a valid Id/PK )
        :return: true if entity updated, false if not found
        """
        return self.dao.update(entity)

    def save(self, entity):
        """
        Updates or creates the given entity in the database
        :param entity: to be updated or created (supposed to have a valid Id/PK )
        :return: json with isNew attribute (True if created) and entity (created or updated)
        """
        return self.dao.save(entity)

    def delete_by_id(self, id_commande):
        """
        Deletes an entity using its Id / Primary Key
        :param id_commande: PK of the entity to delete
        :return: true if the entity has been deleted, false if not found and not deleted
        """
        return self.dao.delete_by_id(id_commande)

    def delete(self, entity):
        """
        Deletes an entity
        :param entity: to delete
        :return: 1 if the entity has been deleted, 0 if not found and not deleted
        """
        return self.dao.delete(entity)

    def exists_by_id(self, id_commande):
        """
        Ckeck if an Id / Primary Key is in the entity table
        :param id_commande: PK to check in database
        :return: true or false
        """
        return self.dao.exists_by_id(id_commande)

    def exists(self, entity):
        """
        Ckeck if an entity is in the entity table
        :return: true or false
        """
        return self.dao.exists(entity)

    def count_all(self):
        """
        Counts all the entity present in the entity table
        :return: the number of rows in the entity table
        """
        return self.dao.count_all()
