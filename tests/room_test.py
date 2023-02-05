import unittest
from src.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(20)

    def test_price_of_room(self):
        expected = 20
        actual = self.room.price
        self.assertEqual(expected, actual)

    def test_has_songs(self):
        expected = []
        actual = self.room.songs
        self.assertEqual(expected, actual)

    def test_has_guests(self):
        expected = []
        actual = self.room.guests
        self.assertEqual(expected, actual)


    # def test_add_songs_to_room(self):
    #     self.song = Song()