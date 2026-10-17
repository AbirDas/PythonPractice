import sys

import stuff.greetings as gr

#print(sys.path)
#To add more dirctory in sys.path use ->  $ENV:PYTHONPATH = 'temp'
print("\n".join(sys.path))

print()

print("Greetings", gr.__file__)

