# Python class for unit test of Client

import unittest

from entities.fournisseur import Fournisseur
from dao.fournisseur_dao import FournisseurDao

fournisseur_dao = FournisseurDao()


class TestDaoFournisseur(unittest.TestCase):

    def test_dao(self):
        print("--- test ClientPersistence ")
        entity = Fournisseur(1, "Dikukuli", "papillon", "0790504676", "12 rue du Papillon", "Gabon", "lbv", "7614")

        print("Delete : {}".format(entity.to_dict()))
        fournisseur_dao.delete(entity)
        cpt_initial = fournisseur_dao.count_all()
        print("Initial count = {}".format(cpt_initial))

        print("Create : {}".format(entity))
        fournisseur_dao.insert(entity)
        self.assertTrue(fournisseur_dao.exists_by_id(1))
        self.assertTrue(fournisseur_dao.exists(entity))

        cpt = fournisseur_dao.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        print("Find by id ...")
        element = fournisseur_dao.find_by_id(1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(fournisseur_dao.exists(entity))
        print("Found : {}".format(element))

        entity.nom = "Papillon"
        entity.prenom = "Dikulili"
        entity.tel = "001122334455"
        entity.addresse = "4 rue de Paris"
        entity.pays = "France"
        entity.ville = "Paris"
        entity.zipcode = "1309"

        element = fournisseur_dao.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = fournisseur_dao.find_by_id(1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = fournisseur_dao.delete_by_id(1)
        self.assertEqual(element, 1)
        self.assertEqual(fournisseur_dao.delete_by_id(1), False)
        self.assertEqual(fournisseur_dao.delete(entity), 0)

        cpt_final = fournisseur_dao.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(fournisseur_dao.exists_by_id(1))
        self.assertFalse(fournisseur_dao.exists(entity))
        self.assertEqual(fournisseur_dao.find_by_id(1), None)

        print("Normal end of persistence service test.")
