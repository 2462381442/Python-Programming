limit = int(input("Limit: "))
number = 1
total = 0
string = ""

while total < limit:
    total += number
    
    # --- 核心逻辑改动在这里 ---
    if string:  # 如果 string 不是空的 (即已经有数字了)
        string += " + " # 就先添加分隔符
    
    string += f"{number}" # 然后再添加数字
    # --- 核心逻辑改动结束 ---

    number += 1
    
string += f" = {total}"
print(f"The consecutive sum: {string}")