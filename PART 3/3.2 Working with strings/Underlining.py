# 第一次获取输入
string = input("Please type in a string:")

# 当字符串不为空时，进入循环
while string:
    print(string)
    print("-" * len(string))
    print("")
    # 在循环内部再次获取输入，以便更新 string 的值
    # 如果用户在这里直接按回车（输入空字符串），循环将在下一次判断时终止
    string = input("Please type in a string:")

print("Exiting...") # 可以加一句提示，表示程序已退出循环