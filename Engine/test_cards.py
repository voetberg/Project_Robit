from project_robit.Engine.cards import Cards
from unittest import TestCase

class TestCards(TestCase):
    def setUp(self):
        self.deck = Cards("stars")
        self.card = self.deck.get_card("base")

    def test_make_deck(self):
        expected = {
          "base": {
            "description": "Can I call this an easter egg",
            "attack": 0,
            "heal": 0,
            "defense_buff": 1,
            "attack_buff": 1
          }
        }
        #Generate a json with each deck, load in the accessor class
        self.assertEqual(expected, self.deck.deck)

    def test_get_card_disciption(self):
        expected = "Can I call this an easter egg"
        self.assertEqual(expected,self.card.description)

    def test_get__defence_buff_effect(self):
        self.assertEqual(1,self.card.defense_buff)

    def test_get_attack_buff_effect(self):
        self.assertEqual(1, self.card.attack_buff)

    def test_get_attack_effect(self):
        self.assertEqual(0,self.card.attack)

    def test_get_heal_effect(self):
        self.assertEqual(0,self.card.heal)

    def remove_card_from_deck(self):
        self.deck.drop_card(0)
        self.assertEqual(12,len(self.deck))