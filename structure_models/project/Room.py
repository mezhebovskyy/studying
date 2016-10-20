from Models import Room
from Hotel import HotelService

class RoomService:
    def __init__(self):
        self.listofrooms = []

    def addRoom(self):
        array = self.listofrooms
        while True:
            new_room = raw_input("Do you want to add a room?(y/n): ")
            if new_room == "n":
                break
            if new_room == "y":
                continue
            ID = len(array) + 1
            hotelID = HotelService().hotelid
            number = raw_input("Type the number of Room: ")
            beds = raw_input("Type the number of beds in Room %s: ") % number
            price = raw_input("Type the price of stay per person: ")
            is_avaliable = True
            self.listofrooms.append(Room(ID, hotelID, number, beds, price, is_avaliable))
            print "Room №%s is successfuly added to Hotel %s." % (number, hotelID)
            
    def editroom(self, roomID):



    def showrooms(self, from, till, hotelID):

        # after all this array contains 
        array = [self.hotelID, self.roomID, ...]
        print array




    
