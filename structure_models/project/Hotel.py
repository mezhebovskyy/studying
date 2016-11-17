import sqlite3 as lite
import sys
import uuid
from Models import Hotel
from Room import *
# from Order import OrderService

database = "HROdata.db"

class HotelService:
    def getHotelById(self, hotelID):
        hotel = None
        conn = lite.connect(database)
        with conn:
            conn.row_factory = lite.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Hotels WHERE Id='%s'" % hotelID)
            row = cursor.fetchone()
            hotel = Hotel(row["Id"], str(row["Name"]), str(row["Status"])=="True")
        conn.close()
        return hotel

    def getHotelsByStatus(self, status):
        hotels = []
        conn = lite.connect(database)
        with conn:
            conn.row_factory = lite.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Hotels WHERE Status=%s" % status)
            rows = cursor.fetchall()
            for row in rows:
                hotels.append(Hotel(row["Id"], str(row["Name"]), row["Status"]))
        conn.close()
        return hotels

    def getAllHotels(self):
        hotels = []
        conn = lite.connect(database)
        with conn:
            conn.row_factory = lite.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Hotels")
            rows = cursor.fetchall()
            for row in rows:
                hotels.append(Hotel(row["Id"], str(row["Name"]), str(row["Status"])=='True'))
        conn.close()
        return hotels

    def addhotel(self, name, isavaliable):
        ID = uuid.uuid4()
        hotel = Hotel(ID, name, isavaliable)
        HotelReader().saveNewHotel(hotel)

    def editHotelName(self, hotel, newname):
        hotel.name = newname
        HotelReader().updateHotelName(hotel, newname)

    def editHotelStatus(self, hotel):
        hotel.isavaliable = not hotel.isavaliable
        HotelReader().updateHotelStatus(hotel)

    def deleteHotel(self, hotelId):
        HotelReader().deleteHotelFromDB(hotelId)


class HotelPrinter:
    def showAllHotels(self):
        print "Here is the list of all hotels: "
        hotels = HotelService().getAllHotels()
        index = 1
        for hotel in hotels:
            if hotel.isavaliable == True:
                print "%s) Hotel name - %s. Status - %s. ID - %s." % (index, hotel.name, "avaliable", hotel.id)
            else:
                print "%s) Hotel name - %s. Status - %s. ID - %s." % (index, hotel.name, "not avaliable", hotel.id)
            index += 1

        def getId(number):
            return hotels[int(number)-1].id
        return getId

    def showHotelsByStatus(self, status):
        conn = lite.connect(database)
        with conn:
            conn.row_factory = lite.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * From Hotels WHERE Status=%s" % str(status))
            rows = cursor.fetchall()
            if status == True:
                title = "avaliable"
            else:
                title = "not avaliable"
            print "Here is the list of %s hotels: " % title
            for row in rows:
                print "Hotel name - %s. ID - %s." % (row["Name"], row["Id"])

class HotelReader:
    def saveNewHotel(self, hotel):
        conn = lite.connect(database)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Hotels VALUES(?, ?, ?)", (str(hotel.id), hotel.name, str(hotel.isavaliable)))
        conn.commit()
        conn.close()

    def updateHotelName(self, hotel, name):
        conn = lite.connect(database)
        with conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Hotels SET Name=? WHERE Id=?", (name, str(hotel.id)))
            conn.commit()
        conn.close()

    def updateHotelStatus(self, hotel):
        conn = lite.connect(database)
        with conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Hotels SET Status=? WHERE Id=?", (str(hotel.isavaliable), str(hotel.id)))
            conn.commit()
        conn.close()

    def deleteHotelFromDB(self, hotelID):
        conn = lite.connect(database)
        with conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Hotels WHERE Id=?", [str(hotelID)])
            cursor.execute("DELETE FROM Rooms WHERE HotelID=?", [str(hotelID)])
            conn.commit()
        conn.close()