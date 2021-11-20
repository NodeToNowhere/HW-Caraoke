import unittest

from src.guest import Guests


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guests("Betty")

    def test_guest_has_name(self):
        expected = "Betty"
        actual = self.guest.name
        self.assertEqual(expected, actual)
