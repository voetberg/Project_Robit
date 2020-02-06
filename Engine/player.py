from . resource_access import Resource_Manager

class Player:
    def __init__(self, day='0', character=''):
        self.name = character
        self.hp = 6
        self.deck = Resource_Manager(['Cards',day, character]) # TODO Make sure this is a good naming method
        self.won = False

