# 1. 询问用户输入一个数字
user_input = input("Please type in a number: ")
number = int(user_input)

# 2. 初始化一个从 1 开始的计数器
i = 1

# 3. 循环直到计数器超过输入的数字
while i <= number:
    # 4. 检查是否存在一个完整的数字对 (i 和 i + 1)
    #    这个条件确保我们不会打印出比用户输入还大的数字
    if i + 1 <= number:
        # 如果存在一个完整的对，先打印第二个数字...
        print(i + 1)
        # ...然后打印第一个数字
        print(i)
    else:
        # 如果只剩下最后一个数字（在奇数输入的情况下），就直接打印它
        print(i)

    # 5. 将计数器增加 2，以移动到下一对数字
    i = i + 2