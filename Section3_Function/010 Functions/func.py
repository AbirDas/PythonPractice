def calculate_area(width, height, length):
    return width * height * length

def calculate_area_withDefault(width, height, length=2):
    return width * height * length

area = calculate_area(2, 3, 6)
area_def = calculate_area_withDefault(2,3)

print(area)
print(area_def)