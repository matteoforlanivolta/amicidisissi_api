from location import Location

class Place:
    def __init__(self, name: str, loc: Location, rating: int, imgurl: str) -> None:
        self.name = name
        self.loc = loc
        self.rating = rating
        self.imgurl = imgurl