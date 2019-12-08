from unittest import TestCase
from project_robit.Engine.suits import Suits

class TestSuits(TestCase):
    def setUp(self):
        self.user_suit = Suits(area="Area0", character="Deuce")
        self.enemy_suit = Suits(area="Area0", character="Deuce")
        #TODO Init should call the resource class

    def test_get_hand_size(self):
        self.assertEqual(1, self.user_suit.hand_size)

    def test_draw_new_hand(self):
        self.user_suit.draw_hand()
        self.assertEqual(self.user_suit.hand_size, len(self.user_suit.hand))

    def test_use_card(self):
        self.user_suit.draw_hand()
        card_to_use = self.user_suit.hand[0]
        expected_enemy_hp = self.enemy_suit.hp - card_to_use["damage"]
        self.user_suit.use_card(card=card_to_use, target=self.enemy_suit)
        self.assertEqual(expected_enemy_hp, self.enemy_suit.hp)

    def test_use_item(self):
        self.user_suit.inventory.add_item('trash')
        self.user_suit.use_item(self.user_suit.inventory.inventory['trash'],self.user_suit)
        self.assertEqual(0,self.user_suit.inventory.get_inventory_size())

    def test_discard_hand(self):
        self.user_suit.draw_hand()
        self.user_suit.discard_hand()
        self.assertEqual(0,len(self.user_suit.hand))

    def test_take_damage(self):
        hp = self.user_suit.hp
        self.user_suit.take_damage(1,self.user_suit)
        self.assertEqual(hp-1,self.user_suit.hp)

    def test_die(self):
        self.user_suit.take_damage(self.user_suit.hp+1,self.user_suit)
        self.assertEqual("dead",self.user_suit.status)

    def test_heal(self):
        self.user_suit.hp = 16
        self.user_suit.take_damage(12,self.user_suit)
        self.user_suit.heal(12,self.user_suit)
        self.assertEqual(1,self.user_suit.hp)

    def test_heal_beyond_limit(self):
        self.user_suit.hp = 16
        self.user_suit.take_damage(1,target=self.user_suit)
        self.user_suit.heal(1000,self.user_suit)
        self.assertEqual(1,self.user_suit.hp)

    def test_heal_dead_unit(self):
        self.user_suit.status = "dead"
        self.user_suit.heal(10000,self.user_suit)
        self.assertEqual(0,self.user_suit.hp)

    def test_revive(self):
        base_hp = self.user_suit.hp
        self.user_suit.status = "dead"
        self.user_suit.revive(self.user_suit)
        self.assertEqual(int(base_hp/2),self.user_suit.hp)

    def test_buff_defence(self):
        self.user_suit.buff({"defence":.5},self.enemy_suit)
        self.assertEqual(.5,self.user_suit.defense)
