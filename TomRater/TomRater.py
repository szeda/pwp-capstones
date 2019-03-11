class User(object):
    def __init__(self, name, email):
        self.name=str(name)
        assert("@" in email)
        assert(".com" or ".edu" or ".org" in email)
        self.email=str(email)
        self.books={}
    def read_book(self,book,rating=None):
        self.books[book]=rating
    def get_average_rating(self):
        r=0
        b=0
        for book in self.books.values():
           r+=books
        for book in self.books.keys():
           b+=1
        return r/b
    def get_email(self):
        if self.name:
            return self.email
        else:
            print("No such user")
            
    def change_email(self, address):
            if self.email:
                assert("@" in email)
                assert(".com" or ".edu" or ".org" in email)
                self.email=address
                print( "User has had his/her email updated")
                
    def __repr__(self):
        print( " User {name}, email:{email}, books read: {num}".format(name=self.name,email=self.email,num=len(self.books))
                       

    def __eq__(self, other_user):
         return self.name == other_user.name and self.email == other_user.email


class Books():           
    def __init__(self,title,isbn):
          self.title=str(title)
          self.isbn=int(isbn)
          self.ratings=[]
    def get_title(self):
               if self.title:
                   return self.title

    def __hash__(self):
          return hash((self.title, self.isbn))

    def get_average_rating(self):
      ar=0
      for i in self.ratings:
         if len(self.ratings)!=0:
            ar+=i
      return ar/len(self.ratings)
               
    def get_isbn(self):
      if self.isbn:
        return self.isbn

    def set_isbn(self,new_number):
      if self.isbn:
        self.isbn=new_number
        print("{book}'s isbn has been updated".format(book=self.title))

    def add_rating(self,rating):
      if rating>0 and rating <4:
        self.ratings.append(rating) 
      else:
        print("Invalid Rating")
      
    def __eq__(self, other_book):
          return self.title==other_book.title
          return self.isbn==other_book.isbn
               
class Fiction(Books):
     def __init__(self,title,isbn,author=None):
      super().__init__(title,isbn)
      if author:
         self.autor=author
          
      def get_author(self):
        if self.autor:
           return self.autor

      def __repr__(self):
           return "{title} by {author}".format(title=self.title,author=self.author)


class Non_Fiction(Books):
      def __init__(self,title,isbn,subject=None,level=None):
       super().__init__(title,isbn)
       if subject:
          self.subject=str(subject).title()
          if level:
            self.level=str(level).lower
                         
      def get_subject(self):
        return self.subject

      def get_level(self):
        return self.level

      def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)


class TomRater(object):
     def __init__(self):
         self.users={}
         self.books={}
               
     def create_book(self,title,isbn):
        return Books(title,isbn)
     def create_novel(self,title,author,isbn):
        return Fiction(title,author,isbn)
     def create_non_fiction(self,title,subject,level):
        return Non_Fiction(title,subject,level)


     def add_book_to_user(self,book,email,rating=None):
           if email in self.users:
              self.users[email].read_book(book, rating)
              if rating != "":
                 book.add_rating(rating)
                 if book in self.books:
                   self.books[book] += 1
                 else:
                   self.books[book] = 1               
           else:
               return "No user with email {email}!".format(email=email)

      def add_user(self, name, email, user_books=None):
            if email in self.users:
                print("This user already in the list")
            else:
                user = User(name, email)
                self.users[email] = user
               if user_books != None:
                   for book in user_books:
                      self.add_book_to_user(book, email)

      def print_catalog(self):
            for book in self.books.keys():
                  print(book)

      def print_users(self):
           for user in self.users.values():
                print(user)


      def get_most_read_book(self):
         return max(self.books, key=lambda key: self.books[key])


      def highest_rated_book(self):
         hr = None
         hrat = 0
         for book in self.books.keys():
             rating = book.get_average_rating()
             if rating > hrat:
                 hr = book                
                 hrat = rating
         return hr

      def most_positive_user(self):
          pu = None
          hrat = 0
          for user in self.users.values():
              avg_user_rating = user.get_average_rating()
              if avg_user_rating > hrat:
                  pu = user
                  hrat = avg_user_rating
          return pu



      def get_n_most_read_books(self,n):
          descending=sorted(self.books.items(),key=lambda kv:kv[1],reverse=True)
          return descending[0:n]


      def get_n_most_expensive_books(self, n):
          most_expensive_books = []
          for book in self.books.keys():
              most_expensive_books.append((book.price, book))
          most_expensive_books.sort(reverse=True)

          if n > len(most_expensive_books):
              n = len(most_expensive_books)

          return most_expensive_books[0:n]    
    


               

  


 
