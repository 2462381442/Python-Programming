print("Please type in integer numbers. Type in 0 to finish.")
number = int(input("Number:"))
count = 1

while number != 0:
    number1 = int(input("Number:"))
    count += 1
    if number1 != 0:
        number += number1
    else:
        break

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {number}")
print(f"The mean of the numbers is {number/count}")
