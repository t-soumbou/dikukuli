# Python class for create database connection

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import Engine
from sqlalchemy import event
from commons.config import database_url


class DataProvider(object):
    """
    Provide database session
    """

    def __init__(self):
        """
        Connect to a database and provide data managing
        """
        engine_connect = create_engine(database_url, echo=True)
        self.Session = sessionmaker(bind=engine_connect, expire_on_commit=False)
        self.metadata = MetaData(engine_connect)

    def new_session(self):
        """
        Get a new database connection
        :return: Database session
        """
        return self.Session()


# Initialize database and session
data_provider = DataProvider()

# Base : maping entity with database table
Base = declarative_base(metadata=data_provider.metadata)


@event.listens_for(Engine, "connect")
def set_pragma(db_connection, connection_record):
    """
    For SQLite database, activate foreign keys
    :param db_connection: Database connection
    :param connection_record:
    :return foreign keys turned on
    """
    cursor = db_connection.cursor()
    # Activate Foreign Keys
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
