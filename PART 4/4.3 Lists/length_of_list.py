# Write your solution here
def length(my_list):
    if not my_list:
        return 0
    return 1 + length(my_list[1:])

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = length(my_list)
    print(result)