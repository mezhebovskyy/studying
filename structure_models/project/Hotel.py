from Models import Hotel
from Room import *
# from Order import OrderService

hotelFileName = "fileHotels.csv"

class HotelService:
    def __init__(self):
        self.listofhotels = []
        self.roomservice = RoomService()
    
    def loadhotels(self):
        reader = HotelReader()
        self.listofhotels = reader.readfromfile(hotelFileName)
        for hotel in self.listofhotels:
            hotel.rooms = self.roomservice.loadRoomsForHotel(hotel.id)

    def addhotel(self, name, isavaliable):
        ID = len(self.listofhotels) + 1
        hotel = Hotel(ID, name, isavaliable)
        self.listofhotels.append(hotel)

    def deletehotel(self, hotelid):
        for hotel in self.listofhotels:
            if hotel.id == hotelid:
                self.listofhotels.remove(hotel)

    def showhotels(self, status):
        if status:
            title = "avaliable"
        else:
            title = "not avaliable"
        print "Here is the list of %s hotels: " % title
        for item in self.listofhotels:
            if item.isavaliable == status:
                print "Hotel name is %s. Hotel ID - %s." % (item.name, item.id)
    
    def edithotel(self, act, hotelID, newname, newstatus):
        for hotel in self.listofhotels:
            if hotelID == hotel.id:
                if act == "name":
                    hotel.name = newname
                if act == "status":
                    hotel.isavaliable = newstatus

    def savehotel(self):
        open(hotelFileName, "w").close()
        f = open(hotelFileName, "a")
        for hotel in self.listofhotels:
            linetoadd = "%s,%s,%s\n" % (hotel.id, hotel.name, hotel.isavaliable)
            f.write(linetoadd)
        f.flush()
        f.close()

class HotelReader:
    def readfromfile(self, fileName):
        array = []
        f = open(fileName, "r")
        for line in f:
            line = line.replace('\n','')
            id, name, status = line.split(",")
            array.append(Hotel(id, name, status))
        f.close()
        return array





