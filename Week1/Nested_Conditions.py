"""
2. Nested Conditions
Take a number as input:
- If positive → check whether it is even or odd
- If negative → print "Negative number"
- If zero → print "Zero"
"""

num = int(input("\nEnter a number: "))

if num > 0:
    if num % 2 == 0:
        print(f"{num} is a positive even number.")
    else:
        print(f"{num} is a positive odd number.")

elif num < 0:
    print(f"{num} is a negative number.")

else:
    print("The number is zero.")
