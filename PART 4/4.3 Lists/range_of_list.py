# Write your solution here
def range_of_list(my_list):
    if not my_list:
        return 0
    return max(my_list) - min(my_list)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)