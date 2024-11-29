from item import Item
import json
import os

class Inventory:
    def __init__(self,filename="inventory.json"):
        self.items = []
        self.filename = filename
        self.load_inventory()
        
        
    def add_item(self,name,category,quantity,price):
        item = Item(name,category,quantity,price)
        self.items.append(item)
        self.save_inventory()
        print(f"\nAdded '{name}' to the inventory.")
        
    def remove_item(self,name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                self.save_inventory()
                print(f"\nRemoved '{name}' from the inventory.")
                return
        print(f"\nItem not found.")
        
    def update_item(self,name,quantity = None, price = None):
        for item in self.items:
            if item.name == name:
                if quantity is not None:
                    item.quantity = quantity
                    
                if price is not None:
                    item.price = price
                    
                self.save_inventory()
                print(f"\nUpdated {name}'s details.")
                return
        print(f"\nItem not found.")
        
    
    def view_item(self):
        if len(self.items) == 0:
            print("\nNo items in the inventory.")
        else:
            print("\nInventory")
            print("=========")
            for item in self.items:
                print(item)
                
    def save_inventory(self):
        
        data = [item.to_dict() for item in self.items]
        
        with open(self.filename, "w") as file:
            json.dump(data,file,indent = 4)
        
            
    def load_inventory(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.items = [Item.from_dict(item) for item in data]
        else:
            print("File not found. Starting Fresh....")
        
        
        
            
    
        
        
        
            
                
        
                
            
        
    
                
        