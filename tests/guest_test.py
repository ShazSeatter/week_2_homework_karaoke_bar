import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("John Smith", 50)

    def test_guest_has_name(self):
        expected = "John Smith"
        actual = self.guest.name
        self.assertEqual(expected, actual)