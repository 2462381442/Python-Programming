# 1. 获取用户输入
word = input("Please type in a word: ")
letter = input("Please type in a character: ")

# 2. 循环遍历所有可能的起始索引
# 最后一个可能的起始位置是 len(word) - 3，所以 range 要到 len(word) - 2
# 例如，对于 "python" (长度6)，最后一个有效起始点是索引3 ('h')，可以切出 "hon"。
# 所以 i 的范围是 0, 1, 2, 3。 range(6-2) -> range(4) -> 0, 1, 2, 3。
for i in range(len(word) - 2):
    
    # 3. 检查当前位置的字符是否是我们要找的字符
    # word[i] 代表在索引 i 处的字符
    if word[i] == letter:
        
        # 4. 如果是，就打印从这个位置开始的3个字符的切片
        print(word[i:i+3])