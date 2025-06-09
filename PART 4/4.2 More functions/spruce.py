# Write your solution here
def spruce(height):
    print("a spruce!")
    x = 1
    y = 1
    while x <= height:
        print(" " * (height - x) + "*" * (2 * x - 1))
        x += 1
    print(" " * (height - 1) + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)