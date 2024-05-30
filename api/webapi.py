# Progetto Amici Di Sissi
# webapi.py
# Codice per l'interazione via API Web

from flask import Flask, request, jsonify
from place import Place
from location import Location
from dbaccess import DBAccess
from dbauth import DBAuth
from adslogging import ADSLogger

class WebAPI:
    @staticmethod
    def open(name):
        app = Flask(name)

        @app.route("/api/getplaces", methods=['POST'])
        def getplaces():
            json = request.get_json()
            key = json['key']

            if not DBAuth.validate(key):
                response = {'failed': 'key is wrong.'}
                return jsonify(response)

            dbplaces = DBAccess.getallplaces()
            places: list[dict[str, any]] = []

            for i in dbplaces:
                iplace = Place(i)
                places.append(iplace.to_dictionary())

            return jsonify(places)

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
            
            place = iplace.to_dictionary()

            return jsonify(place)
            
        
        @app.route("/api/writeplace", methods=['POST'])
        def writeplace():
            json = request.get_json()
            key = json['key']

            if not DBAuth.validate(key):
                return jsonify({'failed': 'key is wrong.'})
            
            ADSLogger.log(json)

            loc = Location(json['loc'][0], json['loc'][1])
            newplace = Place(json['name'], loc, json['rating'], json['imgurl'])

            DBAccess.writeplace(newplace)

            return jsonify({'success': 'commited to db'})

        app.run(host="0.0.0.0", port=5001)