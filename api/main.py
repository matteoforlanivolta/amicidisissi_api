# Progetto Amici Di Sissi
# main.py
# Codice per inizializzare ed avviare l'API

from adslogging import ADSLogger
from dbauth import DBAuth
from dbaccess import DBAccess
from webapi import WebAPI

def main():
    ADSLogger.open()
    ADSLogger.log("Starting AmiciDiSissi API.")

    DBAccess.open("test_bw", "postgres", "dbprova", "lab.matthew5pl.net")

    WebAPI.open("ADSAPI", 5001)

    DBAccess.close()
    ADSLogger.log("AmiciDiSissi API is going down!")

if __name__ == "__main__":
    main()