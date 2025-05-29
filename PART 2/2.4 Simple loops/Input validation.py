# sqrt function will not work without this line in the beginning of the program
from math import sqrt

while True:
    number = int(input("Please type in a number: "))
    if number < 0:
        print("Invalid number")
    elif number > 0:
        print(sqrt(number))
    elif number == 0:
        break

print("Exiting...")