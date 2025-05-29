# This program asks the user for a password and verifies it.

# Ask the user to set their password
password = input("Password: ")

# Loop until the repeated password matches the original password
while True:
    # Ask the user to repeat the password
    repeat_password = input("Repeat password: ")

    # Check if the passwords match
    if repeat_password == password:
        # If they match, print a success message and break the loop
        print("User account created!")
        break
    else:
        # If they don't match, print an error message and continue the loop
        print("They do not match!")