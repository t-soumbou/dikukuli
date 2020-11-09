# Python class for entity compte

from commons.data_provider import Base


class Compte(Base):
    __tablename__ = 'compte'
    __table_args__ = {'autoload': True}

    def __init__(self, id_client, id_compte, date_creation, email, password, token):
        """
        Init the table
        """
        self.id_client = id_client
        self.id_compte = id_compte
        self.date_creation = date_creation
        self.email = email
        self.password = password
        self.token = token

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "id_client": self.id_client,
            "id_compte": self.id_compte,
            "date_creation": self.date_creation,
            "email": self.email,
            "password": self.password,
            "token": self.token
        }
