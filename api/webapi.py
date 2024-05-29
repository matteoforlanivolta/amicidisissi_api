# Progetto Amici Di Sissi
# webapi.py
# Codice per l'interazione via API Web

from flask import Flask, request, jsonify
from place import Place
from dbaccess import DBAccess
from dbauth import DBAuth

class WebAPI:
    app = Flask(__name__)

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
            response = {'failed': 'key is wrong.'}
            return jsonify(response)
        
        newplace = Place(json['name'], json['loc'], json['rating'], json['imgurl'])

        DBAccess.writeplace(newplace)