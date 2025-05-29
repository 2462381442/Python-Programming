# This program prints "hi" and asks to continue until the user inputs "no".

while True:
    # Print the initial message
    print("hi")

    # Ask the user if they want to continue
    user_input = input("Shall we continue? ")

    # Check if the user wants to stop
    if user_input.lower() == "no":
        # Print the exit message
        print("okay then")
        # Break out of the loop
        break