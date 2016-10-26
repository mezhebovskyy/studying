class Hotel:
    def __init__(self, id, name, isavaliable):
        self.id = id
        self.name = name
        self.rooms = []
        self.isavaliable = isavaliable

class Room:
    def __init__(self, id, hotelID, number, beds, price, isavaliable):
        self.id = id
        self.hotelID = hotelID
        self.number = number
        self.beds = beds
        self.price = price
        self.isavaliable = isavaliable

class Order:
    def __init__(self, id, roomID, hotelID, stayfrom, staytill, numberofvisitors, email):
        self.id = id
        self.roomID = roomID
        self.hotelID = hotelID
        self.stayfrom = stayfrom
        self.staytill = staytill
        self.numberofvisitors = numberofvisitors
        self.email = email
