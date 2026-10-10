import re

text = "dog cat mouse"

result = re.sub(r"c.*t", "giraffe", text)
print(result)

regex = re.compile(r"C.*T", flags=re.IGNORECASE)
result1 = re.sub(regex, "lion", text)
print(result1)

result2 = re.sub(regex, "tiger", text)
print(result2)