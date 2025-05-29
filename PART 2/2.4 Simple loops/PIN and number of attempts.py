# This program asks the user for a PIN code until they guess it correctly.
# It then prints the number of attempts.

correct_pin = "4321"
attempts = 0

while True:
    # Ask the user for the PIN
    user_pin = input("PIN: ")
    attempts += 1  # Increment the attempt counter

    # Check if the entered PIN is correct
    if user_pin == correct_pin:
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempts} attempts")
        break  # Exit the loop if the PIN is correct
    else:
        print("Wrong") # Print "Wrong" if the PIN is incorrect