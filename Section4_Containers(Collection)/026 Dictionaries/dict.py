months = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
}

print(months["Jan"])

print()

months["Apr"] = "April"
print(months)

print()

months.update({"May":"May","Jun":"June"})
print(months)

print()

for month in months:
    print(month,months[month])

print()

for month in months.keys():
    print(month, months[month])

print()

for month in months.values():
    print(month)

print()

for month in months.items():
    print(month)

print()

for key, value in months.items():
    print(key,value)

print()

print("Jan" in months)
print("Oct" in months)