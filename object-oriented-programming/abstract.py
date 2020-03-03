class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError(
            "Subclass must implemented this abstract method")


class Dog(Animal):
    def speak(self):
        return self.name + " says woof!"


class Cat(Animal):
    def speak(self):
        return self.name + " says meow!"


myAnimal = Animal('freed')
# myAnimal.speak()

dog = Dog('fido')
cat = Cat('isis')

print(dog.speak())
print(cat.speak())

