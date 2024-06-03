# Progetto Amici Di Sissi
# webapi.py
# Codice per l'interazione via API Web

from flask import Flask, request, jsonify
from flask_cors import CORS
from place import Place
from location import Location
from dbaccess import DBAccess
from dbauth import DBAuth
from adslogging import ADSLogger

class WebAPI:
    # Inizializzazione del webserver con Flask
    @staticmethod
    def open(name, port):
        ADSLogger.log("Starting Flask webserver...")

        app = Flask(name)
        CORS(app)

        # Chiamata API (HTTP POST) che ritorna tutte le entry del database.
        #
        # Parametri JSON API:
        # key: Hash SHA256 della chiave. Validata usando la classe DBAuth
        @app.route("/api/getplaces", methods=['POST'])
        def getplaces():
            ADSLogger.log(f"Request from: {request.host_url}")

            json = request.get_json()
            key = json['key']

            # Validazione della chiave
            if not DBAuth.validate(key):
                return jsonify({'failed': 'key is wrong.'})

            dbplaces = DBAccess.getallplaces()
            places: list[dict[str, any]] = []

            for i in dbplaces:
                iplace = Place(i)
                
                if iplace.id == None:
                    ADSLogger.log("Failed to get place!")
                    return jsonify({'failed': 'db query failed'})

                places.append(iplace.to_dictionary())

            return jsonify(places)

        # Chiamata API (HTTP POST) che ritorna un'entry specifica del database.
        #
        # Parametri JSON API:
        # key: Hash SHA256 della chiave. Validata usando la classe DBAuth
        # name: Nome della `Place` che si vuole ricevere dal DB
        @app.route("/api/getplace", methods=['POST'])
        def getplace():
            json = request.get_json()
            key = json['key']

            if not DBAuth.validate(key):
                response = {'failed': 'key is wrong.'}
                return jsonify(response)

            name = json['name']

            dbplace = DBAccess.getplace(name)
            iplace = Place(dbplace)

            if iplace.id == None:
                ADSLogger.log("Failed to get place!")
                return jsonify({'failed': 'db query failed'})
            
            place = iplace.to_dictionary()

            return jsonify(place)
        
        # Chiamata API (HTTP POST) che ritorna un'entry specifica del database.
        #
        # Parametri JSON API:
        # key: Hash SHA256 della chiave. Validata usando la classe DBAuth
        # name: Nome della `Place` che si vuole ricevere dal DB
        # loc: Array di due elementi, il primo e' la latitudine e il secondo la longitudine
        # rating: Int da 0-5, valutazione di accessibilita' per il post
        # imgurl: URL dell'immagine del posto
        # 
        # Forse e' meglio non esporre questa API al pubblico :P
        # @app.route("/api/writeplace", methods=['POST'])
        #def writeplace():
        #    json = request.get_json()
        #    key = json['key']
        #
        #    if not DBAuth.validate(key):
        #        return jsonify({'failed': 'key is wrong.'})
            
        #    ADSLogger.log(json)

        #    loc = Location(json['loc'][0], json['loc'][1])
        #    newplace = Place(json['name'], loc, json['rating'], json['imgurl'])

        #    DBAccess.writeplace(newplace)

        #    return jsonify({'success': 'commited to db'})

        app.run(host="0.0.0.0", port=port)