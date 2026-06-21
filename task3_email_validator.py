# Task 3: Email Validator

email = input("Enter your email: ")

if "@" in email and "." in email.split("@")[-1]:
    print("Valid Email Address")
else:
    print("Invalid Email Address")