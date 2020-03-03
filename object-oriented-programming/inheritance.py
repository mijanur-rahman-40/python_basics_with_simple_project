class Animal:
    def __init__(self):
        print('Animal created')

    def whoAmI(self):
        print('I am a animal')

    def eat(self):
        print('I am eating')


class Dog(Animal):
    def __init__(self):
        # creating instance of animal class
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print('I am a dog')


animal = Animal()
animal.eat()

#  dog class
myDog = Dog()

myDog.whoAmI()

