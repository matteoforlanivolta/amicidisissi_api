# Progetto Amici Di Sissi
# place.py
# Classe che rappresenta un luogo che puo' essere visitato

from location import Location
from uuid import uuid4

class Place:
    def __init__(self, name: str, loc: Location, rating: int, imgurl: str) -> None:
        self.name = name
        self.loc = loc
        self.rating = rating
        self.imgurl = imgurl
        self.id = uuid4().hex

    def __init__(self, dbquery):
        if dbquery != None:
            self.name = dbquery[1]
            self.loc = Location(float(str(dbquery[2])), float(str(dbquery[3])))
            self.rating = int(dbquery[4])
            self.imgurl = dbquery[5]
            self.id = uuid4().hex

    def to_dictionary(self):
        return {'name': self.name, 'loc': [self.loc.latitude, self.loc.longitude], 'rating': self.rating, 'imgurl': self.imgurl}