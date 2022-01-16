import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room(2, 10)
       
    def test_add_guest(self):
        guest1 = Guest("Harry", 50)
        guest2 = Guest("Sam", 30)
        self.room.add_guest(guest1)
        self.room.add_guest(guest2)
        self.assertEqual(2, len(self.room.guests))

    def test_check_out_guest(self):
        guest1 = Guest("Harry", 50)
        self.room.add_guest(guest1)
        self.room.check_out_guest(guest1)
        self.assertEqual(0, len(self.room.guests))

    def test_add_song(self):
        song1 = Song("Percy Sledge", "The dark end of the street")
        song2 = Song("Zenet", "Contigo")
        self.room.add_song(song1)
        self.room.add_song(song2)
        self.assertEqual(2, len(self.room.songs))

    def test_room_space(self):
        self.assertEqual(2, self.room.space)

    def test_room_no_space(self):
        guest1 = Guest("Harry", 50)
        guest2 = Guest("Sam", 30)
        guest3 = Guest("Luna", 70)
        song = Song("Percy Sledge", "The dark end of the street")
        self.room = Room(2, 10)
        self.room.add_guest(guest1)
        self.room.add_guest(guest2)
        self.room.room_no_space()
        self.assertEqual("Room is full", self.room.room_no_space())

    def test_guest_can_afford_entry_fee(self):
        guest1 = Guest("Harry", 20)
        self.room = Room(2, 10)
        self.room.add_guest(guest1)
        self.room.can_affod_entry_fee(guest1)
        self.assertEqual(True, self.room.can_affod_entry_fee(guest1))



   