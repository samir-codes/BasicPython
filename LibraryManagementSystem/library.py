from book import Book
import json
import os


class Library:
    def __init__(self,filename = "library.json"):
        self.books = []
        self.filename = filename
        self.load_books()
        
    def add_books(self,title,author):
        book = Book(title,author)
        self.books.append(book)
        print(f"\n'{title}' by '{author}' added.")
        
    def borrow_books(self,title):
        for book in self.books:
            if book.title == title.lower():
                if book.status == "available":
                    book.status = "borrowed"
                    print(f"\nYou have successfully borrowed the book '{title}'")
                    return
                else:
                    print(f"\n'{title}' already borrowed.")
                    return
        
        print(f"\n'{title}' not found")
        

    def return_books(self,title):
        for book in self.books:
            if book.title == title.lower():
                if book.status == "borrowed":
                    book.status = "available"
                    print(f"\nYou have successfully returned the book '{title}'.")
                    return
                else:
                    print(f"\nThe book was not borrowed.")
                    return
        print(f"\n'{title}' not found!")
                    
    
    def view_books(self):
        print("\nAvailable Books")
        print("===============\n")
        
        for book in self.books:
            if book.status == "available":
                print(f" - {book}")
                
        print("\nBorrowed Books")
        print("===============\n")
        
        for book in self.books:
            if book.status == "borrowed":
                print(f" - {book}")
        
    def remove_books(self,title):
        for book in self.books:
            if book.title == title.lower():
                if book.status == "available":
                    self.books.remove(book)
                    print(f"\nBook named '{title}' is removed.")
                    return
                elif book.status == "borrowed":
                    print("\nBook must be returned to the Library!!!")
                    return
        print(f"{title} not found.")
            
    
    def save_books(self):
        # Save the current list of books to the json file
        
        data = [book.to_dict() for book in self.books]
        
        
        with open(self.filename, 'w') as file:
            json.dump(data,file,indent = 4)
            
        # print("\nlibrary Saved Successfully.")
    
    
    def load_books(self):
        #load books from the JSON file if it exists
        
        if os.path.exists(self.filename):
            with open(self.filename,'r') as file:
                data = json.load(file)
                self.books = [Book.from_dict(book) for book in data]
            
            # print("\nLibrary Loaded Successfully.")
            
        else:
            print("\nNo Saved Library Found. Starting Fresh...")
        
        
                
        
                
                
        
                
            
    