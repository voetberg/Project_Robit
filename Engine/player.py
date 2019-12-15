## Class for a player
    ## Holds the parameters a player can have
from project_robit.Engine.inventory_system import Inventory
from project_robit.Engine.suits import Suits

class Player:
    def __init__(self, money=0, suits=Suits(area="Area0",character="Deuce"), position=(0,0,0), inventory=Inventory()):
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

    def access_inventory(self,item,action):
        if action == "add":
            self.inventory.add_item(item)
        if action == "remove":
            self.inventory.remove_item(item)

    def save(self):
        pass
