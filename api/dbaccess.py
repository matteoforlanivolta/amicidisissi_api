# Progetto Amici Di Sissi
# dbaccess.py
# Codice per la lettura e scrittura dal database

import psycopg2
from place import Place
from adslogging import ADSLogger

class DBAccess:
    connection = None
    cursor = None
    is_open = False

    # Apre la connessione al database.
    # I parametri sono quelli necessari per l'accesso ad un database postgresql
    # (Nome database, nome utente, password database, host del database)
    @staticmethod
    def open(dbname: str, user: str, password: str, host: str):
        ADSLogger.log(f"Opening DB connection to {host}")
        DBAccess.connection = psycopg2.connect(f"host={host} dbname={dbname} user={user} password={password}")
        DBAccess.cursor = DBAccess.connection.cursor()
        DBAccess.is_open = True

    # Query di una entry del database
    # Ritorna una tuple di valori (nome, lat., long., accessibilita', link immagine)
    @staticmethod
    def getplace(name: str):
        if DBAccess.is_open:
            DBAccess.cursor.execute("SELECT * FROM places WHERE name=%s;", (name,))
            ADSLogger.log(f"Queried place {name}")
            return DBAccess.cursor.fetchone()
        else:
            ADSLogger.error("Connection to database attempted, but it's closed!")
            return None

    # Query di tutte le entry del database
    @staticmethod
    def getallplaces():
        if DBAccess.is_open:
            DBAccess.cursor.execute("SELECT * FROM places;")
            ADSLogger.log("Queried all places")
            return DBAccess.cursor.fetchall()
        else:
            ADSLogger.error("Connection to database attempted, but it's closed!")

    # Chiude la connessione al database
    @staticmethod
    def close():
        ADSLogger.log("Closing DB connection!")
        DBAccess.connection.close()
        DBAccess.is_open = False