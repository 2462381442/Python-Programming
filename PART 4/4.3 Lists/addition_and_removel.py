# Write your solution here
my_list = []
x = 1

while True:
    print(f"The list is now {my_list}")
    move = input("a(d)d, (r)emove or e(x)it: ")
    if move == "d":
        my_list.append(x)
        x += 1
    elif move == "r":
        my_list.pop()
        x -= 1
    elif move == "x":
        break
print("Bye!")