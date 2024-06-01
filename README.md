# API Web per il sito BetterWays - Amici Di Sissi

L'API è scritta in Python 3, utilizzando le librerie [psycopg2](https://github.com/psycopg/psycopg2) e [Flask](https://github.com/pallets/flask) per l'accesso al database PostgreSQL e per esporre le chiamate API necessarie.

# Installazione

Idealmente questa API verrebbe eseguita su un server Linux.

Utilizzando un sistema Linux tipico, dopo aver copiato il contenuto di questa repository nel percorso `/etc/adsapi/`, è possibile installare le dipendenze necessarie ed avviare il webserver usando lo script `run.sh`. 

### Avvertenza sullo script `run.sh` ⚠️
Questo script usa l'opzione `--break-system-packages` per installare i pacchetti necessari direttamente dalle repository Python, ignorando eventuali pacchetti equivalenti disponibili nella repository di sistema. Di solito questo non causa problemi, ma se si vuole evitare al 100% di avere problemi di dipendenze con altri programmi Python installati bisogna installare tutti i pacchetti elencati nel file `requirements.txt` in un altro modo, e poi avviare il webserver eseguendo `python3 api/main.py`.

# Installazione come servizio

Per i sistemi Linux che utilizzano systemd (ad es. Debian, Fedora, CentOS, Red Hat, Ubuntu, OpenSUSE o Arch) è possibile installare il webserver come un servizio.

In questo modo il programma verrà eseguito all'avvio del sistema e rimarrà in esecuzione in background, riavviandosi da solo se dovesse crashare.

Nella repository è presente un file `adsapi.service` (che fa uso dello script `run.sh`). Copiare questo file nella directory `/etc/systemd/system`.

Il servizio può poi essere avviato con `systemctl start adsapi.service`. Per eseguire il programma all'avvio del sistema, attivare il servizio con `systemctl enable adsapi.service`.