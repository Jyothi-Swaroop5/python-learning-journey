marks = []
n = int(input("Enter number of students: "))
for i in range(n):
    score = int(input(f"Enter marks of student {i+1}: "))
    marks.append(score)

print("Marks List:", marks)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Average Marks:", sum(marks)/len(marks))
