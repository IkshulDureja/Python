# Inheritance
class animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")

class Dog(animal):

    def __init__(self):
    #     animal.__init__(self)
        print("DOG CREATED")

    def eat(self):
        print("DOG EATING")
mya = Dog()
mya.whoAmI()
mya.eat()
# Special Methods

class book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("Book is destroyed!")
b = book("python","jose",200)
print(b)
print(len(b))
del b
