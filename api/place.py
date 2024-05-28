# Progetto Amici Di Sissi
# place.py
# Classe che rappresenta un luogo che puo' essere visitato

from location import Location

class Place:
    def __init__(self, name: str, loc: Location, rating: int, imgurl: str) -> None:
        self.name = name
        self.loc = loc
        self.rating = rating
        self.imgurl = imgurl