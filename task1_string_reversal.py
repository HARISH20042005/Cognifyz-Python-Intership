# Task 1: String Reversal

def reverse_string(text):
    return text[::-1]

user_input = input("Enter a string: ")
reversed_text = reverse_string(user_input)

print("Reversed String:", reversed_text)