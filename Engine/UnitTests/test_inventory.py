from unittest import TestCase
from project_robit.Engine.inventory_system import Inventory


class TestInventory(TestCase):
    def setUp(self):
        self.inventory = Inventory

    def test_add_item(self):
        self.inventory.add_item(inventory)

    def test_remove_item(self):
        pass

    def test_exceed_inventory_space(self):
        pass

    def test_display_all_names(self):
        pass

    def test_give_item_discription(self):
        pass
