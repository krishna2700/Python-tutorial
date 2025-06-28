class ClassTest:
    def instance_method(self):
        return (f"This is an instance method of {self}")
    
    @classmethod
    def class_method(cls):
        return (f"This is a class method of {cls}")
    
    @staticmethod
    def static_method():
        return "This is a static method"
    
# test = ClassTest() # Create an instance of ClassTest
# print(test.instance_method()) # This will print the instance method
# print(ClassTest.instance_method(test))     # This will also print the instance method, showing that it can be called with an instance or the class itself

# ClassTest.class_method()  # This will print the class method

# print(ClassTest.class_method())  # This will also print the class method

# print(ClassTest.static_method())  # This will print the static method
# print(ClassTest.instance_method())  # This will raise an error because instance_method is not


class BOOK:
    TYPES = ("hardcover", "paperback", "ebook")

    def __init__(self,name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"BOOK({self.name!r}, {self.book_type!r}, {self.weight!r})"
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return BOOK(name , BOOK.TYPES[2], page_weight + 100)
    @classmethod
    def paperback(cls, name, page_weight):
        return BOOK(name , BOOK.TYPES[1], page_weight + 100)
    @classmethod
    def ebook(cls, name, page_weight):
        return BOOK(name , BOOK.TYPES[0], page_weight + 100)


book = BOOK.hardcover("Python Programming", 500)  # Create a hardcover book instance
light_book = BOOK.paperback("Learning Python", 300)  # Create a paperback book instance
ebook = BOOK.ebook("Python Cookbook", 200)  # Create an ebook instance
print(book)  # This will print the book object using the __repr__ method      
print(light_book)  # This will print the light book object using the __repr__ method
print(ebook)  # This will print the ebook object using the __repr__ method  