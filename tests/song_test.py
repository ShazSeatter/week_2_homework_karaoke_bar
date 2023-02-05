import unittest
from src.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Hound Dog", "Elvis Presley", "Rock")

    def test_song_has_title(self):
        expected = "Hound Dog"
        actual = self.song.title
        self.assertEqual(expected, actual)

    def test_song_has_artist(self):
        expected = "Elvis Presley"
        actual = self.song.artist
        self.assertEqual(expected, actual)