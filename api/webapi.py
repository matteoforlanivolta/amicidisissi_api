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
            places: list[Place] = []

            for i in dbplaces:
                lat = float(str(i[2]))
                lng = float(str(i[3]))
                iplace = Place(i[1], Location(lat, lng), i[4], i[5])
                ADSLogger.log(f"{iplace.name}, {iplace.loc.latitude}, {iplace.loc.longitude}, {iplace.rating}, {iplace.imgurl}")
                places.append(iplace)


            return jsonify({'ok': 'ok'})

        @app.route("/api/getplace", methods=['POST'])
        def getplace():
            json = request.get_json()
            key = json['key']

            if not DBAuth.validate(key):
                response = {'failed': 'key is wrong.'}
                return jsonify(response)

            id = json['id']
            DBAccess.getplace(id)

            response = {'id': id}
            return jsonify(response)
            
        
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

        app.run()