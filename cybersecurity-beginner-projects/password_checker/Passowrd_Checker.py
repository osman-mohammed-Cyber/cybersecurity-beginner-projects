# ======================================
# Educational Password Strength Checker
# ======================================

import string

# Common weak passwords list (educational example)
COMMON_PASSWORDS = [
    "password", "123456", "12345678",
    "qwerty", "abc123", "password123"
]

# Ask the user to enter a password
password = input("Enter a password to evaluate: ")

score = 0
feedback = []

# Rule 1: Check password length
if len(password) >= 8:
    score += 1
else:
    feedback.append("Password is too short (minimum 8 characters).")

# Rule 2: Check for uppercase letters
if any(char.isupper() for char in password):
    score += 1
else:
    feedback.append("Add at least one uppercase letter.")

# Rule 3: Check for lowercase letters
if any(char.islower() for char in password):
    score += 1
else:
    feedback.append("Add at least one lowercase letter.")

# Rule 4: Check for digits
if any(char.isdigit() for char in password):
    score += 1
else:
    feedback.append("Add at least one number.")

# Rule 5: Check for special characters
if any(char in string.punctuation for char in password):
    score += 1
else:
    feedback.append("Add at least one special character.")

# Rule 6: Check against common passwords
if password.lower() in COMMON_PASSWORDS:
    feedback.append("Password is too common and easily guessable.")
    score = 0

# Final evaluation
print("\nPassword Strength Evaluation:")

if score <= 2:
    print("Strength: Weak")
elif score <= 4:
    print("Strength: Moderate")
else:
    print("Strength: Strong")

# Show feedback
if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)
else:
    print("\nGood job! Your password meets basic security requirements.")

print("\nNote: This tool is for educational purposes only.")
