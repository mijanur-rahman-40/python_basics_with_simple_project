class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"


dog = Dog('niko')
cat = Cat('felix')

print(dog.speak())

for pet in [dog, cat]:
    print(type(pet))
    print(type(pet.speak()))


def petSpeak(animalObj):
    print(animalObj.speak())


petSpeak(dog)
petSpeak(cat)


