# Dictionary operations demo
student = {"name": "Rahul", "age": 20, "marks": 85}

print("Original Dictionary:", student)

# keys()
print("Keys:", student.keys())

# values()
print("Values:", student.values())

# items()
print("Items:", student.items())

# get()
print("Get marks:", student.get("marks")) 

# update()
student.update({"marks": 90, "course": "Python"})
print("After update:", student)

# pop()
student.pop("age")
print("After pop (removed age):", student)
S

#Contact Book 
contacts = {}
n = int(input("Enter number of contacts: "))
for i in range(n):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone

print("Contact Book:", contacts)
search = input("Search contact: ")
print("Phone:", contacts.get(search, "Not Found"))

#Frequency Counter
text = input("Enter a string: ")
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print("Character Frequency:", freq)
