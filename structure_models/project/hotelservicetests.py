import unittest
from Hotel import HotelService


class HotelserviceTestSuite(unittest.TestCase):
    def test_can_Add_New_Hotel(self):
        hotelservice = HotelService()

        hotelservice.addhotel("fff", True)

        self.assertEqual(len(hotelservice.listofhotels), 1)


    def test_can_Delete_Hotel(self):
        hotelservice = HotelService()
        hotelservice.addhotel("mmm", True)
        hotelservice.addhotel("nnn", True)

        hotelservice.deleteHotel(2)

        self.assertEqual(len(hotelservice.listofhotels), 1)
        for hotel in hotelservice.listofhotels:
            self.assertEqual(hotel.name, "mmm")


    def test_can_Edit_Hotel_Name(self):
        hotelservice = HotelService()
        hotelservice.addhotel("mmm", True)

        hotelservice.editHotelName(1, "ttt")

        for hotel in hotelservice.listofhotels:
            self.assertEqual(hotel.name, "ttt")


    def test_can_Edit_Hotel_Status(self):
        hotelservice = HotelService()
        hotelservice.addhotel("mmm", True)

        hotelservice.editHotelStatus(1)

        for hotel in hotelservice.listofhotels:
            self.assertEqual(hotel.isavaliable, False)


    def test_can_Get_Hotel_by_Number(self):
        hotelservice = HotelService()
        hotelservice.addhotel("mmm", True)
        hotelservice.addhotel("vvv", True)
        hotelservice.addhotel("nnn", False)

        hotel = hotelservice.getHotel(3)

        self.assertEqual(hotel.name, "nnn")


    def test_can_Get_Hotels_By_Status(self):
        hotelservice = HotelService()
        hotelservice.addhotel("mmm", True)
        hotelservice.addhotel("vvv", True)
        hotelservice.addhotel("nnn", False)

        avaliableHotels = hotelservice.getHotelsByStatus(True)
        notAvaliableHotels = hotelservice.getHotelsByStatus(False)

        self.assertEqual(len(avaliableHotels), 2)
        self.assertEqual(len(notAvaliableHotels), 1)


    def test_can_Get_All_Hotels(self):
        hotelservice = HotelService()
        hotelservice.addhotel("mmm", True)
        hotelservice.addhotel("nnn", True)

        hotels = hotelservice.getAllHotels()

        self.assertEqual(len(hotels), 2)


if __name__ == "__main__":
    unittest.main()
