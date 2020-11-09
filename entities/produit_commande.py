# Python class for entity produit_commande

from commons.data_provider import Base


class Produit_Commande(Base):
    __tablename__ = 'produit_commande'
    __table_args__ = {'autoload': True}

    def __init__(self, id_produit, id_commande, quantite, prix, tva, details):
        """
        Init the table
        """
        self.id_produit = id_produit
        self.id_commande = id_commande
        self.quantite = quantite
        self.prix = prix
        self.tva = tva
        self.details = details

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "id_produit": self.id_produit,
            "id_commande": self.id_commande,
            "quantite": self.quantite,
            "prix": self.prix,
            "tva": self.tva,
            "details": self.details
        }
