class Person:
    def __init__(self, name):
        self._name = name

    def eating(self):
        print(f"{self._name} is eating")

    def __str__(self):
        return f"Hello i am {self._name}"

    def __repr__(self):
        return f'Person("{self._name}")'

p = Person("Abir")
p.eating()
print(p)

print()

text = str(p)
print(text)

print()

print(repr(p))
print(eval(repr(p)))