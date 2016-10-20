from Models import Hotel
from Room import RoomService
from Order import OrderService

hotelFileName = "fileHotels.csv"

class HotelService:
    def __init__(self):
        self.listofhotels = []
    
    def loadItems(self):
        reader = HotelReader()
        self.listofhotels = reader.readfromfile(hotelFileName)

    def addhotel(self):
        array = self.listofhotels
        self.hotelid = ID
        while True:
            ID = len(array) + 1
            name = raw_input("Type the name of new hotel: ")
            if name == ".":
                break
            oneroom = RoomService.addRoom
            rooms = RoomService().listofrooms
            is_avaliable = True
            self.listofhotels.append(Hotel(ID, name, rooms, is_avaliable))

    def showhotels(self, status):
        print "Here is the list of %s hotels: " % status
        for item in self.listofhotels:
            if item.status == status:
                print "Hotel name is %s. Hotel ID - %s." % (item.name, item.id)
    
    def edithotel(self, hotelID):
        for hotel in self.listofhotels:
            if hotelID == hotel.id:
                act = raw_input("What do you want to edit in your Hotel (name/status)?: ")
                if act == "name":
                    new_name = raw_input("Type new name of Hotel")
                    hotel.name = new_name
                if act == "status":
                    print "Hotel status is %s." % hotel.status
                    new_status = raw_input("Print new status: ")
                    hotel.status = new_status
                 

class HotelReader:
    def readfromfile(self, fileName):
        array = []
        f = open(fileName, "r")
        for line in f:
            line = line.replace('\n','')
            id, name, rooms, status = line.split(",")
            array.append(Hotel(id, name, rooms, status))
        f.close()
        return array

def main():
    listofhotels = HotelService()

    # f = open(hotelFileName, "r")
    # for line in f:
    #     line = line.replace('\n','')
    #     id, name, rooms, status = line.split(",")
    #     hotel = Hotel(id, name, rooms, status)
    #     listofhotels.listofhotels
    #     todolist.listofitems.append(item)
    # f.close()





