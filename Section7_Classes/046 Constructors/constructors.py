class Person:
    def __init__(self, name):
        self._name = name

    def eating(self):
        print(f"{self._name} is Eating!")

p = Person("Abir")
p.eating()
print(p)