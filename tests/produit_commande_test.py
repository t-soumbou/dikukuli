# Python class for unit test of Client
import unittest

from entities.produit_commande import Produit_Commande
from dao.produit_commande_dao import ProduitCommandeDao

produit_commande_dao = ProduitCommandeDao()


class TestDaoProduitCommande(unittest.TestCase):

    def test_dao(self):
        print("--- test ApprovisionnementPersistence ")
        entity = Produit_Commande(1, 3, 110, 200, 2.3, "my details")

        print("Delete : {}".format(entity.to_dict()))
        produit_commande_dao.delete(entity)
        cpt_initial = produit_commande_dao.count_all()
        print("Initial count = {}".format(cpt_initial))

        print("Create : {}".format(entity))
        produit_commande_dao.insert(entity)
        self.assertTrue(produit_commande_dao.exists_by_id(1, 3))
        self.assertTrue(produit_commande_dao.exists(entity))

        cpt = produit_commande_dao.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        print("Find by id ...")
        element = produit_commande_dao.find_by_id(1, 3)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(produit_commande_dao.exists(entity))
        print("Found : {}".format(element))

        self.quantite = 210
        self.prix = 290
        self.tva = 5.2
        self.details = "my new details"

        element = produit_commande_dao.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = produit_commande_dao.find_by_id(1, 3)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = produit_commande_dao.delete_by_id(1, 3)
        self.assertEqual(element, 1)
        self.assertEqual(produit_commande_dao.delete_by_id(1, 3), False)
        self.assertEqual(produit_commande_dao.delete(entity), 0)

        cpt_final = produit_commande_dao.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(produit_commande_dao.exists_by_id(1, 3))
        self.assertFalse(produit_commande_dao.exists(entity))
        self.assertEqual(produit_commande_dao.find_by_id(1, 3), None)

        print("Normal end of persistence service test.")
