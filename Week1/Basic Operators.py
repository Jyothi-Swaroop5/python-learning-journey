
# 1. Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print()

# 2. Comparison Operators
print("Comparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
print()

# 3. Assignment Operators
print("Assignment Operators:")
x = 5
print("Initial x:", x)
x += 2
print("x after += 2:", x)
x -= 1
print("x after -= 1:", x)
x *= 3
print("x after *= 3:", x)
x /= 2
print("x after /= 2:", x)
x //= 2
print("x after //= 2:", x)
x %= 3
print("x after %= 3:", x)
x **= 2
print("x after **= 2:", x)
print()

# 4. Logical Operators
print("Logical Operators:")
p = True
q = False
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)
print()

# 5. Bitwise Operators
print("Bitwise Operators:")
m = 6   # binary: 110
n = 3   # binary: 011
print("m & n:", m & n)   # AND
print("m | n:", m | n)   # OR
print("m ^ n:", m ^ n)   # XOR
print("~m:", ~m)         # NOT
print("m << 1:", m << 1) # Left shift
print("m >> 1:", m >> 1) # Right shift
print()

# 6. Membership Operators
print("Membership Operators:")
text = "hello world"
print("'h' in text:", 'h' in text)
print("'z' not in text:", 'z' not in text)
print()

# 7. Identity Operators
print("Identity Operators:")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("list1 is list2:", list1 is list2)       # False (different objects)
print("list1 is list3:", list1 is list3)       # True (same object)
print("list1 is not list2:", list1 is not list2)
print()

# 8. Ternary Operator
print("Ternary Operator:")
num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(f"{num} is {result}")

# Nested ternary example
num = -5
status = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(f"{num} is {status}")
