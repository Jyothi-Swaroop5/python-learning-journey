# Tuple operations
coordinates = (10, 20, 30, 40)

# Access
print("First:", coordinates[0])
print("Last:", coordinates[-1])

# Count + Index
print("Count of 20:", coordinates.count(20))
print("Index of 30:", coordinates.index(30))

# Tuple unpacking
x, y, z, w = coordinates
print("Unpacked:", x, y, z, w)

# Conversion
list_version = list(coordinates)
list_version.append(50)
coordinates=(60,70)
print(coordinates)
print("Converted to list:", list_version)
