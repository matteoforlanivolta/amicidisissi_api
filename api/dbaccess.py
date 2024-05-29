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
    def open(dbname: str, user: str, password: str):
        DBAccess.connection = psycopg2.connect(f"dbname={dbname} user={user} password={password}")
        DBAccess.cursor = DBAccess.connection.cursor()
        DBAccess.is_open = True

    @staticmethod
    def writeplace(newplace: Place):
        if DBAccess.is_open:
            DBAccess.cursor.execute(f"INSERT INTO places (name, lat, lng, rating, imgurl, id) VALUES ({newplace.name}, {newplace.loc.latitude}, {newplace.loc.longitude}, {newplace.rating}, {newplace.imgurl}, {newplace.id});")
            DBAccess.connection.commit()
            ADSLogger.log(f"Wrote place with ID {newplace.id}")
        else:
            ADSLogger.error("Connection to database attempted, but it's closed!")

    @staticmethod
    def getplace(id: str):
        if DBAccess.is_open:
            DBAccess.cursor.execute(f"SELECT * FROM places WHERE id='{id}';")
            ADSLogger.log(f"Queried place with ID {id}.")
            return DBAccess.cursor.fetchone()
        else:
            ADSLogger.error("Connection to database attempted, but it's closed!")

    @staticmethod
    def close():
        DBAccess.connection.close()
        DBAccess.is_open = False