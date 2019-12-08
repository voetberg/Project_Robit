from project_robit.Engine.cards import Cards
from project_robit.Engine.inventory_system import Inventory
from project_robit.Engine.resource_accessor import ResourceAccessor

import random

class Suits:
    def __init__(self, area=False,
                 character="Character"):
        self.resource = ResourceAccessor(area=area, resource="Suits").resource[character]

        suit = self.resource["deck"]
        self.deck = Cards(suit=suit).deck

        self.hp = self.resource["base_hp"]
        self.hand_size = self.resource["hand_size"]
        self.attack = self.resource["base_attack"]
        self.defense = self.resource["base_attack"]
        self.status = self.resource["life_status"]

        self.hand = {}
        self.inventory = Inventory()

    def draw_hand(self):
        ##TODO Discard hand
        if len(self.hand) > self.hand_size:
            self.hand = dict(random.sample(self.deck.items(), self.hand_size))
        else:
            self.hand = self.deck

    def discard_hand(self):
        self.hand = {}

    def use_card(self, card, target):
        self.take_damage(card.attack, target)
        self.heal(card.heal,target)
        buff_dictionary = {
            "defense": card.defense_buff,
            "attack": card.attack_buff
        }
        self.buff(buff_dictionary,target)
        self.deck.drop_card()

    def use_item(self,item,target):
        self.use_card(item,target=target)
        self.inventory.remove_item(item)

    def heal(self,heal_amount,target):
        post_heal_hp = target.hp + heal_amount
        if target.status == "living":
            if post_heal_hp > self.resource["base_hp"]:
                target.hp = self.resource["base_hp"]
            else:
                target.hp = post_heal_hp
        else:
            target.hp = 0

    def take_damage(self,damage_amount,target):
        ##TODO Damage Formula
        target.hp -= damage_amount
        if target.hp < 0:
            target.status = "dead"
            target.hp = 0

    def buff(self,buff_dictionary,target):
        for buff_action in buff_dictionary.items():
            if buff_action[0] == "defense":
                target.defense *= buff_action[1]
            if buff_action[0] == "attack":
                target.attack *= buff_action[1]

    def revive(self,target):
        if target.status == "dead":
            target.hp = int(self.resource["base_hp"]/2)
            target.status = "living"

