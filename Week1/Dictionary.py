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
