days = {
    "Mon":"Monday",
    "Tue":"Tuesday",
    "Wed":"Wednesday",
    "Thur":"Thursday",
    "Fri":"Friday",
    "Sat":"Saturday",
    "Sun":"Sunday",
}

print(days)

del days["Mon"]
print(days)

print()

print(days.pop("Thur"))
print(days)

print()

print(days.popitem())
print(days)

print(days.clear())
# or use
# days = {}
print(days)