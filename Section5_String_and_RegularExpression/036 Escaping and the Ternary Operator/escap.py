import re

text = "az"
result = re.match(r"az",text)
print("No Match" if result is None else result.group())

print()

text1 = r"a\nz"
result1 = re.match(r"a\nz",text1)
print("No match" if result1 is None else result1.group())

result2 = re.match(r"a\\nz", text1)
print("No match" if result2 is None else result2.group())