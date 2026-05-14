# List operations demo
numbers = [10, 20, 30, 40]

print("Original List:", numbers)

# Access
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Update
numbers[2] = 35
print("Updated list:", numbers)

# append()
numbers.append(50)
print("After append:", numbers)

# insert()
numbers.insert(2, 25)   # insert 25 at index 2
print("After insert:", numbers)

# remove()
numbers.remove(40)      # removes first occurrence of 40
print("After remove:", numbers)

# pop()
popped = numbers.pop()  # removes last element
print("After pop:", numbers, "| Popped:", popped)

# sort()
numbers.sort()
print("Sorted:", numbers)

# reverse()
numbers.reverse()
print("Reversed:", numbers)

# count()
print("Count of 20:", numbers.count(20))

# index()
print("Index of 25:", numbers.index(25))


marks = []
n = int(input("Enter number of students: "))
for i in range(n):
    score = int(input(f"Enter marks of student {i+1}: "))
    marks.append(score)

print("Marks List:", marks)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Average Marks:", sum(marks)/len(marks))
