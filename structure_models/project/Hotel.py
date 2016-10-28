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

    def getHotelByID(self, hotelID):
        for hotel in self.listofhotels:
            if hotel.id == hotelID:
                return hotel

    def getHotelsByStatus(self, status):
        hotels = []
        for hotel in self.listofhotels:
            if hotel.isavaliable == status:
                hotels.append(hotel)
        return hotels

    def getAllHotels(self):
        hotels = []
        if len(self.listofhotels) != len(hotels):
            for hotel in self.listofhotels:
                hotels.append(hotel)
        if len(self.listofhotels) == len(hotels):
            return hotels

    def addhotel(self, name, isavaliable):
        ID = len(self.listofhotels) + 1
        hotel = Hotel(ID, name, isavaliable)
        self.listofhotels.append(hotel)

    def edithotel(self, act, hotelID, newname, newstatus):
        for hotel in self.listofhotels:
            if hotelID == hotel.id:
                if act == "name":
                    hotel.name = newname
                if act == "status":
                    hotel.isavaliable = newstatus

    def deletehotel(self, hotelid):
        for hotel in self.listofhotels:
            if hotel.id == hotelid:
                self.listofhotels.remove(hotel)

class HotelPrinter:
    def showAllHotels(self, hotels):
        print "Here is the list of all hotels: "
        for hotel in hotels:
            if hotel.isavaliable == "True":
                status = "avaliable"
                print "Hotel name - %s. ID - %s. Status - %s." % (hotel.name, hotel.id, status)
            else:
                status = "not avaliable"
                print "Hotel name - %s. ID - %s. Status - %s." % (hotel.name, hotel.id, status)

    def showHotelsByStatus(self, hotels, status):
        if status:
            title = "avaliable"
        else:
            title = "not avaliable"
        print "Here is the list of %s hotels: " % title
        for hotel in hotels:
            print "Hotel name - %s. ID - %s." % (hotel.name, hotel.id)

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

    def savehotel(self, hotels):
        open(hotelFileName, "w").close()
        f = open(hotelFileName, "a")
        for hotel in hotels:
            linetoadd = "%s,%s,%s\n" % (hotel.id, hotel.name, hotel.isavaliable)
            f.write(linetoadd)
        f.flush()
        f.close()





