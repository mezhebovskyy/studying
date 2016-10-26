from Models import *
from Hotel import *
from Room import *
# from Order import *

hotelFileName = "fileHotels.csv"
roomFileName = "fileRooms.csv"
orderFileName = "fileOrders.csv"


def main():
    bunchofhotels = HotelService()
    bunchofhotels.loadhotels()

    # bunchofrooms = RoomService()
    # f = open(roomFileName, "r")
    # for line in f:
    #     line = line.replace('\n','')
    #     id, hotelID, number, beds, price, status = line.split(",")
    #     room = Room(id, hotelID, number, beds, price, isavaliable)
    #     bunchofrooms.listofrooms.append(room)
    # f.close()

    # bunchoforders = OrderService()
    # f = open(ordrFileName, "r")
    # for line in f:
    #     line = line.replace('\n','')
    #     id, roomID, hotelID, stayfrom, staytill, numberofvisitors, email = line.split(",")
    #     order = Order(id, roomID, hotelID, stayfrom, staytill, numberofvisitors, email)
    #     bunchoforders.listoforders.append(order)
    # f.close()

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
        print("[9] Press 9 to save hotels to file system.")
        print("[10] Press 10 to save rooms to file system.")
        print("[q] Press q to quit.")
        
        choice = raw_input("\nWhat would you like to do? ")
        
        if choice == "1":
            while True:
                isavaliable = True
                name = raw_input("Type the name of new hotel: ")
                bunchofhotels.addhotel(name, isavaliable)
                print "Hotel successfully added."
                new_hotel = raw_input("Do you want to add another hotel?(y/n): ")
                if new_hotel == "n":
                    break
        
        elif choice == "2":
            while True:
                hotelID = raw_input("Type index of the hotel where you want to add a room: ")
                number = raw_input("Type the number of Room: ")
                beds = raw_input("Type the number of beds in Room %s: ") % number
                price = raw_input("Type the price of stay per person: ")
                isavaliable = True
                RoomService().addRoom(hotelID, number, beds, price, isavaliable)
                new_room = raw_input("Do you want to add another room?(y/n): ")
                if new_room == "n":
                    break
        
        elif choice == "3":
            while True:
                hotelID = raw_input("Type ID of hotel you want to delete: ")
                bunchofhotels.deletehotel(hotelID)
                choice = raw_input("Do you want to remove one more hotel?(y/n): ")
                if choice == "n":
                    break
        # elif choice == "4":

        elif choice == "5":
            while True:
                hotelID = raw_input("Type ID of hotel you want to edit: ")
                act = raw_input("What do you want to edit in your Hotel (name/status)?: ")
                if act == "name":
                    newname = raw_input("Type new name of hotel: ")
                    bunchofhotels.edithotel(act, hotelID, newname, None)
                    print "Hotel name was successfully changed."
                if act == "status":
                    newstatus = raw_input("Print new status: ")
                    bunchofhotels.edithotel(act, hotelID, None, newstatus)
                    print "Hotel status was successfully changed."
                newedit = raw_input("Do you want another changes in your hotels?(y/n): ")
                if newedit == "n":
                    break

        # elif choice == "6":


        elif choice == "9":
            bunchofhotels.savehotel()
            print "Hotels are saved to a file."

        # elif choice == "9":
        #     bunchofhotels.savehotel()
        #     print "Hotels are saved to a file."

        elif choice == "q":
            print("Thanks again, bye now.")
            break

        

        else:
            print("\nI don't understand that choice, please try again.\n")

  
if __name__== "__main__":
    main()