## Class for a player
    ## Holds the parameters a player can have


class Player:
    def __init__(self, money=0, suits={}, position=(0,0,0), inventory={}):
        self.money = money
        self.suits = suits
        self.position = position
        self.inventory = inventory

    def use_money(self, money_change):
        self.money += money_change

    def move(self, x_pos, y_pos, screen):
        self.position[0] += x_pos
        self.position[1] += y_pos
        self.position[2] += screen

    def add_item(self,item):
        self.inventory[-1] = item
