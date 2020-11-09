# Python class for entity produit

from commons.data_provider import Base


class Stock(Base):
    __tablename__ = 'stock'
    __table_args__ = {'autoload': True}

    def __init__(self, id_stock, id_produit, quantite, date_modification):
        """
        Init the table
        """
        self.id_stock = id_stock
        self.id_produit = id_produit
        self.quantite = quantite
        self.date_modification = date_modification

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "id_stock": self.id_stock,
            "nom_produit": self.nom_produit,
            "quantite": self.quantite,
            "date_modification": self.date_modification
        }
