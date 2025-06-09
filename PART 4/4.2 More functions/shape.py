# Copy here code of line function from previous exercise and use it in your solution
def line(length, character):
    if character:
        print(character[0] * length)
    else:
        print("*" * length)

def shape(size1, character1, size2, character2):
    x = 1
    y = 1
    while x <= size1:
        line(y, character1)
        x += 1
        y += 1
    z = 1
    while z <= size2:
        line(size1, character2)
        z += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")