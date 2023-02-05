import unittest
from src.karaoke_bar import KaraokeBar


class TestKaraokeBar(unittest.TestCase):
    def setUp(self):
        self.karaoke_bar = KaraokeBar("CodeClan Caraoke", 1000)

    def test_karaoke_bar_has_name(self):
        expected = "CodeClan Caraoke"
        actual = self.karaoke_bar.name
        self.assertEqual(expected, actual)

    
    def test_karaoke_bar_has_money(self):
        expected = 1000
        actual = self.karaoke_bar.total_cash
        self.assertEqual(expected, actual)

    
