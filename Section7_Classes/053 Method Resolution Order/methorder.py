class A:
    def run(self):
        print("Hello A")

class B:
    def run(self):
        print("Hello B")

class C(A,B):
    pass

class D(B,A):
    pass

c = C()
c.run()
print(C.mro())

print()

d = D()
d.run()
print(D.mro())