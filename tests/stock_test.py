# Python class for unit test of Client
import datetime
import unittest

from entities.stock import Stock
from dao.stock_dao import StockDao

stock_dao = StockDao()


class TestDaoCompte(unittest.TestCase):

    def test_dao(self):
        print("--- test ClientPersistence ")
        entity = Stock(1, 5, 100,  datetime.date(1011, 11, 11))

        print("Delete : {}".format(entity.to_dict()))
        stock_dao.delete(entity)
        cpt_initial = stock_dao.count_all()
        print("Initial count = {}".format(cpt_initial))

        print("Create : {}".format(entity))
        stock_dao.insert(entity)
        self.assertTrue(stock_dao.exists_by_id(1))
        self.assertTrue(stock_dao.exists(entity))

        cpt = stock_dao.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        print("Find by id ...")
        element = stock_dao.find_by_id(1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(stock_dao.exists(entity))
        print("Found : {}".format(element))

        self.id_produit = 12
        self.quantite = 210
        self.date_modification = datetime.date(1012, 11, 11)

        element = stock_dao.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = stock_dao.find_by_id(1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = stock_dao.delete_by_id(1)
        self.assertEqual(element, 1)
        self.assertEqual(stock_dao.delete_by_id(1), False)
        self.assertEqual(stock_dao.delete(entity), 0)

        cpt_final = stock_dao.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(stock_dao.exists_by_id(1))
        self.assertFalse(stock_dao.exists(entity))
        self.assertEqual(stock_dao.find_by_id(1), None)

        print("Normal end of persistence service test.")
