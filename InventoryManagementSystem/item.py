class Item:
    def __init__(self,name,category,quantity,price):
        self.name = name.lower()
        self.category = category.lower()
        self.quantity = quantity.lower()
        self.price = price.lower()
        
    # convert item to dictionary for saving to JSON file
    def to_dict(self):
        return {
            "name" : self.name,
            "category" : self.category,
            "quantity" : self.quantity,
            "price" : self.price
        }
        
    # create item object from the dictionay
    @classmethod
    def from_dict(cls,data):
        return cls(data["name"],data["category"],data["quantity"],data["price"])
    
    def __str__(self):
        return f'Item (Name : "{self.name.capitalize()}", Category: "{self.category.capitalize()}", Quantity: {self.quantity}, Price: ${self.price:.2f})'
        
        

