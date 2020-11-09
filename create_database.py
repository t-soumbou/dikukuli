# Python class for init the database

from commons.config import database_file
from commons.database_managing import create_db
from commons.database_managing import exec_sql

if __name__ == '__main__':
    create_db(database_file)

    exec_sql('''PRAGMA foreign_keys=off;''')

    exec_sql('''
        create table CLIENT
            (
                id_client INT(32),
                nom       VARCHAR(32),
                prenom    VARCHAR(32),
                tel       VARCHAR(32)  not null,
                addresse   VARCHAR(32)  not null,
                pays      VARCHAR(32)  not null,
                ville     VARCHAR(32)  not null,
                zipcode   VARCHAR(32)  not null,
                genre     VARCHAR(32)  not null,
                primary key (id_client)
                
            );
    ''')
    print("Table Client : created")
    # end
    exec_sql('''PRAGMA foreign_keys=on;''')
