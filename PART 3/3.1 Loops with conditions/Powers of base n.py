limit = int(input("Upper limit: "))
power = 0
base = int(input("Base: "))

while limit > 0 and base**power <= limit:
    print(base**power)
    power += 1