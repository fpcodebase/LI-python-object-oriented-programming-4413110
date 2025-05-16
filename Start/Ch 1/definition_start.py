# Basic class definitions
# Falguni's exercises


# basic class
# This class does nothing
class example1:
  pass

class example2:
  pass

# Class that inherits from other classes
class example3(example1, example2):
  pass

# Book class which has all the python class features
class Book:
  # Class attributes or variables
  book_types = ['paper', 'e-book']

  # Class constructor or initializer method
  # This is an instance method
  def __init__(self, title):
    self.title = title
    self.type = self.book_types[0]

# TODO: create instances of the class
book1 = Book("Gora")
book2 = Book("Science Grade 1 text book")

# TODO: print the class and property
print('\n', book1, end='\n\n')
print("This book is of type: {}".format(book1.type))
print(book1.title)
print(book2.title)