# Python class for entity produit

from commons.data_provider import Base


class Produit(Base):
    __tablename__ = 'produit'
    __table_args__ = {'autoload': True}

    def __init__(self, id_produit, nom_produit, prix, tva, capacite_produit, desc_produit, genre, category):
        """
        Init the table
        """
        self.id_produit = id_produit
        self.nom_produit = nom_produit
        self.prix = prix
        self.tva = tva
        self.capacite_produit = capacite_produit
        self.desc_produit = desc_produit
        self.genre = genre
        self.category = category

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "id_produit": self.id_produit,
            "nom_produit": self.nom_produit,
            "prix": self.prix,
            "tva": self.tva,
            "capacite_produit": self.capacite_produit,
            "desc_produit": self.desc_produit,
            "genre": self.genre,
            "category": self.category
        }
