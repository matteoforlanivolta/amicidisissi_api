# Progetto Amici Di Sissi
# itinerary.py
# Classe che rappresenta un itinerario (in sintesi un'array di Place con un nome)

from place import Place
from adslogging import ADSLogger

class Itinerary:
    def __init__(self, name: str, places: list[Place]):
        self.name = name
        self.places = places

    # Ritorna il numero di Place nell'itinerario.
    def get_size(self) -> int:
        return len(self.places)
    
    # Ritorna l'n-esimo Place nell'itinerario.
    # `n` deve essere >= 0 ed entro i limiti dell'array.
    def get_nth(self, n: int) -> Place:
        if n > len(self.places) - 1 or n < 0:
            ADSLogger.error("Tried to get Place out of bounds of Itinerary!")
            return None
        
        return self.places[n]
    
    # Ritorna la Place nell'itinerario con nome `name`.
    # Ritorna None se la Place richiesta non esiste.
    def get_named(self, name: str) -> Place:
        for p in self.places:
            if p.name == name:
                return p
            
        ADSLogger.warn("Looked up non-existing Place in Itinerary.")
        return None