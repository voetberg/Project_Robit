from project_robit.Engine.resource_accessor import ResourceAccessor
from project_robit.Engine.cards import Card

class Inventory:
    def __init__(self):
        self.inventory = {}
        self.max_item_number = 12

    def get_item_names(self):
        item_name_list = []
        for item in self.inventory:
            item_object = Items(item)
            item_name_list.append(item_object.name)
        return item_name_list

    def get_inventory_size(self):
        return len(self.inventory)

    def add_item(self,item):
        if self.get_inventory_size() >= self.max_item_number:
            return "Inventory Full"
        else:
            item_object = Items(item)
            self.inventory[item] = item_object

    def remove_item(self,item):
        self.inventory.pop(item)

    def get_item_descriptions(self):
        item_description_list = []
        for item in self.inventory:
            item_object = Items(item)
            item_description_list.append(item_object.description)
        return item_description_list

    def get_item_stats(self):
        item_stat_list = []
        for item in self.inventory:
            item_object = Items(item)
            item_stat_list.append({

            })
        return item_stat_list

class Items(Card):
    def __init__(self,item):
        ##TODO Treat this as a card
        #You know. Right. 
        all_items = ResourceAccessor(resource="Items").resource
        item_object = all_items[item]
        self.item = self.Card(item_object)
