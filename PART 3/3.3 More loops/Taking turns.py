# 1. 询问用户输入一个数字
user_input = input("Please type in a number: ")
number = int(user_input)

# 2. 初始化两个“指针”：一个在左边，一个在右边
left = 1
right = number

# 3. 循环直到两个指针相遇或交错
while left <= right:
    # 4. 打印左边的数字
    print(left)

    # 5. 如果左指针和右指针不指向同一个数字，
    #    才打印右边的数字，以避免在奇数情况下重复打印中间的数
    if left != right:
        print(right)

    # 6. 将指针向中间移动
    left = left + 1
    right = right - 1