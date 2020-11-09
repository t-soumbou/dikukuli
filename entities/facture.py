# Python class for entity facture

from commons.data_provider import Base


class Facture(Base):
    __tablename__ = 'facture'
    __table_args__ = {'autoload': True}

    def __init__(self, id_facture, id_commande, date_facture, details):
        """
        Init the table
        """
        self.id_facture = id_facture
        self.id_commande = id_commande
        self.date_facture = date_facture
        self.details = details

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "id_facture": self.id_facture,
            "id_commande": self.id_commande,
            "date_facture": self.date_facture,
            "details": self.details
        }
