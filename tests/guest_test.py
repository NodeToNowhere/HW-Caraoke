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

        self.room = Room(
            "Green"
        )  # had to instantiate room object for test on list to work.

    def test_guest_list_length(self):
        self.room.add_guests(self.guest_1)
        expected = 1
        actual = len(self.room.guest_list)
        self.assertEqual(expected, actual)

    def test_room_is_full(self): #how to reset unit tests
        self.room.add_guests(self.guest_1)
        self.room.add_guests(self.guest_2)
        self.room.add_guests(self.guest_3)
        self.room.add_guests(self.guest_4)
        self.room.add_guests(self.guest_5)
        self.room.add_guests(self.guest_6)

        expected = "Limit reached only 5 allowed"
        actual = self.room.add_guests(self.guest_6)

        self.assertEqual(expected, actual)
