# Python class for unit test of Client
import unittest

from entities.facture_details import Facture_Details
from dao.facture_details_dao import FactureDetailsDao

facture_details_dao = FactureDetailsDao()


class TestDaoFactureDetails(unittest.TestCase):

    def test_dao(self):
        print("--- test ApprovisionnementPersistence ")
        entity = Facture_Details(1, 3, 10, "my details")

        print("Delete : {}".format(entity.to_dict()))
        facture_details_dao.delete(entity)
        cpt_initial = facture_details_dao.count_all()
        print("Initial count = {}".format(cpt_initial))

        print("Create : {}".format(entity))
        facture_details_dao.insert(entity)
        self.assertTrue(facture_details_dao.exists_by_id(1, 3, 10))
        self.assertTrue(facture_details_dao.exists(entity))

        cpt = facture_details_dao.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        print("Find by id ...")
        element = facture_details_dao.find_by_id(1, 3, 10)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(facture_details_dao.exists(entity))
        print("Found : {}".format(element))

        entity.details = "my new details"

        element = facture_details_dao.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = facture_details_dao.find_by_id(1, 3, 10)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = facture_details_dao.delete_by_id(1, 3, 10)
        self.assertEqual(element, 1)
        self.assertEqual(facture_details_dao.delete_by_id(1, 3, 10), False)
        self.assertEqual(facture_details_dao.delete(entity), 0)

        cpt_final = facture_details_dao.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(facture_details_dao.exists_by_id(1, 3, 10))
        self.assertFalse(facture_details_dao.exists(entity))
        self.assertEqual(facture_details_dao.find_by_id(1, 3, 10), None)

        print("Normal end of persistence service test.")
