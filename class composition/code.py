class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books"



class Book:
    def __init__(self,name,):
        self.name = name

    def __str__(self):
        return f"Book: {self.name}"


book = Book("Python Programming")  # Create an instance of Book
book1 = Book("Learning Python")  # Create another instance of Book
shelf = BookShelf(book, book1)  # Create a BookShelf instance with the books
print(shelf)  # This will print the BookShelf object using the __str__ method