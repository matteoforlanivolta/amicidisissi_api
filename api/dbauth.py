import psycopg2
import os
import hashlib

from adslogging import ADSLogger

class DBAuth:
    @staticmethod
    def validate(passwd: str) -> bool:
        ADSLogger.log("Attempting to validate hash.")
        env_passwd = os.getenv("ADS_PASSWD")
        if env_passwd == None:
            ADSLogger.error("Hash validation failed, ADS_PASSWD not set!")
            return False

        env_passwd_hash = hashlib.sha256(env_passwd.encode('utf-8')).hexdigest()

        ADSLogger.error("REMOVE ME!!! NO PROD!!!! " + passwd + " ?= " + env_passwd_hash)

        if passwd == env_passwd_hash:
            ADSLogger.log("Hash validation successful!")
            return True
        else:
            ADSLogger.warn("Hash validation failed!")
            return False