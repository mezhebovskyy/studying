from Models import *
from Hotel import *
from Room import *
# from Order import *

hotelFileName = "fileHotels.csv"
roomFileName = "fileRooms.csv"
orderFileName = "fileOrders.csv"


def main():
    database = Database()
    database.isDbCreated()
    database.isHotelsTableCreated()
    database.isRoomsTableCreated()

    hotelreader = HotelReader()
    hotelservice = HotelService()

    room_service = RoomService()

    hotel_printer = HotelPrinter()

    choice = ''
    while choice != 'q':
        print("\n[1] Press 1 to add new hotel.")
        print("[2] Press 2 to edit hotel.")
        print("[3] Press 3 to delete hotel.")
        print("[4] Press 4 to add new room.")
        print("[5] Press 5 to edit room.")
        print("[6] Press 6 to delete room.")
        print("[7] Press 7 to look at a number of all booked rooms in a certain hotel.")
        print("[8] Press 8 to look at a number of people in a certain hotel.")
        print("[q] Press q to quit.")
        
        choice = raw_input("\nWhat would you like to do? ")
        
        if choice == "1":
            while True:
                isavaliable = True
                name = raw_input("Type the name of new hotel: ")
                hotelservice.addhotel(name, isavaliable)
                print "Hotel successfully added."
                new_hotel = raw_input("Do you want to add another hotel?(y/n): ")
                if new_hotel == "n":
                    break
        
        elif choice == "2":
            while True:
                callback = hotel_printer.showAllHotels()
                hotelnumber = raw_input("Type number of hotel you want to edit: ")
                hotelId = callback(hotelnumber)
                hotel = hotelservice.getHotelById(hotelId)
                act = raw_input("What do you want to edit in your Hotel (name/status)?: ")
                if act == "name":
                    newname = raw_input("Type new name of hotel: ")
                    hotelservice.editHotelName(hotel, newname)
                if act == "status":
                    hotelservice.editHotelStatus(hotel)
                newedit = raw_input("Do you want another changes in your hotels?(y/n): ")
                if newedit == "n":
                    break
        
        elif choice == "3":
            while True:
                callback = hotel_printer.showAllHotels()
                hotelnumber = raw_input("Type number of hotel you want to remove: ")
                hotelId = callback(hotelnumber)
                hotelservice.deleteHotel(hotelId)
                choice = raw_input("Do you want to remove one more hotel?(y/n): ")
                if choice == "n":
                    break

        elif choice == "4":
            while True:
                callback = hotel_printer.showAllHotels()
                hotelnumber = raw_input("Type number of hotel where you want to add room: ")
                hotelId = callback(hotelnumber)
                number = raw_input("Type the number of room: ")
                beds = raw_input("Type the number of beds in room: ")
                price = raw_input("Type the price of stay per person: ")
                isavaliable = True
                room_service.addRoom(hotelId, number, beds, price, isavaliable)
                new_room = raw_input("Do you want to add another room?(y/n): ")
                if new_room == "n":
                    break

        elif choice == "5":
            while True:
                hotelcallback = hotel_printer.showAllHotels()
                hotelnumber = raw_input("Type number of hotel where you want to edit room: ")
                hotelId = hotelcallback(hotelnumber)
                roomcallback = RoomPrinter().showRoomsByHotel(hotelId)
                roomNumber = raw_input("Choose room number: ")
                roomId = roomcallback(roomNumber)

                newnumber = raw_input("Type new room number (otherwise type .): ")
                newbeds = raw_input("Type new number of beds (otherwise type .): ")
                newprice = raw_input("Type new price (otherwise type .): ")
                newstatus = raw_input("Print new status (otherwise type .): ")

                room_service.editRoom(roomId, newnumber, newbeds, newprice, newstatus)
                newedit = raw_input("Do you want another changes in your rooms?(y/n): ")
                if newedit == "n":
                    break
                
        elif choice == "6":
            while True:
                hotelcallback = hotel_printer.showAllHotels()
                hotelnumber = raw_input("Type number of hotel where you want to remove room: ")
                hotelId = hotelcallback(hotelnumber)
                roomcallback = RoomPrinter().showRoomsByHotel(hotelId)
                roomNumber = raw_input("Choose room to remove: ")
                roomId = roomcallback(roomNumber)
                room_service.deleteRoom(roomId)
                choice = raw_input("Do you want to remove one more room?(y/n): ")
                if choice == "n":
                    break


        elif choice == "q":
            print("Bye!")
            break

        else:
            print("\nI don't understand that choice, please try again.\n")

  
if __name__== "__main__":
    main()