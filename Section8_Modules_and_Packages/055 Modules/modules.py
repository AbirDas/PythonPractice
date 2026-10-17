import mymodules as mod

mod.myfunc()
#mymodules.MyClass.mymethod() #this will work if self is missing from mymethod() of MyClass

print()

c = mod.MyClass()
c.mymethod()