# class1.py

class Person:

    def __init__(self):
        self.name = "default name"
    
    def print(self):
        print(f"Myname is {self.name}")

p1 = Person()
p2 = Person()
p1.name = "전우치"
p1.print()
p2.print()

