limit = int(input("Upper limit: "))
power = 0

while limit > 0 and 2**power <= limit:
    print(2**power)
    power += 1