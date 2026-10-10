import re

menu = """
1. Fish
2. Bread
3. Peppers
4. Potatoes
"""

result = re.findall(r"^(.*)$", menu)
print(result)

result1 = re.findall(r"^(.*)$", menu, re.DOTALL)
print(result1)

result2 = re.findall(r"^(.*)$", menu, re.DOTALL|re.MULTILINE)
print(result2)

result3 = re.findall(r"^(.*)$" , menu, re.MULTILINE)
print(result3)