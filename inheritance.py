"""Generalization (inheritance): Dog is a kind of Animal."""
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} makes a sound.')

class Dog(Animal):
    def speak(self):
        print(f'{self.name} says woof!')

if __name__ == '__main__':
    animal = Animal('Creature')
    dog = Dog('Buddy')
    animal.speak()
    dog.speak()
