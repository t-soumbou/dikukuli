# Python class for unit test of Client

import unittest

from entities.produit import Produit
from dao.produit_dao import ProduitDao

produit_dao = ProduitDao()


class TestDaoProduit(unittest.TestCase):

    def test_dao(self):
        print("--- test ClientPersistence ")
        entity = Produit(1, "Dikukuli", 100, 3.9, "100 ml", "my desc produit", "H", "parfum")

        print("Delete : {}".format(entity.to_dict()))
        produit_dao.delete(entity)
        cpt_initial = produit_dao.count_all()
        print("Initial count = {}".format(cpt_initial))

        print("Create : {}".format(entity))
        produit_dao.insert(entity)
        self.assertTrue(produit_dao.exists_by_id(1))
        self.assertTrue(produit_dao.exists(entity))

        cpt = produit_dao.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        print("Find by id ...")
        element = produit_dao.find_by_id(1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(produit_dao.exists(entity))
        print("Found : {}".format(element))

        entity.nom_produit = "my new name"
        self.prix = 110
        self.tva = 1.9
        self.capacite_produit = "110 ml"
        self.desc_produit = "my new desc produit"

        element = produit_dao.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = produit_dao.find_by_id(1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = produit_dao.delete_by_id(1)
        self.assertEqual(element, 1)
        self.assertEqual(produit_dao.delete_by_id(1), False)
        self.assertEqual(produit_dao.delete(entity), 0)

        cpt_final = produit_dao.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(produit_dao.exists_by_id(1))
        self.assertFalse(produit_dao.exists(entity))
        self.assertEqual(produit_dao.find_by_id(1), None)

        print("Normal end of persistence service test.")
