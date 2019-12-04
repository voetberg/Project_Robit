from project_robit.Engine.cards import Cards
from unittest import TestCase

class TestCards(TestCase):
    def setUp(self):
        self.deck = Cards("stars")

    def test_make_deck(self):
        expected = {}
        #Generate a json with each deck, load in the accessor class
        self.assertEqual(expected, self.deck)

    def test_get_card_disciption(self):
        expected = {

        }
        card = self.deck[0]
        self.assertEqual(expected,card)

    def test_get__defence_buff_effect(self):
        self.assertEqual(1,self.deck[0].defence_buff)

    def test_get_attack_buff_effect(self):
        self.assertEqual(1, self.deck[0].attack_buff)

    def test_get_attack_effect(self):
        self.assertEqual(1,self.deck[0].attack)

    def test_get_heal_effect(self):
        self.assertEqual(1,self.deck[0].heal)

    def remove_card_from_deck(self):
        self.deck.drop_card[0]
        self.assertEqual(12,len(self.deck))