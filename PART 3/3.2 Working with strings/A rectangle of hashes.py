width = int(input("Width: "))
len = 1
hight = int(input("Height: "))
times = 0

while width > 0 and hight > 0 and times < hight:
    len = width
    print("#"*len)
    times += 1