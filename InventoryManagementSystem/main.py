from item import Item
from inventory import Inventory


def main():
    inventory = Inventory()
    
    print("\nNepali-Mart Manager")
    print("===================\n")
    
    while (True):
        print()
        print("Choose a Task:")
        print("==============")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. View Item")
        print("5. Exit\n")
        
        
        user_choice = int(input("Enter your choice (1-5): "))
        print()
        
        if (user_choice == 1):
            name = input("\tEnter name of item: ")
            category = input("\tEnter category of item: ")
            quantity = int(input("\tEnter qantity to be added: "))
            price = float(input("\tEnter price per item: "))
            
            inventory.add_item(name,category,quantity,price)
            
        elif(user_choice == 2):
            name = input("\tEnter name of item to remove: ")
            inventory.remove_item(name)
            
        elif(user_choice == 3):
            name = input("\tEnter name of item to update: ")
            
            update_quantity = input("\n\tDo you want to udpate quantity? (yes/no): ").lower()
            if update_quantity == "yes":
                quantity = int(input(f"\t\tEnter new quantity of '{name}': "))
                inventory.update_item(name,quantity,None)
                
                
            update_price = input("\n\tDo you want to udpate price? (yes/no): ").lower()
            if update_price == "yes":
                price = float(input(f"\t\tEnter new price of '{name}': "))
                inventory.update_item(name,None,price)
                
        elif(user_choice == 4):
            
            inventory.view_item()
            
        elif(user_choice == 5):
            inventory.save_inventory()
            print("\nExitting...")
            break
        
        else:
            print("\n Invalid input.")
            
        
    
if __name__ == "__main__":
    main()