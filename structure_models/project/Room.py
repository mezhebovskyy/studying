from Models import Room
from Hotel import *

roomFileName = "fileRooms.csv"


class RoomService:
    # def __init__(self):
    #     self.listofrooms = []

    def addRoom(self, hotel, number, beds, price, isavaliable):
        ID = len(self.listofrooms) + 1
        hotelid = hotel.id
        hotel.rooms.append(Room(ID, hotelid, number, beds, price, isavaliable))

    def loadRoomsForHotel(self, hotelid):
        roomreader = RoomReader()
        rooms = roomreader.readfromfile(roomFileName, hotelid)
        return rooms 

    # def editroom(self, room):



    # def showrooms(self, from, till, hotelID):

    #     # after all this array contains 
    #     array = [self.hotelID, self.roomID, ...]
    #     print array

    def saveroom(self):
        open(roomFileName, "w").close()
        f = open(roomFileName, "a")
        for room in self.listofrooms:
            linetoadd = "%s,%s,%s,%s,%s\n" % (room.id, room.hotelID, room.number, room.beds, room.price, room.isavaliable)
            f.write(linetoadd)
        f.flush()
        f.close()


class RoomReader:
    def readfromfile(self, fileName, hotelid):
        array = []
        f = open(fileName, "r")
        for line in f:
            line = line.replace('\n','')
            id, hotelID, number, beds, price, isavaliable = line.split(",")
            if hotelID == hotelid:
                array.append(Room(id, hotelID, number, beds, price, isavaliable))
        f.close()
        return array


    
