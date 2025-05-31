string = input("Please type in a string: ")
ct1 = string[1]
ct2 = string[-2]

if ct1 == ct2:
    print(f"The second and the second to last characters are {ct1}")
else:
    print("The second and the second to last characters are different")

