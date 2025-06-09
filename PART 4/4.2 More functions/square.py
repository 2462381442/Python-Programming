# Copy here code of line function from previous exercise
def line(length, character):
    if character:
        print(character[0] * length)
    else:
        print("*" * length)

def square(size, character):
    # You should call function line here with proper parameters
    x = 1
    while x <= size:
        line(size, character)
        x += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")