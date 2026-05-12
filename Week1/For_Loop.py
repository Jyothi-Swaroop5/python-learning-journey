"""
3. For Loop
- Print numbers from 1 to 20
- Print multiplication table of 5
- Bonus: Print sum of numbers from 1 to 100
"""

# Print numbers from 1 to 20
print("\nNumbers from 1 to 20:")

for i in range(1, 21):
    print(i)

# Multiplication table of 5
print("\nMultiplication Table of 5:")

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# Sum of numbers from 1 to 100
total_sum = 0

for i in range(1, 101):
    total_sum += i

print(f"\nSum of numbers from 1 to 100: {total_sum}")