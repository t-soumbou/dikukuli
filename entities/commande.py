# Python class for entity commande

from commons.data_provider import Base


class Commande(Base):
    __tablename__ = 'commande'
    __table_args__ = {'autoload': True}

    def __init__(self, id_client, id_commande, date_commande, commande_details):
        """
        Init the table
        """
        self.id_client = id_client
        self.id_commande = id_commande
        self.date_commande = date_commande
        self.commande_details = commande_details

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "id_client": self.id_client,
            "id_commande": self.id_commande,
            "date_commande": self.date_commande,
            "commande_details": self.commande_details
        }
