import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.person = Guest("Mary", 50)

    def test_has_name(self):
        self.assertEqual("Mary", self.person.name)

    def test_guest_has_wallet(self):
        self.assertEqual(50, self.person.wallet)

    