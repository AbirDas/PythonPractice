distance = 1.2345
height = 2.34

print(f"Height: {height}, Distance: {distance}")
print(f"Height: {height:.1f}, Distance: {distance:.3f}")

print()

print("Height: {}, Distance: {}".format(height,distance))
print("Height: {1}, Distance: {0}".format(distance,height))
print("Height: {1:.1f}, Distance: {0:.3f}".format(distance,height))

print()

print("Height: %i, Distance: %f" % (height,distance))
print("Height: %.1f, Distance: %.3f" %(height,distance))

print()

print("one\ntwo")
print(r"one\ntwo")