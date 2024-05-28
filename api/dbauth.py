# Progetto Amici Di Sissi
# dbauth.py
# Codice per la gestione degli accessi al database

import psycopg2
import os
import hashlib

from adslogging import ADSLogger

class DBAuth:
    # Convalida se l'hash SHA256 e' valida per l'accesso al DB.
    # Parametro: passwd (stringa), hash SHA256 della chiave.
    # Ritorna: Valore bool, se true l'autenticazione e' effettuata con successo.
    @staticmethod
    def validate(passwd: str) -> bool:
        ADSLogger.log("Attempting to validate hash.")

        # Carico la chiave dalle variabili di ambiente
        env_passwd = os.getenv("ADS_PASSWD")

        # Controllo che la chiave sia configurata
        if env_passwd == None:
            ADSLogger.error("Hash validation failed, did you set $ADS_PASSWD?")
            return False

        # Calcolo l'hash SHA256 della chiave
        env_passwd_hash = hashlib.sha256(env_passwd.encode('utf-8')).hexdigest()

        ADSLogger.error("REMOVE ME!!! NO PROD!!!! " + passwd + " ?= " + env_passwd_hash)

        # Se l'hash passato e l'hash della chiave sono uguali, l'autenticazione e' riuscita
        if passwd == env_passwd_hash:
            ADSLogger.log("Hash validation successful!")
            return True
        else:
            ADSLogger.warn("Hash validation failed!")
            return False