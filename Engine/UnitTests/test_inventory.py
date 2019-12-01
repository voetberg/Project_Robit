from unittest import TestCase
from project_robit.Engine.inventory_system import Inventory


class TestInventory(TestCase):
    def setUp(self):
        self.inventory = Inventory

    def test_add_item(self):
        self.inventory.add_item("trash")
        self.assertEqual(1,self.inventory.size)

    def test_remove_item(self):
        self.inventory.add_item("trash")
        self.inventory.remove_item("trash")
        self.assertEqual(0,self.inventory.size)

    def test_exceed_inventory_space(self):
        for _ in range(0,self.inventory.max_item_number):
            self.inventory.add_item("trash")
        expected = "Inventory Full"
        self.assertEqual(expected,self.inventory.add_item("trash"))

    def test_display_all_names(self):
        self.inventory.add_item("trash")
        expected = ["Trash"]
        self.assertEqual(expected,self.inventory.item_names)

    def test_give_item_discription(self):
        self.inventory.add_item("trash")
        expected = ["It's Trash"]
        self.assertEqual(expected,self.inventory.item_descriptions)

    def test_give_item_stats(self):
        self.inventory.add_item("trash")
        expected = [{
            
        }]
        self.assertEqual(expected,self.inventory.item_stats)
