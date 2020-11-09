# Python class for managing database

import sqlite3
from sqlite3 import Error
from commons.config import database_file


def create_db(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Database created, version = ", sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()


def exec_sql(sql):
    conn = sqlite3.connect(database_file)

    c = conn.cursor()

    # Create table
    c.execute(sql)

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
