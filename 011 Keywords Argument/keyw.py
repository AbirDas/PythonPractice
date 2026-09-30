def calculate_area(width, height, length=1):
    return width * height * length

area = calculate_area(width=2, height=3, length=6)
area1 = calculate_area(2, length=6, height=8)

print(area)
print(area1)