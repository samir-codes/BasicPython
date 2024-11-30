from item import Item
import json
import os


def log_action(action):
    """Decorator to log actions performed in the inventory."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"\nAction: {action}")
            result = func(*args, **kwargs)
            print(f"Action '{action}' completed successfully.")
            return result
        return wrapper
    return decorator

def handle_errors(func):
    """Decorator to handle exceptions."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
    return wrapper





class Inventory:
    def __init__(self,filename="inventory.json"):
        self.items = []
        self.filename = filename
        self.load_inventory()
        
    
    @log_action("Adding an item")
    @handle_errors
    def add_item(self,name,category,quantity,price):
        name = name.strip().lower()
        item = Item(name,category,quantity,price)
        self.items.append(item)
        self.save_inventory()
        print(f"Added '{name}' to the inventory.")
    
    
    @log_action("Removing an item")
    @handle_errors
    def remove_item(self,name):
        name = name.strip().lower()
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                self.save_inventory()
                print(f"Removed '{name}' from the inventory.")
                return
        print(f"Item not found.")
    
    
    
    @log_action("Updating an item")
    @handle_errors    
    def update_item(self,name,quantity = None, price = None):
        name = name.strip().lower()
        for item in self.items:
            if item.name == name:
                if quantity is not None:
                    item.quantity = quantity
                    
                if price is not None:
                    item.price = price
                    
                self.save_inventory()
                print(f"Updated {name}'s details.")
                return
        print(f"Item not found.")
        
    
    
    
    
    @log_action("Viewing items")
    @handle_errors
    def view_item(self):
        if len(self.items) == 0:
            print("No items in the inventory.")
        else:
            print("\nInventory")
            print("=========")
            for item in self.items:
                print(item)
    
    
    @handle_errors         
    def save_inventory(self):
        
        data = [item.to_dict() for item in self.items]
        
        with open(self.filename, "w") as file:
            json.dump(data,file,indent = 4)
        
    
    @handle_errors
    def load_inventory(self):
        if os.path.exists(self.filename):
            
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.items = [Item.from_dict(item) for item in data]
            
        else:
            print("File not found. Starting Fresh....")
        
        
        
            
    
        
        
        
            
                
        
                
            
        
    
                
        