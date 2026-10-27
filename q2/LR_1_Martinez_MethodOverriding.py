
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "eats food.")

    def make_sound(self):
        print(self.name, "makes a sound.")
        

class Lion(Animal):
    def eat(self):
        print(self.name, "eats fresh meat.")

    def make_sound(self):
        print(self.name, "roars loudly.")


class Elephant(Animal):
    def eat(self):
        print(self.name, "eats grass and fruits.")

    def make_sound(self):
        print(self.name, "trumpets.")


class Monkey(Animal):
    def eat(self):
        print(self.name, "eats bananas.")

    def make_sound(self):
        print(self.name, "chatters.")

animal1 = Lion("Simba")
animal2 = Elephant("Dumbo")
animal3 = Monkey("George")

animals = [animal1, animal2, animal3]

for animal in animals:
    animal.make_sound()
    animal.eat()
    print()
