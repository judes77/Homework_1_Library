library = {
    "name": "CodeClan Library",
    "books": [
        {
            "author": "George RR Martin",
            "title": "A Song of Ice and Fire"
        },
        {
            "author": "J R. R. Tolkien",
            "title": "The Hobbit"
        },
        {
            "author": "Paul Barry",
            "title": "Head-First Python"
        },
        {
            "author": "Allen B. Downey",
            "title": "Think Python: How to Think Like a Computer Scientist"
        },
        {
            "author": "Eric Matthes",
            "title": "Python Crash Course"
        }
    ]
}

# TODO - Print welcome statement including library name
print(f"Welcome everyone to {library['name']}")

option = ""
while option != "q":
    print("Options:")
    print("1 - List all books")
    print("2 - Search for a book by title")
    print("3 - Add a book")
    print("4 - Remove a book")
    print("5 - Update a book")
    print("q - Quit")
    option = input("What would you like to do? \n")
    
    
    if option == "1":
        print("Listing all books...")
        for book in library["books"]:
            print(f"{book['title']} by {book['author']}")

    # TODO - List all books
    

    if option == "2":
        print("Searching for a book by title...")
        title_to_search_for = input("Which book would you like to search for? ")
        book_found = None
        for book in library["books"]:
            if title_to_search_for == book["title"]:
                 book_found = book
                 print(f"{book['title']} by {book['author']}")
        else:
            print("Book not found.")
        # TODO - Search for a book by title

    if option == "3":
        print("Adding a book...")
        add_book = input("Which book would you like to add? ")
        
        


         
    
    if option == "4":
        print("Removing a book...")
        book_to_remove = input("Which book would you like to remove? ")

            # TODO - Remove a book

    if option == "5":
        print("Updating a book...")
        # TODO - Update a book