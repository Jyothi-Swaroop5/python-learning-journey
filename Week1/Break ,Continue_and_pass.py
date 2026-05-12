"""
5. Break, Continue, and Pass
- Skip number 5 using continue
- Use pass for number 7
- Stop the loop completely when number is 8 using break

Bonus:
- Print only even numbers between 1 and 20 using continue
"""

print("Numbers from 1 to 10:")

for i in range(1, 11):

    # Skip number 5
    if i == 5:
        continue

    # Placeholder for future code
    if i == 7:
        pass

    # Stop loop when number becomes 8
    if i == 8:
        break

    print(i)

    print("\nEven numbers from 1 to 20:")

# Print only even numbers from 1 to 20
for i in range(1, 21):

    # Skip odd numbers
    if i % 2 != 0:
        continue

    print(i)