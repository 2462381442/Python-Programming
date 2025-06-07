word = input("Please type in a word: ")
letter = input("Please type in a character: ")

# 查找字符第一次出现的位置
index = word.find(letter)

# 检查：1. 字符是否被找到 (index >= 0)
#       2. 找到的位置后面是否还有足够的字符来构成一个3字符的切片
if index >= 0 and index <= len(word) - 3:
    print(word[index:index+3])

# 如果以上条件不满足，程序会自然结束，不打印任何内容，符合题目要求。