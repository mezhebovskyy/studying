from Models import *
from Hotel import *
from Rooms import *
from Order import *

hotelFileName = "fileHotels.csv"
roomFileName = "fileRooms.csv"
orderFileName = "fileOrders.csv"


def main():
    bunchofhotels = HotelService()
    f = open(hotelFileName, "r")
    for line in f:
        line = line.replace('\n','')
        id, name, rooms, status = line.split(",")
        hotel = Hotel(id, name, rooms, status)
        bunchofhotels.listofhotels.append(hotel)
    f.close()

    bunchofrooms = RoomService()
    f = open(roomFileName, "r")
    for line in f:
        line = line.replace('\n','')
        id, hotelID, number, beds, price, status = line.split(",")
        room = Room(id, hotelID, number, beds, price, status)
        bunchofrooms.listofrooms.append(room)
    f.close()

    bunchoforders = OrderService()
    f = open(ordrFileName, "r")
    for line in f:
        line = line.replace('\n','')
        id, roomID, hotelID, stayfrom, staytill, numberofvisitors, email = line.split(",")
        order = Order(id, roomID, hotelID, stayfrom, staytill, numberofvisitors, email)
        bunchoforders.listoforders.append(order)
    f.close()

choice = ''
while choice != 'q':
    print("\n[1] Press 1 to add new hotel.")
    print("[2] Press 2 to add new room to existing hotel.")
    print("[3] Press 3 to look at a number of all booked rooms in a certain hotel.")
    print("[4] Press 4 to look at a number of people in a certain hotel.")
    print("[5] Press 5 to close the room for repairs.")
    print("[6] Press 6 to close hotel for repairs.")
    print("[q] Press q to quit.")
    
    choice = raw_input("\nWhat would you like to do? ")
    
    if choice == '1':
        
    elif choice == '2':
        print("\nHere are some running shoes. Run fast!\n")
    elif choice == '3':
        print("\nHere's a map. Can you leave a trip plan for us?\n")
    elif choice == 'q':
        print("\nThanks for playing. See you later.\n")
    else:
        print("\nI don't understand that choice, please try again.\n")

print("Thanks again, bye now.")