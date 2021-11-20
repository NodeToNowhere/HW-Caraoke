import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("song1", 3.5)
        
    
    def test_song_has_name(self):
        expected = "song1"
        actual = self.song.name
        self.assertEqual(expected, actual)
        
    def test_song_has_duration(self):
        expected = 3.5
        actual = self.song.duration
        self.assertEqual(expected, actual)
    