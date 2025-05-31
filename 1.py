class Dog:
    def sound(self):
        print("Dog says Woof!")

class Cat:
    def sound(self):
        print("Cat says Meow!")

class Parrot:
    def sound(self):
        print("Parrot says Hello!")

class Cow:
    def sound(self):
        print("Cow says Moo!")
# Polymorphism example
def animal_sound(animal):
    animal.sound()

# Creating objects
d = Dog()
c = Cat()
p = Parrot()
w = Cow()


# Using the same function for different objects
animal_sound(d)
animal_sound(c)
animal_sound(p)
animal_sound(w)

    