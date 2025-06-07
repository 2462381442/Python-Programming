word = input("Word: ")

# 定义总宽度，方便修改
total_width = 30
# 内部文本区域的宽度
inner_width = total_width - 2 

# 检查单词是否太长
if len(word) > inner_width:
    print(f"错误：单词 '{word}' 太长，无法放入宽度为 {total_width} 的框中。")
else:
    # 计算需要填充的总空格数
    padding_total = inner_width - len(word)
    # 计算左侧的空格数
    padding_left = padding_total // 2
    # 计算右侧的空格数
    padding_right = padding_total - padding_left

    print("*" * total_width)
    print(f"*{' ' * padding_left}{word}{' ' * padding_right}*")
    print("*" * total_width)