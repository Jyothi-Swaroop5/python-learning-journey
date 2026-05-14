# Set operations demo
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Set1:", set1)
print("Set2:", set2)

# Union
print("Union:", set1 | set2)

# Intersection
print("Intersection:", set1 & set2)

# Difference
print("Difference (set1 - set2):", set1 - set2)

# Symmetric Difference
print("Symmetric Difference:", set1 ^ set2)

# Add & Remove
fruits = {"apple", "banana", "orange","kiwi"}
print("Is apple in fruits?", "apple" in fruits)
fruits.add("grape")
fruits.remove("banana")
fruits.discard("kiwi") 
print("Fruits after add/remove:", fruits)
