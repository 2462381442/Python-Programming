value = int(input("Value of gift: "))

if value <= 5000:
    print("No tax!")

if 5000 < value <= 25000:
    print(f"Amount of tax: {100 + (value - 5000) * 0.08 } euros")

if 25000 < value <= 55000:
    print(f"Amount of tax: {1700 + (value - 25000) * 0.1 } euros")

if 55000 < value <= 200000:
    print(f"Amount of tax: {4700 + (value - 55000) * 0.12 } euros")

if 200000 < value <= 1000000:
    print(f"Amount of tax: {22100 + (value - 200000) * 0.15 } euros")

if 1000000 < value:
    print(f"Amount of tax: {142100 + (value - 1000000) * 0.17 } euros")