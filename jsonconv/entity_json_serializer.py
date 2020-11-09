import json
import datetime
from entities.stock import Stock
from entities.produit_commande import Produit_Commande
from entities.produit import Produit
from entities.fournisseur import Fournisseur
from entities.client import Client
from entities.facture_details import Facture_Details
from entities.facture import Facture
from entities.compte import Compte
from entities.commande import Commande
from entities.approvisionnement import Approvisionnement


class StockJsonSerializer(object):
    def to_json(self, entity: Stock):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json
        """
        return {
            "id_produit": entity.id_produit,
            "id_stock": entity.id_stock,
            "date_modification": str(entity.date_modification),
            "quantite": entity.quantite
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Stock()
        entity.id_produit = data['id_produit']
        entity.id_stock = data['id_stock']
        entity.quantite = data['quantite']
        entity.date_modification = datetime.datetime.strptime(data['date_modification'], "%Y-%m-%d %H:%M:%S")

        return entity


class ProduitCommandeJsonSerializer(object):
    def to_json(self, entity: Produit_Commande):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json
        """
        return {
            "id_produit": entity.id_produit,
            "id_commande": entity.id_commande,
            "quantite": entity.quantite,
            "details": entity.details,
            "tva": entity.tva,
            "prix": entity.prix
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Produit_Commande()
        entity.id_produit = data['id_produit']
        entity.id_commande = data['id_commande']
        entity.quantite = data['quantite']
        entity.tva = data['tva']
        entity.prix = data['prix']
        entity.details = data['details']

        return entity


class ProduitJsonSerializer(object):
    def to_json(self, entity: Produit):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json
        """
        return {
            "id_produit": entity.id_produit,
            "nom_produit": entity.nom_produit,
            "category": entity.category,
            "desc_produit": entity.desc_produit,
            "tva": entity.tva,
            "prix": entity.prix,
            "capacite_produit": entity.capacite_produit,
            "genre": entity.genre
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Produit()
        entity.id_produit = data['id_produit']
        entity.nom_produit = data['nom_produit']
        entity.category = data['category']
        entity.tva = data['tva']
        entity.prix = data['prix']
        entity.desc_produit = data['desc_produit']
        entity.capacite_produit = data['capacite_produit']
        entity.genre = data["genre"]

        return entity


class FournisseurJsonSerializer(object):
    def to_json(self, entity: Fournisseur):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json
        """
        return {
            "pays": entity.pays,
            "prenom": entity.prenom,
            "zipcode": entity.zipcode,
            "ville": entity.ville,
            "addresse": entity.addresse,
            "tel": entity.tel,
            "nom": entity.nom,
            "id_fournisseur": entity.id_fournisseur
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Fournisseur()
        entity.id_fournisseur = data['id_fournisseur']
        entity.nom = data['nom']
        entity.prenom = data['prenom']
        entity.tel = data['tel']
        entity.addresse = data['addresse']
        entity.pays = data['pays']
        entity.zipcode = data['zipcode']
        entity.ville = data["ville"]

        return entity


class ClientJsonSerializer(object):
    def to_json(self, entity: Client):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json
        """
        return {
            "pays": entity.pays,
            "prenom": entity.prenom,
            "zipcode": entity.zipcode,
            "ville": entity.ville,
            "addresse": entity.addresse,
            "tel": entity.tel,
            "nom": entity.nom,
            "id_client": entity.id_client,
            "genre": entity.genre
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Client()
        entity.id_client = data['id_client']
        entity.nom = data['nom']
        entity.prenom = data['prenom']
        entity.tel = data['tel']
        entity.addresse = data['addresse']
        entity.pays = data['pays']
        entity.zipcode = data['zipcode']
        entity.ville = data["ville"]
        entity.genre = data['genre']

        return entity


class FactureDetailsJsonSerializer(object):
    def to_json(self, entity: Facture_Details):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json
        """
        return {
            "details": entity.details,
            "id_commande": entity.id_commande,
            "id_produit": entity.id_produit,
            "id_facture": entity.id_facture
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Facture_Details()
        entity.id_facture = data['id_facture']
        entity.id_produit = data['id_produit']
        entity.id_commande = data['id_commande']
        entity.details = data['details']

        return entity


class FactureJsonSerializer(object):
    def to_json(self, entity: Facture):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json
        """
        return {
            "details": entity.details,
            "id_commande": entity.id_commande,
            "date_facture": str(entity.date_facture),
            "id_facture": entity.id_facture
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Facture()
        entity.id_facture = data['id_facture']
        entity.date_facture = datetime.datetime.strptime(data['date_facture'], "%Y-%m-%d %H:%M:%S")
        entity.id_commande = data['id_commande']
        entity.details = data['details']

        return entity


class CompteJsonSerializer(object):
    def to_json(self, entity: Compte):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json
        """
        return {
            "id_client": entity.id_client,
            "id_compte": entity.id_compte,
            "date_creation": str(entity.date_creation),
            "email": entity.email,
            "password": entity.password,
            "token": entity.token,
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Compte()
        entity.id_client = data['id_client']
        entity.date_creation = datetime.datetime.strptime(data['date_creation'], "%Y-%m-%d %H:%M:%S")
        entity.email = data['email']
        entity.password = data['password']
        entity.token = data['token']

        return entity


class CommandeJsonSerializer(object):
    def to_json(self, entity: Commande):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json
        """
        return {
            "id_client": entity.id_client,
            "id_commande": entity.id_commande,
            "date_commande": str(entity.date_commande),
            "commande_details": entity.commande_details
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Commande()
        entity.id_client = data['id_client']
        entity.id_commande = data['id_commande']
        entity.date_commande = datetime.datetime.strptime(data['date_commande'], "%Y-%m-%d %H:%M:%S")
        entity.commande_details = data['commande_details']

        return entity


class ApprovisionnementJsonSerializer(object):
    def to_json(self, entity: Approvisionnement):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json
        """
        return {
            "id_fournisseur": entity.id_fournisseur,
            "id_produit": entity.id_produit,
            "quantite": entity.quantite,
            "date_commande": str(entity.date_commande),
            "date_arrive": str(entity.date_arrive),
            "status": entity.status
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Approvisionnement()
        entity.id_fournisseur = data['id_fournisseur']
        entity.id_produit = data['id_produit']
        entity.date_commande = datetime.datetime.strptime(data['date_commande'], "%Y-%m-%d %H:%M:%S")
        entity.date_arrive = datetime.datetime.strptime(data['date_arrive'], "%Y-%m-%d %H:%M:%S")
        entity.quantite = data['quantite']
        entity.status = data['status']

        return entity
