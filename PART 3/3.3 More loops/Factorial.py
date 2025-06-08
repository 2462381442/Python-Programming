while True:
    # 1. 询问用户输入一个数字
    user_input = input("Please type in a number: ")
    number = int(user_input)

    # 2. 检查数字是否小于或等于0
    if number <= 0:
        print("Thanks and bye!")
        break  # 如果是，打印告别语并结束循环

    # 3. 如果数字是正数，则计算阶乘
    # 初始化阶乘结果为 1
    factorial = 1
    # 初始化一个计数器，从 1 开始
    counter = 1

    # 4. 使用 while 循环计算阶乘
    while counter <= number:
        factorial = factorial * counter
        counter = counter + 1  # 计数器加 1，直到等于输入的数字

    # 5. 打印结果
    print(f"The factorial of the number {number} is {factorial}")