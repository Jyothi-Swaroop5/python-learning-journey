"""
4. While Loop
Keep asking the user for a password until they enter "python123"

Bonus:
- Count how many attempts the user made
"""

correct_password = "python123"
attempts = 0

while True:
    password = input("\nEnter your password: ")
    attempts += 1

    if password == correct_password:
        print("Password is correct.")
        print(f"You entered the correct password in {attempts} attempts.")
        break

    else:
        print("Incorrect password. Please try again.")