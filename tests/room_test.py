import unittest
from src.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Green")

    def test_room_has_name(self):
        expected = "Green"
        actual = self.room.name
        self.assertEqual(expected, actual)

    # def test_room_is_occupied(self):
    #     expected = True
    #     actual = self.room.occupied
    #     self.assertEqual(expected, actual)
