class Animal:
    def legs(self):
        print("Ihave four legs")
    def fur(self):
        print("My body is covered with fur")
class Dog(Animal):
    def bark(self):
        print("The dog barks")
d=Dog()
d.barks()
d.legs()
d.fur()