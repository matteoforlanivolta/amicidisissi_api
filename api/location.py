# Progetto Amici Di Sissi
# location.py
# Classe che rappresenta una posizione (lat, long) sulla mappa

class Location:
    def __init__(self, latitude: float, longitude: float) -> None:
        self.longitude = longitude
        self.latitude = latitude