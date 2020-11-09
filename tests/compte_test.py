# Python class for unit test of Client
import datetime
import unittest

from entities.compte import Compte
from dao.compte_dao import CompteDao

compte_dao = CompteDao()


class TestDaoCompte(unittest.TestCase):

    def test_dao(self):
        print("--- test ClientPersistence ")
        entity = Compte(1, 5,  datetime.date(1011, 11, 11), "test@gmail.com", "monpass", "myToken")

        print("Delete : {}".format(entity.to_dict()))
        compte_dao.delete(entity)
        cpt_initial = compte_dao.count_all()
        print("Initial count = {}".format(cpt_initial))

        print("Create : {}".format(entity))
        compte_dao.insert(entity)
        self.assertTrue(compte_dao.exists_by_id(1))
        self.assertTrue(compte_dao.exists(entity))

        cpt = compte_dao.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        print("Find by id ...")
        element = compte_dao.find_by_id(1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(compte_dao.exists(entity))
        print("Found : {}".format(element))

        entity.id_compte = 8
        entity.date_creation = datetime.date(1012, 11, 11)
        entity.email = "updateemail@gmail.com"
        entity.password = "mynewpassword"
        entity.token = "mynewtoken"

        element = compte_dao.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = compte_dao.find_by_id(1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = compte_dao.delete_by_id(1)
        self.assertEqual(element, 1)
        self.assertEqual(compte_dao.delete_by_id(1), False)
        self.assertEqual(compte_dao.delete(entity), 0)

        cpt_final = compte_dao.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(compte_dao.exists_by_id(1))
        self.assertFalse(compte_dao.exists(entity))
        self.assertEqual(compte_dao.find_by_id(1), None)

        print("Normal end of persistence service test.")
