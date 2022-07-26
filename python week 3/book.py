class Book:
    """This class represents a Book and it's information
    """
    def __init__(self):
        """Initializes book

        Args:
            self
        """

    def set_book(self):
        ISBN = input("Enter the ISBN number: ")
        title = input("Enter the title: ")
        auths = input("Enter the authors (separated by comma): ")
        pub = input("Enter the publisher: ")
        pub_date = input("Enter the publication date: ")
        price = float(input("Enter the price: "))

        self.ISBN = ISBN
        self.title = title
        self.auths = auths.split(", ")
        self.pub = pub
        self.pub_date = pub_date
        self.price = price

    def __str__(self):
        #return f'{self.title}: ISBN number- {self.ISBN}, Author- {self.auths}, Publisher- {self.pub}, Publication Date- {self.pub_date}, Price- {self.price}.'
        #another way:
        s = ""
        s += f'Title: {self.title} \n'
        s += f'ISBN Number: {self.ISBN} \n'
        s += f'Authors: '
        for author in self.auths:
            s+= author + ", "
        s = s[:-2]          #removes extra last comma from authors 
        s += "\n"
        s += f'Publisher: {self.pub} \n'
        s += f'Publication Date: {self.pub_date} \n'
        s += f'Price: {self.price}'

        return s
