import unittest

from src.guest import Guests
from src.room import Room
from src.song import Song


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.room = Room("Green")

        self.song_1 = Song("War Pig", 451)
        self.song_2 = Song("War Fig", 345)

        self.guest_1 = Guests("Betty", 4.51, "War Pig")
        self.guest_2 = Guests("Ben", 3.23, "War Fig")
        self.guest_3 = Guests("Bill", 9.23, "War Gig")

    def test_guest_has_name(self):
        expected = "Betty"
        actual = self.guest_1.name
        self.assertEqual(expected, actual)

    def test_guest_has_wallet(self):
        expected = True
        actual = self.guest_1.wallet > 0
        self.assertEqual(expected, actual)

    def test_has_favorite_song(self):
        expected = "War Pig"
        actual = self.guest_1.favorite_song
        self.assertEqual(expected, actual)

    def test_room_plays_favorite_song_true(self):
        self.room.add_song(self.song_1)
        self.room.add_song(self.song_2)
        self.room.add_guests(self.guest_1)
        
        expected = "Betty: Oh yeah! War Pig is my jam!"
        actual = self.guest_1.guest_check_song_list(self.guest_1, self.room.song_list)
        self.assertEqual(expected,actual)
        

    def test_room_plays_favorite_song_false(self):
        self.room.add_song(self.song_1)
        self.room.add_song(self.song_2)
        self.room.add_guests(self.guest_3)
        
        expected = "Bill: This music sucks..."
        actual = self.guest_1.guest_check_song_list(self.guest_3, self.room.song_list)
        self.assertEqual(expected,actual)
        
        
