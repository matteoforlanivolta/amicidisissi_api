# Progetto Amici Di Sissi
# adslogging.py
# Logger di messaggi sul funzionamento dell'API (info, avvisi, errori)

import os
import colorama
import termcolor
import datetime

class ADSLogger:
    file_handle = None
    is_open = False

    # Apre il file di log ("Home/ads.log") per la scrittura.
    # Non e' necessario per il funzionamento del logger, ma senza
    # i log vengono scritti solo sulla console e non in un file,
    # rendendo l'analisi piu' difficile
    @staticmethod
    def open():
        colorama.init()
        # Trovo il percorso della Home
        home_dir = os.path.expanduser("~")
        ADSLogger.file_handle = open(os.path.join(home_dir, "ads.log"), 'a+')
        ADSLogger.is_open = True

    # Chiude il file di log
    @staticmethod
    def close():
        if ADSLogger.is_open:
            ADSLogger.file_handle.close()
            ADSLogger.is_open = False

    # Log di un informazione generica che non causa
    # e non ha il potenziale di causare errori
    @staticmethod
    def log(x):
        buf = f"[{str(datetime.datetime.now())}] Info: {x}"
        print(termcolor.colored(buf, 'green'))
        if ADSLogger.is_open:
            ADSLogger.file_handle.write(buf + '\n')

    # Log di un avviso, per informare di una condizione
    # che potrebbe causare errori
    @staticmethod
    def warn(x):
        buf = f"[{str(datetime.datetime.now())}] Warning: {x}"
        print(termcolor.colored(buf, 'yellow'))
        if ADSLogger.is_open:
            ADSLogger.file_handle.write(buf + '\n')

    # Log di un errore
    @staticmethod
    def error(x):
        buf = f"[{str(datetime.datetime.now())}] ERROR: {x}"
        print(termcolor.colored(buf, 'red'))
        if ADSLogger.is_open:
            ADSLogger.file_handle.write(buf + '\n')