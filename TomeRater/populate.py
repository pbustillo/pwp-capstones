from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678, 10)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345, 20)
print()
novel1.set_isbn(9781536831139)
print()
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452, 15)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938, 30)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010, 7)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000, 25)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


# for testing the methods. I chose to use print() as part of these methods' output rather than return.
Tome_Rater.print_catalog()
print()
Tome_Rater.print_users()
print()
print("Most positive user:")
print()
Tome_Rater.most_positive_user()
print()
print("Highest rated book:")
print()
Tome_Rater.highest_rated_book()
print()
print("Most read book:")
print()
Tome_Rater.most_read_book()
print()

#for testing more additional methods
Tome_Rater.get_n_most_read_books(5)
print()
Tome_Rater.get_n_most_prolific_readers(10)
print()
Tome_Rater.get_n_most_expensive_books(4)
print()
print(str(Tome_Rater.get_worth_of_user("alan@turing.com"))+" "+"USD$")






