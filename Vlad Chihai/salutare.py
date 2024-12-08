class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hi(self):
        print("Hi, my name is", self.name)
        self.sage()
    def sage(self):
        print("Im", self.age, "years old")

p1 = Person("Ion", 16)
p1.say_hi()

