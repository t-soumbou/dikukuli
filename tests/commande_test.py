# Python class for unit test of Client
import datetime
import unittest

from entities.commande import Commande
from dao.commande_dao import CommandeDao

commande_dao = CommandeDao()


class TestDaoCommande(unittest.TestCase):

    def test_dao(self):
        print("--- test ClientPersistence ")
        entity = Commande(1, 2, datetime.date(1011, 11, 11), "details de la commande")

        print("Delete : {}".format(entity.to_dict()))
        commande_dao.delete(entity)
        cpt_initial = commande_dao.count_all()
        print("Initial count = {}".format(cpt_initial))

        print("Create : {}".format(entity))
        commande_dao.insert(entity)
        self.assertTrue(commande_dao.exists_by_id(1, 2))
        self.assertTrue(commande_dao.exists(entity))

        cpt = commande_dao.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        print("Find by id ...")
        element = commande_dao.find_by_id(1, 2)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(commande_dao.exists(entity))
        print("Found : {}".format(element))

        entity.date_commande = datetime.date(1011, 11, 11)
        entity.commande_details = "commande details test update"

        element = commande_dao.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = commande_dao.find_by_id(1, 2)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = commande_dao.delete_by_id(1, 2)
        self.assertEqual(element, 1)
        self.assertEqual(commande_dao.delete_by_id(1, 2), False)
        self.assertEqual(commande_dao.delete(entity), 0)

        cpt_final = commande_dao.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(commande_dao.exists_by_id(1, 2))
        self.assertFalse(commande_dao.exists(entity))
        self.assertEqual(commande_dao.find_by_id(1, 2), None)

        print("Normal end of persistence service test.")
