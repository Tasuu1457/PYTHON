class Library:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
class Books:
    def __init__(self):
        self.books = []
        
    def add_books(self, title, author):
        self.title = title
        self.author = author
        new_books = Library(title, author)
        self.books.append(new_books)
        print(f"{title} {author}, books added successfuly!")
        
    def return_books(self, title, author):
        self.title = title
        self.author = author
        return_books = Library(title, author)
        self.books.append(return_books)
        print(f"{title} {author}, books return successfuly!")
        
    def list_all_books(self):
        if not self.books:
            print("No books found in the library.")
        else:
            for book in self.books:
                print(f"Book name: {book.title}, {book.author}")


if __name__ == "__main__":
    my_library = Books()
    
    my_library.add_books("Harry Potter and The Sorcerer's Stone", "J.K Rowling")
    my_library.add_books("Pride and Prejudice", "Jane Austen")
    my_library.add_books("To Kill a Mockingbird", "Harper Lee")
    
    print()
    
    my_library.return_books("The Lord of the Rings", "J.R.R. Tolkien")
    my_library.return_books("1984", "George Orwell")
    my_library.return_books("The Catcher in the Rye", "J.D. Salinger")
    
    print()
    
    my_library.list_all_books()