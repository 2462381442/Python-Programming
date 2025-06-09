# Copy here code of line function from previous exercise
def line(length, character):
    if character:
        print(character[0] * length)
    else:
        print("*" * length)

def triangle(size):
    # You should call function line here with proper parameters
    x = 1
    y = 1
    character = "#"
    while x <= size:
        line(y, character)
        x += 1
        y += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
