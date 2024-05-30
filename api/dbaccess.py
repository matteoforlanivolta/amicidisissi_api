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

    @staticmethod
    def open(dbname: str, user: str, password: str, host: str):
        ADSLogger.log(f"Opening DB connection to {host}")
        DBAccess.connection = psycopg2.connect(f"host={host} dbname={dbname} user={user} password={password}")
        DBAccess.cursor = DBAccess.connection.cursor()
        DBAccess.is_open = True

    @staticmethod
    def writeplace(newplace: Place):
        if DBAccess.is_open:
            query = f"INSERT INTO places (name, lat, lng, rating, imgurl) VALUES ('{newplace.name}', {newplace.loc.latitude}, {newplace.loc.longitude}, {newplace.rating}, '{newplace.imgurl}');"
            ADSLogger.log(f"Sending Query: {query}")

            DBAccess.cursor.execute(query)
            DBAccess.connection.commit()

            ADSLogger.log(f"Wrote place with ID {newplace.id}")
        else:
            ADSLogger.error("Connection to database attempted, but it's closed!")

    @staticmethod
    def getplace(id: str):
        if DBAccess.is_open:
            DBAccess.cursor.execute(f"SELECT * FROM places WHERE id='{id}';")
            ADSLogger.log(f"Queried place with ID {id}")
            return DBAccess.cursor.fetchone()
        else:
            ADSLogger.error("Connection to database attempted, but it's closed!")

    @staticmethod
    def getallplaces():
        if DBAccess.is_open:
            DBAccess.cursor.execute("SELECT * FROM places;")
            ADSLogger.log("Queried all places")
            return DBAccess.cursor.fetchall()
        else:
            ADSLogger.error("Connection to database attempted, but it's closed!")

    @staticmethod
    def close():
        ADSLogger.log("Closing DB connection")
        DBAccess.connection.close()
        DBAccess.is_open = False