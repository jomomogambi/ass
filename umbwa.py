class Animal:
    def legs(self):
        print("I have four legs")
    def fur(self):
        print("My body is covered with fur")
class Dog(Animal):
    def bark(self):
        print("The dog barks")
class Umbwa(Dog):
    def eat(self):
        print("I like eating meat mostly")
u=Umbwa()
u.eat()
u.bark()
u.legs()
u.fur()