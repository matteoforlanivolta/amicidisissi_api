# Progetto Amici Di Sissi
# main.py
# Codice per inizializzare ed avviare l'API

from adslogging import ADSLogger
from dbauth import DBAuth
from dbaccess import DBAccess
from webapi import WebAPI

# remove me!!!
# import hashlib

def main():
    ADSLogger.open()
    ADSLogger.log("Starting AmiciDiSissi API.")

    # DBAuth.validate(hashlib.sha256("prova".encode('utf-8')).hexdigest())
    DBAccess.open("test_bw", "postgres", "dbprova", "lab.matthew5pl.net")

    WebAPI.open("ADSAPI")

if __name__ == "__main__":
    main()