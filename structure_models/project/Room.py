import sqlite3 as lite
import sys
import uuid
from Models import Room
from Hotel import *

database = "HROdata.db"


class RoomService:
    def getRoomById(self, roomID):
        room = None
        conn = lite.connect(database)
        with conn:
            conn.row_factory = lite.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * From Rooms WHERE Id='%s'" % str(roomID))
            row = cursor.fetchone()
            room = Room(row["Id"], row["HotelID"], row["Number"], row["Beds"], row["Price"], str(row["Status"])=="True")
        conn.close()
        return room

    def getRoomsByStatus(self, status):
        rooms = []
        conn = lite.connect(database)
        with conn:
            conn.row_factory = lite.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * From Rooms WHERE Status=%s" % str(status))
            rows = cursor.fetchall()
            for row in rows:
                rooms.append(Room((row["Id"], row["HotelID"], row["Number"], row["Beds"], row["Price"], str(row["Status"])=="True")))
        conn.close()
        return rooms

    def getRoomsByHotel(self, hotelId):
        rooms = []
        conn = lite.connect(database)
        with conn:
            conn.row_factory = lite.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * From Rooms WHERE HotelID='%s'" % str(hotelId))
            rows = cursor.fetchall()
            for row in rows:
                rooms.append(Room(row["Id"], row["HotelID"], row["Number"], row["Beds"], row["Price"], str(row["Status"])=="True"))
        conn.close()
        return rooms

    def getAllRooms(self):
        rooms = []
        conn = lite.connect(database)
        with conn:
            conn.row_factory = lite.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * From Rooms")
            rows = cursor.fetchall()
            for row in rows:
                rooms.append(Room(row["Id"], row["HotelID"], row["Number"], row["Beds"], row["Price"],
                                  str(row["Status"]) == "True"))
        conn.close()
        return rooms

    def addRoom(self, hotelId, number, beds, price, isavaliable):
        ID = uuid.uuid4()
        room = (Room(ID, hotelId, number, beds, price, isavaliable))
        RoomReader().saveRoom(room)

    def editRoom(self, roomId, newnumber, newbeds, newprice, newstatus):
        room = self.getRoomById(roomId)
        if newnumber != ".":
            room.number = newnumber
        if newbeds != ".":
            room.beds = newbeds
        if newprice != ".":
            room.price = newprice
        if newstatus != ".":
            room.isavaliable = newstatus
        RoomReader().updateRoom(room)

    def deleteRoom(self, roomId):
        RoomReader().deleteRoomFromDB(roomId)


class RoomPrinter:
    def showAllRooms(self):
        print "Here is the list of all rooms: "
        rooms = RoomService().getAllRooms()
        index = 1
        for room in rooms:
            if room.isavaliable == True:
                print ("%s) Room number - %s. Number of beds - %s. Price - %s. Status - %s."
                       % (index, room.number, room.beds, room.price, "avaliable"))
            else:
                print ("%s) Room number - %s. Number of beds - %s. Price - %s. Status - %s."
                   % (index, room.number, room.beds, room.price, "not avaliable"))
            index += 1

        def getId(number):
            return rooms[int(number) - 1].id
        return getId


    def showRoomsByHotel(self, hotelId):
        rooms = RoomService().getRoomsByHotel(hotelId)
        index = 1
        for room in rooms:
            if room.isavaliable == True:
                status = "avaliable"
                print "%s) Room number - %s. Status - %s. Number of beds - %s. Price - %s." % (index, room.number, status,
                                                                                           room.beds, room.price)
            else:
                status = "not avaliable"
                print "%s) Room number - %s. Status - %s. Number of beds - %s. Price - %s." % (index, room.number, status,
                                                                                           room.beds, room.price)
            index += 1

        def getId(number):
            return rooms[int(number) - 1].id
        return getId

    def showRoomsByStatus(self, status):
        rooms = RoomService().getRoomsByStatus(status)
        if status == True:
            title = "avaliable"
        else:
            title = "not avaliable"
        print "Here is the list of %s rooms: " % title
        for room in rooms:
            if str(room.isavaliable) == str(status):
                print "Room number - %s. Number of beds - %s. Price - %s. Room ID - %s." % (room.number, room.beds, room.price, room.id)



        conn = lite.connect(database)
        with conn:
            conn.row_factory = lite.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * From Rooms WHERE Status=%s" % str(status))
            rows = cursor.fetchall()
            if status == True:
                title = "avaliable"
            else:
                title = "not avaliable"
            print "Here is the list of %s rooms: " % title
            for row in rows:
                print "Room number - %s. Number of beds - %s. Price - %s. Room ID - %s." % (row["Number"], row["Beds"], row["Price"], row["Id"])


class RoomReader:
    def saveRoom(self, room):
        conn = lite.connect(database)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Rooms VALUES(?, ?, ?, ?, ?, ?)", (str(room.id), str(room.hotelID),
                                                                      room.number, room.beds, room.price, str(room.isavaliable)))
        conn.commit()
        conn.close()

    def updateRoom(self, room):
        conn = lite.connect(database)
        with conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Rooms SET Number=?, Beds=?, Price=?, Status=? WHERE Id=?", (room.number, room.beds,
                                                                                               str(room.price), str(room.isavaliable), str(room.id)))
            conn.commit()
        conn.close()

    def deleteRoomFromDB(self, ID):
        conn = lite.connect(database)
        with conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Rooms WHERE Id=?", [str(ID)])
            conn.commit()
        conn.close()
