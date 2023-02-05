import unittest
from src.room import Room
from src.song import Song


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

    def test_add_songs_to_room(self):
        song = Song("Hound Dog", "Elvis Presley", "Rock")
        self.room.add_song(song)
        expected = song
        actual = self.room.songs[0]
        self.assertEqual(expected, actual)

    def test_can_find_song_by_title__not_found(self):
        expected = None
        actual = self.room.find_song_by_title("Hound Dog")
        self.assertEqual(expected, actual)
    
    def test_can_find_song_by_title__found(self):
        song = Song("Hound Dog", "Elvis Presley", "Rock")
        self.room.add_song(song)
        expected = song.title
        actual = self.room.find_song_by_title("Hound Dog")
        self.assertEqual(expected, actual)

