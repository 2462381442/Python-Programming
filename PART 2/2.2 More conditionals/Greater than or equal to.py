number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in another number: "))

if number1 > number2:
    print(f"The greater number was: {number1}")

if number2 > number1:
    print(f"The greater number was: {number2}")

if number1 == number2:
    print("The numbers are equal!")