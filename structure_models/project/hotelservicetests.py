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


if __name__ == "__main__":
    unittest.main()