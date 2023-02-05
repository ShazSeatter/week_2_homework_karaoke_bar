import unittest
from src.guest import Guest
from src.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("John Smith", 50)
        self.room = Room(20)

    def test_guest_has_name(self):
        expected = "John Smith"
        actual = self.guest.name
        self.assertEqual(expected, actual)

    def test_guest_has_cash_in_wallet(self):
        expected = 50
        actual = self.guest.cash
        self.assertEqual(expected, actual)

    def test_guest_has_enough_cash_in_wallet_for_karaoke_room__True(self):
        expected = True
        actual = self.guest.enough_cash_for_karaoke_room(self.guest.cash, self.room.price)
        self.assertEqual(expected, actual)

    def test_guest_has_enough_cash_in_wallet_for_karaoke_room__False(self):
        guest = Guest("Jane Doe", 2)
        expected = False
        actual = self.guest.enough_cash_for_karaoke_room(guest.cash, self.room.price)
        self.assertEqual(expected, actual)

    def test_guest_can_reduce_cash_by_entry_fee(self):
        self.guest.reduce_cash(self.guest.cash, self.room.entry_fee)
        expected = 45
        actual = self.guest.cash
        self.assertEqual(expected, actual)

    def test_guest_can_reduce_cash_by_entry_fee__insufficent_funds(self):
        guest = Guest("Jane Doe", 2)
        expected = "You can't afford the entry fee"
        actual = self.guest.reduce_cash(guest.cash, self.room.entry_fee)
        self.assertEqual(expected, actual)

    # def reduce_cash(self, amount):
    #     self.cash -= amount

    #     def test_customer_can_reduce_cash(self):
    #     self.customer.reduce_cash(500)
    #     self.assertEqual(500, self.customer.cash)