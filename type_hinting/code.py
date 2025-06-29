from typing import List

# def list_avg(sequence:List) -> float:
#     return sum(sequence) / len(sequence)

# list_avg(123)  # This will raise a TypeError because 123 is not iterable


# class Book:
#     def __init__(self, name: str, page_count: int):
#         self.name = name
#         self.page_count = page_count


# class BookShelf:
#      def __init__(self,books: List[Book]):
#          self.books = books

#      def __str__(self) -> str:
#          return f"BookShelf with {len(self.books)} books"    


class BOOK:
    TYPES = ("hardcover", "paperback", "ebook")

    def __init__(self,name: str, book_type:str, weight:int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"BOOK({self.name!r}, {self.book_type!r}, {self.weight!r})"
    
    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> 'BOOK':
        return BOOK(name , BOOK.TYPES[2], page_weight + 100)
    @classmethod
    def paperback(cls, name: str, page_weight: int) -> 'BOOK':
        return BOOK(name , BOOK.TYPES[1], page_weight + 100)
    @classmethod
    def ebook(cls, name: str, page_weight: int) -> 'BOOK':
        return BOOK(name , BOOK.TYPES[0], page_weight + 100)
    