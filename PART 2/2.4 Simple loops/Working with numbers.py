# 初始化用于存储统计数据的变量
numbers_typed_in = 0
sum_of_numbers = 0
positive_numbers = 0
negative_numbers = 0

# Pre-task: 要求用户输入数字，直到输入0为止
print("Please type in integer numbers. Type in 0 to finish.")

while True:
    # 获取用户输入
    user_input_str = input("Number: ")
    
    # 将输入转换为整数
    # 我们假设用户总是输入有效的整数，因为题目没有要求错误处理
    number = int(user_input_str)
    
    # 检查是否输入了0，如果是，则结束循环
    if number == 0:
        break
    
    # 如果数字不是0，则处理它
    
    # Part 1: 计数 (不包括最后的0)
    numbers_typed_in = numbers_typed_in + 1
    
    # Part 2: 求和 (不包括最后的0)
    sum_of_numbers = sum_of_numbers + number
    
    # Part 4: 统计正数和负数
    if number > 0:
        positive_numbers = positive_numbers + 1
    elif number < 0: # 使用 elif 来处理负数的情况
        negative_numbers = negative_numbers + 1
        
# 循环结束后，打印所有统计结果

# Part 1 输出: 打印输入数字的数量
print(f"Numbers typed in {numbers_typed_in}")

# Part 2 输出: 打印数字的总和
print(f"The sum of the numbers is {sum_of_numbers}")

# Part 3 输出: 计算并打印数字的平均值
# 题目假设用户至少会输入一个有效的非零数字，所以 numbers_typed_in 不会是0
if numbers_typed_in > 0:
    mean_of_numbers = sum_of_numbers / numbers_typed_in
    print(f"The mean of the numbers is {mean_of_numbers}")
else:
    # 根据题目假设，此分支理论上不会执行
    print("No numbers were entered to calculate the mean.")

# Part 4 输出: 打印正数和负数的数量
print(f"Positive numbers {positive_numbers}")
print(f"Negative numbers {negative_numbers}")
