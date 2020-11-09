# Python class for unit test of Client
import datetime
import unittest

from entities.facture import Facture
from dao.facture_dao import FactureDao

facture_dao = FactureDao()


class TestDaoFacture(unittest.TestCase):

    def test_dao(self):
        print("--- test ClientPersistence ")
        entity = Facture(1, 5,  datetime.date(1011, 11, 11), "my facture details")

        print("Delete : {}".format(entity.to_dict()))
        facture_dao.delete(entity)
        cpt_initial = facture_dao.count_all()
        print("Initial count = {}".format(cpt_initial))

        print("Create : {}".format(entity))
        facture_dao.insert(entity)
        self.assertTrue(facture_dao.exists_by_id(1))
        self.assertTrue(facture_dao.exists(entity))

        cpt = facture_dao.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        print("Find by id ...")
        element = facture_dao.find_by_id(1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(facture_dao.exists(entity))
        print("Found : {}".format(element))

        entity.id_commande = 10
        entity.date_facture = datetime.date(1012, 11, 11)
        entity.details = "my new facture details"

        element = facture_dao.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = facture_dao.find_by_id(1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = facture_dao.delete_by_id(1)
        self.assertEqual(element, 1)
        self.assertEqual(facture_dao.delete_by_id(1), False)
        self.assertEqual(facture_dao.delete(entity), 0)

        cpt_final = facture_dao.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(facture_dao.exists_by_id(1))
        self.assertFalse(facture_dao.exists(entity))
        self.assertEqual(facture_dao.find_by_id(1), None)

        print("Normal end of persistence service test.")
