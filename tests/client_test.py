# Python class for unit test of Client

import unittest

from entities.client import Client
from dao.client_dao import ClientDao

client_dao = ClientDao()


class TestDaoClient(unittest.TestCase):

    def test_dao(self):
        print("--- test ClientPersistence ")
        entity = Client(1, "Dikukuli", "papillon", "0790504676", "12 rue du Papillon", "Gabon", "lbv", "7614", "M")

        print("Delete : {}".format(entity.to_dict()))
        client_dao.delete(entity)
        cpt_initial = client_dao.count_all()
        print("Initial count = {}".format(cpt_initial))

        print("Create : {}".format(entity))
        client_dao.insert(entity)
        self.assertTrue(client_dao.exists_by_id(1))
        self.assertTrue(client_dao.exists(entity))

        cpt = client_dao.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        print("Find by id ...")
        element = client_dao.find_by_id(1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(client_dao.exists(entity))
        print("Found : {}".format(element))

        entity.NOM = "Papillon"
        entity.PRENOM = "Dikulili"
        entity.TEL = "001122334455"
        entity.ADRESSE = "4 rue de Paris"
        entity.PAYS = "France"
        entity.VILLE = "Paris"
        entity.ZIPCODE = "1309"
        entity.GENRE = "M"

        element = client_dao.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = client_dao.find_by_id(1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = client_dao.delete_by_id(1)
        self.assertEqual(element, 1)
        self.assertEqual(client_dao.delete_by_id(1), False)
        self.assertEqual(client_dao.delete(entity), 0)

        cpt_final = client_dao.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(client_dao.exists_by_id(1))
        self.assertFalse(client_dao.exists(entity))
        self.assertEqual(client_dao.find_by_id(1), None)

        print("Normal end of persistence service test.")
