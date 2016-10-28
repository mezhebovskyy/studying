import unittest
from Hotel import HotelService

class HotelserviceTestSuite(unittest.TestCase):
    def test_can_add_new_hotel(self):
        hotelservice = HotelService()
        hotelservice.addhotel("fff", True)
        self.assertEqual(len(hotelservice.listofhotels), 1)
        
    def test_can_delete_hotel(self):
        hotelservice = HotelService()
        hotelservice.addhotel("mmm", True)
        hotelservice.addhotel("nnn", True)
        hotelservice.deletehotel(2)
        self.assertEqual(len(hotelservice.listofhotels), 1)

    def test_can_edit_hotel(self):
        hotelservice = HotelService()
        hotelservice.addhotel("mmm", True)
        hotelservice.edithotel("name", 1, "Hilton", None)
        hotelservice.edithotel("status", 1, None, False)
        for hotel in hotelservice.listofhotels:
            self.assertTrue(hotel.name == "Hilton")
            self.assertTrue(hotel.isavaliable == False)
    
    def test_get_Hotel_By_Id(self):
        hotelservice = HotelService()
        hotelservice.addhotel("mmm", True)
        for neededhotel in hotelservice.listofhotels:
            if neededhotel.id == "1":
                return neededhotel.name
        hotel = hotelservice.getHotelByID(1)
        self.assertTrue(neededhotel.name == hotel.name)

    def test_get_Hotels_By_Status(self):
        hotelservice = HotelService()
        hotelservice.addhotel("mmm", True)
        hotelservice.addhotel("vvv", True)
        hotelservice.addhotel("nnn", False)
        neededhotels = hotelservice.getHotelsByStatus(True)
        hotels = []
        for hotel in hotelservice.listofhotels:
            if hotel.isavaliable == True:
                hotels.append(hotel)
        self.assertTrue(neededhotels == hotels)

    def test_get_All_Hotels(self):
        hotelservice = HotelService()
        hotelservice.addhotel("mmm", True)
        hotelservice.addhotel("nnn", True)
        hotels = hotelservice.getAllHotels()
        self.assertTrue(hotels == hotelservice.listofhotels)

if __name__ == "__main__":
    unittest.main()