import unittest

from src.guest import Guests
from src.room import Room
from src.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Green")

        self.song_1 = Song("War Pig", 451)
        self.song_2 = Song("War Fig", 345)
        self.song_3 = Song("War Gig", 286)
        self.song_4 = Song("War Big", 511)
        self.song_5 = Song("War Wig", 365)

        self.guest_1 = Guests("Betty", 4.51, "War Pig")
        self.guest_2 = Guests("Ben", 3.23, "War Fig")
        self.guest_3 = Guests("Bill", 9.23, "War Gig")
        self.guest_4 = Guests("Bob", 1.11, "War Big")
        self.guest_5 = Guests("Biff", 0, "War Wig")
        self.guest_6 = Guests("Brian", 0.12, "War Wig")

    def test_room_has_name(self):
        expected = "Green"
        actual = self.room.name
        self.assertEqual(expected, actual)

    def test_room_can_add_song(self):
        self.room.add_song(self.song_1)

        expected = "War Pig"
        actual = self.room.add_song(self.song_1)

    def test_guest_list_length(self):
        self.room.add_guests(self.guest_1)
        expected = 1
        actual = len(self.room.guest_list)
        self.assertEqual(expected, actual)
        self.room.guest_list.clear()  # --What is proper way to clear unit tests

    def test_room_is_full(self):
        self.room.add_guests(self.guest_1)
        self.room.add_guests(self.guest_2)
        self.room.add_guests(self.guest_3)
        self.room.add_guests(self.guest_4)
        self.room.add_guests(self.guest_5)
        self.room.add_guests(self.guest_6)

        expected = "Limit reached only 5 allowed"
        actual = self.room.add_guests(self.guest_6)

        self.assertEqual(expected, actual)

    def test_group_has_enough_money_for_room(self):
        self.room.add_guests(self.guest_1)
        self.room.add_guests(self.guest_2)
        self.room.add_guests(self.guest_3)
        self.room.add_guests(self.guest_4)
        self.room.add_guests(self.guest_5)

        expected = True
        actual = self.room.group_money_check(self.room.guest_list)
        self.assertEqual(expected, actual)

    

    
