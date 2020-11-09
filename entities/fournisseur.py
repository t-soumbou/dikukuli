# Python class for entity fournisseur

from commons.data_provider import Base


class Fournisseur(Base):
    __tablename__ = 'fournisseur'
    __table_args__ = {'autoload': True}

    def __init__(self, id_fournisseur, nom, prenom, tel, addresse, pays, ville, zipcode):
        """
        Init the table
        """
        self.id_fournisseur = id_fournisseur
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.addresse = addresse
        self.pays = pays
        self.ville = ville
        self.zipcode = zipcode

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "id_fournisseur": self.id_fournisseur,
            "nom": self.nom,
            "prenom": self.prenom,
            "tel": self.tel,
            "addresse": self.addresse,
            "pays": self.pays,
            "ville": self.ville,
            "zipcode": self.zipcode,
        }
