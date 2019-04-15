from collections import OrderedDict # Built-in class by Python to sort a dictionary

# This class creates a user profile.
class User(object):

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.books = {} # This dictionary includes all the books read by user and each book's rating
        

    def get_email(self):
        return self.email

    def change_email(self, address: str):
        self.address = address
        if self.address != self.email:
            self.email = self.address
            print ("User' email:"+ " "+ str(self.email) + " " + "has been updated")
        return self.email

    # It creates dict: self.books; which key: ths object book and value: the rating
    def read_book(self, book: str, rating: int=0):
        self.books[book]=rating
        return self.books

    # It calculates the average rating given by the user for his/her books.
    def get_average_rating(self):
        counting = 0
        average_rating = 0
        for book_rating in self.books:
            counting += self.books.get(book_rating)
        average_rating = counting / len(self.books)
        return average_rating    
        
    def __repr__(self):
        return "User:"+" "+ self.name+","+" "+"email:"+" "+self.email+","+" "+"books read:"+" "+str(len(self.books))

    # I am not using this method.
    def __eq__(self, other_user):
        pass

    # A built-in method by Python to make sure class objects are hashable.
    def __hash__(self):
        return hash((self.name, self.email))


#This class creates a book profile#
class Book:

    def __init__(self, title: str, isbn: int, price: int):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn: int):
        self.new_isbn = new_isbn
        if self.isbn != self.new_isbn:
            self.isbn = self.new_isbn
            print ("This book's ISBN:"+ " "+ str(self.isbn) + " " + "has been updated")
        return self.isbn

    # It creates a list of all the rating provided by all the users for book xx
    def add_rating(self, rating: int):
        self.rating = rating
        if self.rating >= 0 and self.rating <= 4:
            self.ratings.append(self.rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        counting = 0
        average_rating = 0
        for book_rating in range(0,len(self.ratings)):
            counting += self.ratings[book_rating]
        average_rating = counting / len(self.ratings)
        return average_rating       

    def __repr__(self):
        return "Book title:"+" "+ self.title+","+" "+"ISBN #:"+" "+str(self.isbn)+"."+" "+"Ratings:"+" "+str(self.ratings)

    # I am not using this method.
    def __eq__(self):
        pass
    
    # A built-in method by Python to make sure class objects are hashable.
    def __hash__(self):
        return hash((self.title,self.isbn))


#This class is a subclass of the main class Book#   
class Fiction(Book):

    def __init__(self, title: str, author: str, isbn: int, price: int):
        super().__init__(title, isbn, price)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "Book Title:"+" "+ self.title+" "+"by"+" "+self.author+" "+"ISBN #:"+" "+str(self.isbn)+"."+" "+"Ratings:"+" "+str(self.ratings)    


#This class is a subclass of the main class Book#    
class Non_Fiction(Book):

    def __init__(self, title: str, subject: str, level: str, isbn: int, price: int):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "Book Title:"+" "+ self.title+" "+"a"+" "+self.level+" "+"manual on"+" "+self.subject+" "+"ISBN #:"+" "+str(self.isbn)+"."+" "+"Ratings:"+" "+str(self.ratings)    

#Here we create the TomRater Class#
class TomeRater:

    def __init__(self):
        self.users ={}
        self.books ={}

    # It calls the class Book whenever a new object has been instantiated (a new book is created)
    def create_book(self,title: str, isbn: int, price: int):
        return Book(title, isbn, price)

    # It calls the sub-class Fiction whenever a new object has been instantiated (a new book novel is created)
    def create_novel(self, title: str, author: str, isbn: int, price: int):
        return Fiction(title, author, isbn, price)

    # It calls the sub-class Non_Fiction whenever a new object has been instantiated (a new non_fiction book is created)
    def create_non_fiction(self,title: str, subject: str , level: int, isbn: int, price: int):
        return Non_Fiction(title, subject, level, isbn, price)

    def add_book_to_user(self, book: str, email: str, rating: int = 0):
        if email not in self.users:
            print("No user with email"+" "+ str(email))
        else:
            self.users[email].read_book(book,rating) #self.users[email] = name.// read_book(book,rating) a method under class User
            book.add_rating(rating) # book an object instantiated with the class Book (or its sub-classes) // add_rating(rating) a method of the class Book
            if book not in self.books: # It counts how many times the book has been read.
                self.books[book]=1
            else:
                self.books[book]+=1
              
    # A user is added to the dict: self.users. keys = email and the values = name. Name is an object instantiated with the class User.     
    def add_user(self, name: str, email: str, user_books: list = []):
        name = User(name,email)
        self.users[email]=name
        if len(user_books) != 0: # if the user is added with a list of books, the books are added to the user profile.
            for booklist in user_books:
                self.add_book_to_user(booklist,email)


    # It prints the key (book) of the dict: self.books. Remember each key (book) is an instantation object of the class Book or its sub-classes.
    def print_catalog(self):
        print("---The Catalog of Books is:---")
        for x in self.books:
            print(x)

    # It prints the value (name) of each key (email) within the dict self.users. Remember name is an instantiation object of class User
    def print_users(self):
        print("---The users are:---")
        for x in self.users:
            print(self.users[x])


    def most_read_book(self):
        count = 0
        most_read=[]
        for book in self.books:
            if self.books[book]>count:
                count=self.books[book]
                most_read.insert(0,book)
        print ("The most read book is:"+" "+ str(most_read[0]))

    # We call get_average_rating method under book class to get the book with the highest rating
    def highest_rated_book(self):
        count=0
        highest_rated=[]
        for book in self.books:
            if book.get_average_rating() > count:
                count = book.get_average_rating()
                highest_rated.insert(0,book)
        print("The highest rated book is:"+" "+ str(highest_rated[0]))

    # We call get_average_rating method under User class to get the user with the highest rating given
    def most_positive_user(self):
        count=0
        highest_user_rating=[]
        for user in self.users:
            if self.users[user].get_average_rating() > count:
                count = self.users[user].get_average_rating()
                highest_user_rating.insert(0,self.users[user])
        print("The user with the highest rating is:"+" "+ str(highest_user_rating[0]))

    # The following method will sort the dict: self.books,based on value / not keys, in descending order,
    # It uses the built-in class: OrderedDict and the funct: lambda
    def get_n_most_read_books(self, n: int):
        count = 1
        dd = OrderedDict(sorted(self.books.items(), key=lambda x: x[1], reverse=True))
        print("The"+" "+ str(n)+" "+"books that have been read most are:")
        print()
        for book in dd:
            print("Book:"+" "+str(book.title)+" "+"has been read by"+" "+str(dd[book])+" "+"readers")
            count +=1
            if count > n:
                break

    # It uses the built-in class: OrderedDict and the funct: lambda
    def get_n_most_prolific_readers(self, n: int = 0):
        # Lets create a dict with Key: user'email and value: # of books read by user
        dict1={}
        for x in self.users:
            dict1[x] = len(self.users[x].books)
        # Lets sort in descending order, by value, the dict: dict1 and print the n number of users  
        count = 1
        dd = OrderedDict(sorted(dict1.items(), key=lambda x: x[1], reverse=True))
        print("The"+" "+ str(n)+" "+"most prolific readers are:")
        print()
        for user in dd:
            print("User:"+" "+str(self.users[user].name)+" "+"has read: "+" "+str(dd[user])+" "+"books")
            count +=1
            if count > n:
                break

    # It uses the built-in class: OrderedDict and the funct: lambda
    def get_n_most_expensive_books(self, n: int = 0):
        # Lets create a dict with Key: book's title and value: book' price
        dict1={}
        for book in self.books:
            dict1[book.title]=book.price
        print("The list price is:")
        print(dict1)
        print()
        # Lets sort in descending order, by value, the dict: dict1 and print the n number of books  
        count = 1
        dd = OrderedDict(sorted(dict1.items(), key=lambda x: x[1], reverse=True))
        print("The"+" "+ str(n)+" "+"most expensive books are:")
        print()
        for book in dd:
            print("Book:"+" "+str(book)+"."+" "+"The price is: "+" "+str(dd[book])+" "+"USD$")
            count +=1
            if count > n:
                break


    def get_worth_of_user(self, email: str):
        total_cost=0
        for books_read in self.users[email].books:
            total_cost += books_read.price
        print("The total cost of"+" "+str(email)+" "+"is:")    
        return total_cost   
            
            
        
         
         

            
            
            
            
            
            
        
            
            
            
        
        
              
         
            



        
    




























      















                   

                   
