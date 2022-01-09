# int class obj
x = 1
print(type(x))

# function class obj
def test():
    print(type(x))

print(type(test))

name = "test"
#  .method()
# name is a string class obj
print(name.upper())

# user defined class
class Dog:
    def __init__(self, i=0):
        self.i = i

    def bark(self):
        print("Bark!")

    def increment(self):
        self.i = self.i + 1

d = Dog(5)
d.bark()
d.increment()
d.increment()
d.increment()
print(type(d))
print(d.i)


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Bark! " + self.name)

    def age_pls(self):
        print("Age " + str(self.age))

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

bill = Dog("Bill", 9)
james = Dog("James", 3)

bill.bark()
james.bark()

bill.age_pls()
james.age_pls()

bill.set_name("John")
bill.set_age(1)

bill.bark()
bill.age_pls()
