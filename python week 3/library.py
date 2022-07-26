from book import Book

class Library:
    """This class represents a library. 
    """
    def __init__(self):
        """Initialize library's attributes

        Args:
            self
        """
        self.books = {}     #key = ISBN, value = Book object 
                            #ISBN is unique so is used as key

    def add_book(self, book: Book):
        self.books[book.ISBN] = book

    def remove_book(self, ISBN):
        if ISBN in self.books:
            del self.books[ISBN]
            return True
        else:
            return False

    def display_books(self):
        for book in self.books.values():
            print(book)
            print("-" * 30)     #separate each book when printing
    
    def search_by_ISBN(self, ISBN):
        if ISBN in self.books:
            return self.books[ISBN]
        else:
            return None

    def search_by_auth(self, author):
        #author may have written more than one book   

        # result = []
        # for book in self.books.values():
        #     if auths in book.auths:
        #         result.append(book) 

        #another way using list comp
        return [book for book in self.books.values() if author in book.auths]

    def search_by_price(self, price):
        return [book for book in self.books.values() if book.price < price]
