# and, not, or
# True, False

raining = False
temprature = 18

if temprature > 19 and not raining:
    print("Weather fine")
elif not raining:
    print("At least it's dry")
else:
    print("Stay indoors")

#Ternary operator
mood = "good" if not raining else "bad"
print(mood)