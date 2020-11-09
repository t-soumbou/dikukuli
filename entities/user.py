# Python class for entity client

from commons.data_provider import Base


class User(Base):
    __tablename__ = 'User'
    __table_args__ = {'autoload': True}

    def __init__(self, id_client, nom, prenom, tel, addresse, pays, ville, zipcode, genre):
        """
        Init the table
        """
        self.id_client = id_client
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.addresse = addresse
        self.pays = pays
        self.ville = ville
        self.zipcode = zipcode
        self.genre = genre

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "id_client": self.id_client,
            "nom": self.nom,
            "prenom": self.prenom,
            "tel": self.tel,
            "addresse": self.addresse,
            "pays": self.pays,
            "ville": self.ville,
            "zipcode": self.zipcode,
            "genre": self.genre
        }
