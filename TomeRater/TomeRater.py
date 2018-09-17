class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Email address successfully changed.")

    def __repr__(self):
        print("User " + self.name + ", email: " + self.email + ", books read: ") 

    def __eq__(self, other_user):
        if self.email == other_user.email and self.name == other_user.name:
          return True

    def read_book(self, book, rating=None):
      self.books[book] = rating  

    def get_average_rating(self):
      sum = 0
      count = 0
      for book in self.ratings:
        sum += self.ratings[book]
        count += 1
      return sum / count

class Book:
    def __init__(self, title, isbn):
      self.title = title
      self.isbn = isbn
      self.ratings = []

    def __hash__(self):
      return hash((self.title, self.isbn))

    def get_title(self):
      return self.title

    def get_isbn(self):
      return self.isbn

    def set_isbn(self, newisbn):
      self.isbn = newisbn
      print("ISBN changed to " + str(self.isbn))

    def add_rating(self, rating):
      if rating >= 0 or rating < 5:
        self.ratings.append(rating)
      else:
        print("Invalid Rating")

    def __eq__(self, another_book):
      if self.title == another_book.title and self.isbn == another_book.isbn:
        return True

    def get_average_rating(self):
      sum = 0
      count = 0
      for book in self.ratings:
        sum += self.ratings[book]
        count += 1
      return sum / count

class Fiction(Book):
    def __init__(self, title, author, isbn):
      super().__init__(title, isbn)
      self.author = author

    def get_author(self):
      return self.author

    def __repr__(self):
      return self.title + " by " + self.author

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
      super().__init__(title, isbn)
      self.subject = subject
      self.level = level

    def get_subject(self):
      return self.subject

    def get_level(self):
      return self.level

    def __repr__(self):
      return self.title + ", a " + self.level + " manual on " + self.subject

class TomeRater:
    def __init__(self):
      self.users = {}
      self.books = {}

    def create_book(self, title, isbn):
      self.books.update(Book(title, isbn))
      return Book(title, isbn)

    def create_novel(self, title, author, isbn):
      self.books.update(Fiction(title, author, isbn))
      return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
      self.books.update(Non_Fiction(title, subject, level, isbn))
      return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
      #print("Book is " + str(book))
      #print("Email is " + email)
      #print("User is " + self.users.get(email, "None"))
      if self.users.get(email, "None")  == "None":
        print("No user with email " + email)
      else:
        print("Good user with email " + email)
        self.read_book(book, rating)
        self.add_rating(book, rating)
        if self.books.get(book, "None") == "None":
          self.books[book] = 1
        else:
          self.books[book] += 1

    def add_user(self, name, email, user_books=None):
      print(name, email, user_books)
      self.users.update(User(name, email))
      if user_books != "None":
        for book in user_books:
          self.add_book_to_user(book, email)
  
    def print_catalog(self):
      for book in self.books:
        print(book)

    def print_users(self):
      for user in self.users:
        print(self.users[user])

    def most_read_book(self):
      most_read = 0
      most_read_book = ""
      for book in self.books:
        if self.books[book] > most_read:
          most_read = self.books[book]
          most_read_book = book
      return(book)

    def highest_rated_book(self):
      highest_average = 0
      highest_average_book = ""
      for book in self.books:
        if book.get_average_rating() > highest_average:
          highest_average = book.get_average_rating()
          highest_average_book = book
      return(highest_average_book)

    def most_positive_user(self):
      highest_average = 0
      highest_average_user = ""
      for user in self.users:
        if user.get_average_rating() > highest_average:
          highest_average = user.get_average_rating()
          highest_average_user = user
      return(highest_average_user)
