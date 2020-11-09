# Python class for entity facture_details

from commons.data_provider import Base


class Facture_Details(Base):
    __tablename__ = 'facture_details'
    __table_args__ = {'autoload': True}

    def __init__(self, id_produit, id_commande, id_facture, details):
        """
        Init the table
        """
        self.id_produit = id_produit
        self.id_commande = id_commande
        self.id_facture = id_facture
        self.details = details

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "id_produit": self.id_produit,
            "id_commande": self.id_commande,
            "id_facture": self.id_facture,
            "details": self.details
        }
