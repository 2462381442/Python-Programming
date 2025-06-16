# Write your solution here
limit = int(input("How many items: "))
list = []
x = 1

while x <= limit:
    item = int(input(f"Item {x}: "))
    list.append(item)
    x += 1

print(list)