class TooManyPagesReadError(ValueError): # This custom error is raised when the number of pages read exceeds the total number of pages in the book.
    pass 

class Book:
    def __init__(self,name:str,page_count:int):
        self.name = name # This initializes the book with a name and a page count.
        self.page_count = page_count # This initializes the book with a name and a page count.
        self.pages_read = 0 # This initializes the book with a name and a page count.

    def __repr__(self): 
        return ( f"Book{self.name}({self.page_count} pages, {self.pages_read} read)" )  
    
    def read(self, pages:int): 
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(f"You cannot read more than {self.page_count} pages.") # This raises an error if the number of pages read is greater than the number of pages in the book.
        self.pages_read += pages # This increments the number of pages read by the specified amount.
        print(f"You have read {self.pages_read} pages of {self.name}.")  # This prints the number of pages read.


python101 = Book("Python 101", 50)  # This creates a new Book object with the name "Python 101" and 300 pages.

try:
    python101.read(35)  # This reads 50 pages of the book.        
    python101.read(50)  # This reads 50 pages of the book.      
except TooManyPagesReadError as e:
    print(e)

