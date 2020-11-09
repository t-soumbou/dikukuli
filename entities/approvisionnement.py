# Python class for entity approvisionnement

from commons.data_provider import Base


class Approvisionnement(Base):
    __tablename__ = 'approvisionnement'
    __table_args__ = {'autoload': True}

    def __init__(self, id_fournisseur, id_produit, quantite, date_commande, date_arrive, status):
        """
        Init the table
        """
        self.id_fournisseur = id_fournisseur
        self.id_produit = id_produit
        self.quantite = quantite
        self.date_commande = date_commande
        self.date_arrive = date_arrive
        self.status = status

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "id_fournisseur": self.id_fournisseur,
            "id_produit": self.id_produit,
            "quantite": self.quantite,
            "date_commande": self.date_commande,
            "date_arrive": self.date_arrive,
            "status": self.status
        }
