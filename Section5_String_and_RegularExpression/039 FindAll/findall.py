import re

menu = """
1. Fish
2. Bread
3. Peppers
4. Potatoes
"""

result = re.findall(r"(\d+)\.", menu)
print(result)

result1 = re.findall(r"(\d+)g\.", menu)
print(result1)

result2 = re.findall(r"(\d+)\.\s+(\w+)" , menu)
print(result2)

result3 = re.findall(r"(\d+)\.\s+(\w+)\n", menu)
print(result3)