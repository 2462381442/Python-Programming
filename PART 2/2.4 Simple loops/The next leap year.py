year = int(input("Year: "))
year2 = year + 1

while True:
    # 检查 year2 是否是闰年
    is_leap_year = (year2 % 4 == 0 and year2 % 100 != 0) or (year2 % 400 == 0)
    
    if is_leap_year:
        break  # 如果是闰年，则跳出循环
    else:
        year2 += 1 # 如果不是闰年，则年份加 1 继续检查

print(f"The next leap year after {year} is {year2}")