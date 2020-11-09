# Python class for unit test of Client
import datetime
import unittest

from entities.approvisionnement import Approvisionnement
from dao.approvisionnement_dao import ApprovisionnementDao

approvisionemment_dao = ApprovisionnementDao()


class TestDaoApprovisionnement(unittest.TestCase):

    def test_dao(self):
        print("--- test ApprovisionnementPersistence ")
        entity = Approvisionnement(1, 3, 10, datetime.date(1011, 11, 11), datetime.date(1011, 11, 12), "en cours")

        print("Delete : {}".format(entity.to_dict()))
        approvisionemment_dao.delete(entity)
        cpt_initial = approvisionemment_dao.count_all()
        print("Initial count = {}".format(cpt_initial))

        print("Create : {}".format(entity))
        approvisionemment_dao.insert(entity)
        self.assertTrue(approvisionemment_dao.exists_by_id(1, 3))
        self.assertTrue(approvisionemment_dao.exists(entity))

        cpt = approvisionemment_dao.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        print("Find by id ...")
        element = approvisionemment_dao.find_by_id(1, 3)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(approvisionemment_dao.exists(entity))
        print("Found : {}".format(element))

        entity.quantite = 19
        entity.date_commande = datetime.date(1012, 11, 11)
        entity.date_arrive = datetime.date(1012, 11, 12)
        entity.status = "livré"

        element = approvisionemment_dao.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = approvisionemment_dao.find_by_id(1, 3)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = approvisionemment_dao.delete_by_id(1, 3)
        self.assertEqual(element, 1)
        self.assertEqual(approvisionemment_dao.delete_by_id(1, 3), False)
        self.assertEqual(approvisionemment_dao.delete(entity), 0)

        cpt_final = approvisionemment_dao.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(approvisionemment_dao.exists_by_id(1, 3))
        self.assertFalse(approvisionemment_dao.exists(entity))
        self.assertEqual(approvisionemment_dao.find_by_id(1, 3), None)

        print("Normal end of persistence service test.")
