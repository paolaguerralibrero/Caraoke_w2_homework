import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Percy Sledge", "The dark end of the street")

    def test_has_artist(self):
        self.assertEqual("Percy Sledge", self.song.artist)

    def test_has_title(self):
        self.assertEqual("The dark end of the street", self.song.title)