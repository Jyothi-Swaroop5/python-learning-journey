"""
1. If / Else Basics
Ask the user for their age:
- If age < 18 → print "You are a minor."
- If age >= 18 → print "You are an adult."
- Bonus: If age > 60 → print "You are a senior citizen."
"""

# Validate user age input
while True:
    try:
        age = int(input("Enter your age (1-100): "))

        if 1 <= age <= 100:
            break
        else:
            print("Please enter an age between 1 and 120.")

    except ValueError:
        print("Invalid input! Please enter a valid whole number.")

# Check age category
if age > 60:
    print("You are a senior citizen.")
elif age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")