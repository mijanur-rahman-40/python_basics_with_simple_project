class Dog():
    # class object attribute
    # same for any instance of class
    species = 'mammal'

    def __init__(self, breed, name, spots):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        # here self work like this
        # her self is a keyword
        self.breed = breed
        self.name = name
        # expect boolean
        self.spots = spots

    def bark(self, age):
        print('Oh Yes My name is {} and age is {}'.format(self.name, age))


myDog = Dog(breed='Lab', name='Sammy', spots=True)
myDog = Dog('Lab', 'Sammy', True)

print(type(myDog))
print(myDog.breed)
print(myDog.species)
myDog.bark(4)


class Circle():
    # class object attribute
    pi = 3.1416

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi
        self.piValue = self.pi

   # method
    def getCircumference(self):
        return self.radius * self.pi * 2


myCircle = Circle()
print(myCircle.getCircumference())
print(myCircle.area)
print(myCircle.pi)
