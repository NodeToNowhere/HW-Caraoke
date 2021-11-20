import unittest
from src.guest import Guests
from src.room import Room


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guests("Betty")
        self.guest_2 = Guests("Ben")
        self.guest_3 = Guests("Bill")
        self.guest_4 = Guests("Bob")
        self.guest_5 = Guests("Ben")
        self.guest_6 = Guests("Brian")
        
        self.room = Room("Green")

    def test_guest_list_length(self):
        self.room.add_guests(self.guest_1)
        expected = 1
        actual = len(self.room.guest_list)
        self.assertEqual(expected, actual)
