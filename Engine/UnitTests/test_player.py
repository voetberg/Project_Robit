from unittest import TestCase
from project_robit.Engine.player import Player

class TestPlayer(TestCase):
    def setUp(self):
        self.joker = Player(money=5)

    def test_buy(self):
        self.joker.use_money(-3)
        self.assertEqual(2,self.joker.money)

    def test_sell(self):
        self.joker.use_money(2)
        self.assertEqual(7,self.joker.money)

    def test_pass_money_limit(self):
        self.joker.use_money(-7)
        self.assertEqual(5,self.joker.money)

    def test_gain_suit(self):
        self.joker.gain_suit()
        expected = {}
        self.assertEqual(expected, self.joker.suits)

    def test_loose_suit(self):
        self.joker.lose_suit()
        expected = {}
        self.assertEqual(expected,self.joker.suits)

    def test_loose_nonexistant_suit(self):
        expected = self.joker.suits
        self.joker.lose_suit()
        self.assertEqual(expected,self.joker.suits)

    def test_gain_inventory_item(self):
        expected = {}
        self.joker.access_inventory("placeholder_item", action='add')
        self.assertEqual(expected,self.joker.inventory)

    def test_loose_inventory_item(self):
        expected = {}
        self.joker.access_inventory("removed_item", action='remove')
        self.assertEqual(expected,self.joker.inventory)

    def test_loose_item_not_in_inventory(self):
        expected = {}
        self.joker.access_inventory("Not_An_Item",action='remove')
        self.assertEqual(expected,self.joker.inventory)


    #TODO Write movement cases

