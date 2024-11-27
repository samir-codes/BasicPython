from book import Book
from library import Library

def main():
    
    library = Library()
    
    while True:
    
        print('\nWelcome to "PUSTAKALAYA"!')
        print("=========================\n")
            
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Books")
        print("5. Remove Book")
        print("6. Exit")    
                
        choice = int(input("\nEnter you choice: "))
        
        if (choice == 1):
            title = input("\n\tEnter the book title: ")
            author = input("\tEnter name of author: ")
            library.add_books(title,author)
            library.save_books()
            
        elif (choice == 2):
            title = input("\n\tEnter title of the book to borrow: ")
            library.borrow_books(title)
            library.save_books()
            
        elif (choice == 3):
            title = input("\n\tEnter books to return: ")
            library.return_books(title)
            library.save_books()
            
        elif (choice == 4):
            library.view_books()
            
        elif (choice == 5):
            title = input("\n\tEnter title of book to remove: ")
            library.remove_books(title)
            library.save_books()
            
        elif (choice == 6):
            library.save_books()
            print("\nThank you for using our application.\n")
            break
            
        else:
            print("\nPlease privide valid input.")
    
    
    

if __name__ == "__main__":
    main()