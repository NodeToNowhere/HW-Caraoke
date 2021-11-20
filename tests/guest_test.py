import unittest

from src.guest import Guests


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guests("Betty", 5.43)

    def test_guest_has_name(self):
        expected = "Betty"
        actual = self.guest.name
        self.assertEqual(expected, actual)

    def test_guest_has_money(self):
        expected = True
        actual = self.guest.wallet > 0
        self.assertEqual(expected, actual)
        
