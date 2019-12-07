from project_robit.Engine.cards import Cards
from project_robit.Engine.resource_accessor import ResourceAccessor


class Suits:
    def __init__(self, area=False,
                 character="Character"):
        resource = ResourceAccessor(area=area, resource="Suits").resource[character]

        suit = resource["deck"]
        self.deck = Cards(suit=suit).deck

        self.hp = resource["base_hp"]
        self.hand_size = resource["hand_size"]
        self.attack = resource["base_attack"]
        self.defense = resource["base_attack"]
        self.status = resource["life_status"]

        self.hand = {}
        self.inventory = {}

    def draw_hand(self):
        return ""

    def discard_hand(self):
        pass

    def use_card(self,card,target):
        pass

    def use_item(self,item):
        pass

    def heal(self,heal_amount):
        pass

    def take_damage(self,damage_amount):
        pass

    def buff(self,buff_amount):
        pass

    def revive(self):
        pass

