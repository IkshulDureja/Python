print(type(10))
print(type([]))
print(type(()))
print(type({}))

class Sample():
    pass

# Class names are capitalised to differentiate from functions

x = Sample()

print(type(x))

# Attributes and Methods of class
# Special Methods look like functions inside the class

class Dog():

    #CLASS OBJECT Attributes
    species = "mammal"

    # Attributes
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

mydog = Dog("Lab","Sammy")
print(mydog.breed)
print(mydog.name)
print(mydog.species)



# METHODS
class Circle():

    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

#self keyword tells that it is not just a  free floating function inside the class, it is the method of that class
    def area(self):
        return self.radius* self.radius * Circle.pi

    def set_radius(self,new_r):
        self.radius = new_r

myc = Circle(3)
# To redefine the Radius
# myc.radius = 100
# OR
myc.set_radius(999)
print(myc.area())
