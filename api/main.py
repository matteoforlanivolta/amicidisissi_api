# Progetto Amici Di Sissi
# main.py
# Codice per inizializzare ed avviare l'API

from adslogging import ADSLogger
from dbauth import DBAuth

# remove me!!!
import hashlib

def main():
    ADSLogger.open()
    ADSLogger.log("Starting AmiciDiSissi API.")

    DBAuth.validate(hashlib.sha256("prova".encode('utf-8')).hexdigest())

if __name__ == "__main__":
    main()