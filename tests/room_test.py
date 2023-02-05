import unittest
from src.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(20)

    def test_price_of_room(self):
        expected = 20
        actual = self.room.price
        self.assertEqual(expected, actual)