from .resource_accessor import ResourceAccessor


class Cards:
    def __init__(self,suit):
        resources = ResourceAccessor("cards")
        self.deck = resources[suit]

    def get_card(self,card_number):
        return Card(self.deck[card_number])

    def drop_card(self,card_number):
        self.deck.pop(card_number)


class Card:
    def __init__(self,card):
        self.attack = card['attack']
        self.heal = card['heal']
        self.defense_buff = card['defense_buff']
        self.attack_buff = card['attack_buff']




