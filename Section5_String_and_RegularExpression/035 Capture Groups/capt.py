import re

text = "ID: 123 Some Corp. Serial: 345453"

result = re.match(r".*?\d\d\d", text)
if result is None:
    print("No match")
else:
    print(result.group())

print()

result1 = re.match(r".*?\d{3}", text)
if result1 is None:
    print("No match")
else:
    print(result1.group())

print()

result2 = re.match(r".*?(\d{3})", text)
if result2 is None:
    print("No match")
else:
    print(result2.group(1))

print("**************************")

result3 = re.match(r".*?(\d{3}).*?(\d+)", text)
if result3 is None:
    print("No match")
else:
    print(result3.group(1))
    print(result3.group(2))

print()

result4 = re.match(r".*?(\d{3}).*?(\d*)$",text)
if result4 is None:
    print("No match")
else:
    print(result4.group(1))
    print(result4.group(2))