import re

text = "Once upon a time"

result = re.match(r"O", text)

if result is None:
    print("No match")
else:
    print(result.group())

print("Example of match with ignore case")

result1 = re.match(r"o", text, flags=re.IGNORECASE)
if result1 is None:
    print("No match")
else:
    print(result1.group())

print("Match next char with .")

result2 = re.match(r"o.", text, flags=re.IGNORECASE)
if result2 is None:
    print("No match")
else:
    print(result2.group())

print("match any number of character with *")

result3 = re.match(r"o.*", text, flags=re.I)
if result3 is None:
    print("No match")
else:
    print(result3.group())

print("now with ? to reduce the gredness")

result4 = re.match(r"o.*?", text, flags=re.IGNORECASE)
if result4 is None:
    print("No match")
else:
    print(result4.group())

print("now put an srting after ? to force match till the string")

result5 = re.match(r"o.*?time", text, flags=re.I)
if result5 is None:
    print("No match")
else:
    print(result5.group())