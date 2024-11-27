class Book:
    def __init__(self,title,author,status = "available"):
        self.title = title.lower()
        self.author = author.lower()
        self.status = status.lower()
        
    def to_dict(self):
        #Convert the book object into dictionary
        return {
            "title" : self.title,
            "author" : self.author,
            "status" : self.status,
        }
    
    @classmethod  
    def from_dict(cls,data):
        #Create a Book object from a dictionary.
        return cls(data["title"],data["author"],data["status"])
        
    def __str__(self):
        return f"{self.title.capitalize()} by {self.author.capitalize()} - {self.status.capitalize()}"
    





