class Dog:
    n_legs = 4
    n_ears = 2
    def __init__(self, my_name):
        self.name = my_name
    def bark(self):
        print("Woof")

Jojo = Dog("JoJo")
print(Jojo.n_legs)
print(Jojo.n_ears)
print(Jojo.name)
Jojo.bark()

